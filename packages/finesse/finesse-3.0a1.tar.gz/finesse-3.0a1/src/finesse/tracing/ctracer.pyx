#cython: boundscheck=False, wraparound=False, initializedcheck=False

"""The data structures, and related algorithms, which form the basis of the beam tracing
library.

Details on each class, method and function in this sub-module are provided mostly for
developers. Users should refer to :ref:`tracing_manual` for details on beam tracing,
:meth:`.Model.beam_trace` for the main method through which beam traces can be performed
on a model and :mod:`.tracing.tools` for the various beam propagation tools which the
beam tracing library provides.
"""

from finesse.cymath cimport complex_t
from finesse.cymath.complex cimport conj
from finesse.cymath.gaussbeam cimport (
    transform_q,
    inv_transform_q,
    abcd_multiply,
    sym_abcd_multiply,
)
from finesse.cymath.math cimport float_eq

cimport numpy as np
import numpy as np

from copy import copy
from itertools import chain
import logging

import networkx as nx

from finesse.gaussian import BeamParam, transform_beam_param
from finesse.exceptions import TotalReflectionError
from finesse.utilities import refractive_index


LOGGER = logging.getLogger(__name__)


cdef class TraceForest:
    """A container structure which stores multiple :class:`.TraceTree` instances.

    The :class:`.Model` stores a TraceForest object which then represents the current
    tracing state of the configuration. Each time a :meth:`.Model.beam_trace` is called,
    either directly or indirectly, the TraceForest of the Model will be used to perform
    the tracing via propagation of the beam parameters through each tree. This is also
    detailed in :ref:`tracing_manual`.

    Determination of the ordering and overall structure of the TraceForest happens through
    the "planting" of the forest. By calling :meth:`.TraceForest.plant`, the forest is cleared
    and re-planted according to the ordered list of trace dependencies passed to this method.
    This is a step which is performed automatically in :meth:`.Model.beam_trace`, where this
    re-planting process only occurs under the following condition:

     * a connector has been added or removed since the last call,
     * the type of beam tracing has been switched from symmetric to
       asymmetric or vice-verase,
     * or the tracing priority (i.e. ordered list of trace dependencies)
       has changed in any way.

    In the initialisation process of building a simulation, a specialised version of a TraceForest
    is constructed from the model TraceForest using the ``TraceForest.make_changing_forest`` method.
    This inspects the model forest and selects only those trees, and branches of trees, which will
    have changing beam parameters during the simulation; i.e. due to some :class:`.GeometricParameter`
    being scanned. This new, "changing TraceForest" is then the optimised structure via which
    simulation-time beam traces (on changing beam parameter paths) are performed. More details on
    this, including additional powerful features that this changing forest provides, can be found
    in :ref:`tracing_manual`.
    """
    def __init__(self, object model):
        self.forest = []
        self.N_trees = 0

        self.dependencies = []

        self.symmetric = False

        self.model = model

        self.node_coverage = []
        self.internal_cavity_nodes = []

    def __deepcopy__(self, memo):
        raise RuntimeError("TraceForest instances cannot be copied.")

    def plant(self, list trace_order):
        """Constructs and stores all the trace trees according to
        the order of dependencies in `trace_order`.

        Parameters
        ----------
        trace_order : list
            List of the dependency objects by priority of tracing.
        """
        from finesse.components import Cavity

        self.clear()
        self.dependencies = trace_order.copy()

        # Always make the internal cavity trees first, these
        # will be generated in the order in which each cavity
        # appears in the trace_order dependency list
        cavities = list(filter(lambda x: isinstance(x, Cavity), self.dependencies))
        self._add_internal_cavity_trees(cavities)
        LOGGER.debug("TraceForest with internal Cavity trees: %s", self)

        # Handle ordering of internal cavity trees which overlap
        self._handle_overlapping_cavities()
        LOGGER.debug("TraceForest after overlapping cavities handled: %s", self)

        # Iterate through all dependencies by tracing order
        # and generate their associated trees
        for dep in self.dependencies:
            if isinstance(dep, Cavity):
                self._add_external_cavity_tree(dep)
            else:
                self._add_gauss_tree(dep)
        LOGGER.debug(
            "TraceForest with internal, external Cavity trees and Gauss trees: %s",
            self,
        )

        # Remove common sub-trees sequentially
        self.trim()
        LOGGER.debug("TraceForest after trimming: %s", self)
        # Update the node coverage list to take account
        # for changes made during trim
        self.node_coverage = list(self.gather_nodes())
        # Add branch trees at beam splitters where the nodes weren't
        # reachable from a previous trace tree
        cdef int missing = self._add_beamsplitter_branch_trees()
        LOGGER.debug("TraceForest after branch trees planted: %s", self)

        # If we're not symmetric and there are nodes which we can't
        # reach because of this (i.e. no path leading back to these
        # nodes), then we need to rectify this
        if not self.symmetric and missing:
            self._add_backwards_nonsymm_trees()
            LOGGER.debug("TraceForest after first backwards, asymmetric trees added: %s", self)
            # It's possible that there are still some branch nodes from beam splitters
            # that we couldn't reach at this point in asymmetric traces (e.g. a typical PDH
            # setup with a pick-off BS and one cav command), so we need to repeat the above
            # all over again to catch these trees
            if self._add_beamsplitter_branch_trees():
                self._add_backwards_nonsymm_trees()
            LOGGER.debug("TraceForest after last backwards, asymmetric trees added: %s", self)


        cdef set diff = self.find_untraversed_nodes()
        if len(diff):
            raise RuntimeError(
                "Bug encountered! The following optical nodes are missing from the "
                f"model trace forest:\n{diff}"
            )

    cpdef void clear(self):
        """Clears the trace forest, removing all trace trees."""
        self.forest.clear()
        self.N_trees = 0
        self.dependencies.clear()
        self.internal_cavity_nodes.clear()
        self.node_coverage.clear()

    def full_beam_trace(self):
        """Performs a "model-time" beam trace on all trace trees.

        This method is called internally by :meth:`.Model.beam_trace`. One should
        use that method to get a more complete representation of the tracing of
        the beam through a model.

        Returns
        -------
        trace : dict
            Dictionary of `node: (qx, qy)` mappings where `node` is each
            :class:`.OpticalNode` instance and `qx, qy` are the beam
            parameters in the tangential and sagittal planes, respectively,
            at these nodes.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

            double lambda0 = self.model.lambda0

            object node
            dict trace = {}

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            if tree.is_source:
                node = tree.node
                qx = tree.dependency.qx
                qy = tree.dependency.qy
                trace[node] = qx, qy
                if self.symmetric:
                    trace[node.opposite] = qx.reverse(), qy.reverse()

            propagate(tree, trace, lambda0, self.symmetric)

        return trace

    cdef int _add_internal_cavity_trees(self, list cavities) except -1:
        cdef:
            Py_ssize_t Ncavs = len(cavities)
            Py_ssize_t cav_idx
            object cav

        for cav_idx in range(Ncavs):
            cav = cavities[cav_idx]

            self.forest.append(TraceTree.from_cavity(cav))
            self.node_coverage.extend(cav.path.nodes_only)
            self.internal_cavity_nodes.extend(cav.path.nodes_only)
            self.N_trees += 1

        return 0

    cdef int _handle_overlapping_cavities(self) except -1:
        cdef:
            Py_ssize_t i, j
            TraceTree tree1, tree2

            list tree1_nodes = []
            list overlaps = []

        # Gather all the overlapping cavity combinations
        for i in range(self.N_trees):
            tree1 = self.forest[i]
            tree1_nodes = []
            _gather_nodes(tree1, tree1_nodes)
            for j in range(i + 1, self.N_trees):
                tree2 = self.forest[j]
                for node in tree1_nodes:
                    if tree2.contains_node(node):
                        overlaps.append((tree1, tree2))
                        break

        # If there are no overlaps then nothing to do here
        if not overlaps:
            return 0

        # Make a flattened list of the overlapping tree combinations
        merged = list(chain.from_iterable(overlaps))
        # and merge the column slices of these combinations to get
        # the correct ordering before the operations below
        merged = merged[::2] + merged[1::2]

        # From this, create a list of these unique trees with the order
        # reversed such that trees which were added first from the cavity
        # trace order will overwrite the branches of the later trees which
        # intersect with them. This then guarantees that the trace_order given
        # to TraceForest.plant will be preserved for overlapping cavities.
        new_inner_order = list(dict.fromkeys(reversed(merged)))

        # Remove the internal cavity trees which are present in this
        # overlapping trees container...
        self.forest = [tree for tree in self.forest if tree not in new_inner_order]
        # ... and then add them back in the order as outlined above
        for tree in new_inner_order:
            self.forest.append(tree)

        return 0

    cdef int _add_external_cavity_tree(self, object cav) except -1:
        cdef:
            dict exit_nodes
            object source, target

            TraceTree new_tree

        exit_nodes = cav.get_exit_nodes()
        for source, target in exit_nodes.items():
            new_tree = TraceTree.from_node(
                target,
                cav,
                self.symmetric,
                pre_node=source,
                exclude=self.node_coverage,
            )
            if new_tree is not None:
                self.forest.append(new_tree)
                self.N_trees += 1

                _gather_nodes(new_tree, self.node_coverage)

        return 0

    cdef int _add_gauss_tree(self, object gauss) except -1:
        cdef:
            object gauss_node = gauss.node

            Py_ssize_t tree_idx
            TraceTree tree, new_tree, found, fp, fpp
            TraceTree rm_tree
            set trees_to_remove = set()

        if gauss_node in self.internal_cavity_nodes:
            LOGGER.error(
                "Gauss object %s is at an internal Cavity node (%s). Ignoring "
                "this Gauss. Remove the corresponding Cavity object to "
                "propagate this Gauss object instead.",
                gauss.name,
                gauss_node.full_name,
            )
            return 0

        # Find branches in trees already planted that contain the gauss node
        # or its opposite direction
        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            found = tree.find_tree_at_node(gauss_node, include_opposite=True)
            if found is not None: # found a tree at the gauss node
                fp = found.parent
                if fp is not None: # this tree has a parent
                    # the parent node is an output i.e. a space exists between
                    # parent and the gauss -> so we want to remove parent too
                    if not fp.node.is_input:
                        fpp = fp.parent
                        if fpp is None: # parent has no parent so just remove the whole tree
                            trees_to_remove.add(tree)
                        else: # parent has a parent
                            if fp == fpp.left:
                                fpp.remove_left()
                            else:
                                fpp.remove_right()

                            # if the parent of parent has no remaining connections
                            # just remove the whole tree
                            if fpp.left is None and fpp.right is None and fpp.parent is None:
                                trees_to_remove.add(tree)
                    else: # parent node is an input (no space between parent -> gauss)
                        if found == fp.left:
                            fp.remove_left()
                        else:
                            fp.remove_right()

                        if fp.left is None and fp.right is None and fp.parent is None:
                            trees_to_remove.add(tree)
                else: # found tree has no parent so just remove the whole tree
                    trees_to_remove.add(tree)

        new_tree = TraceTree.from_node(
            gauss_node,
            gauss,
            self.symmetric,
            is_gauss=True,
            exclude=self.internal_cavity_nodes
        )
        if new_tree is not None:
            self.forest.append(new_tree)
            self.N_trees += 1

            _gather_nodes(new_tree, self.node_coverage)

        # if the opposite direction of gauss node is not in the forward propagated
        # gauss tree then we need to make a tree from gauss.opposite too
        if (
            self.symmetric or
            (
                new_tree is not None and
                new_tree.find_tree_at_node(gauss_node.opposite) is None
            )
        ):
            # backwards tree is not from the gauss node itself now
            # so leave is_gauss as False otherwise there would be
            # two sources from the same gauss node leading to problems
            back_new_tree = TraceTree.from_node(
                gauss_node.opposite,
                gauss,
                self.symmetric,
                exclude=self.internal_cavity_nodes
            )

            if (
                back_new_tree is not None and
                (back_new_tree.left is not None or back_new_tree.right is not None)
            ):
                self.forest.append(back_new_tree)
                self.N_trees += 1

                _gather_nodes(back_new_tree, self.node_coverage)

        for rm_tree in trees_to_remove:
            self.forest.remove(rm_tree)
            self.N_trees -= 1

        return 0

    cdef int _add_beamsplitter_branch_trees(self) except -1:
        cdef:
            double node_nr, pre_node_nr
            set diff = self.find_untraversed_nodes()
            dict branch_start_nodes = {}

            TraceTree new_tree

        from finesse.components.general import InteractionType

        if not diff:
            return 0

        for node in diff:
            pre = list(self.model.optical_network.predecessors(node.full_name))
            node_nr = refractive_index(node)
            for pre_node_name in pre:
                pre_node = self.node_from_name(pre_node_name)
                pre_node_nr = refractive_index(pre_node)
                # if predecessor node is also in the set of unreachable nodes OR
                # the interaction type from pre_node -> node is a reflection and
                # the refractive indices at these ports are not the same (total
                # internal reflection) then skip it
                if (
                    pre_node in diff
                    or (
                        node.component.interaction_type(pre_node, node) == InteractionType.REFLECTION
                        and not float_eq(node_nr, pre_node_nr)
                    )
                ):
                    continue

                # otherwise we want to store the predecessor node and its associated
                # dependency in a dict to make trees from later
                branch_start_nodes[node] = pre_node, self.find_dependency_from_node(pre_node)
                break

        if not branch_start_nodes:
            # Shouldn't ever have a case where a branched node does not have
            # a predecessor (when doing symmetric planting), so if this
            # happens a bug has been encountered
            if self.symmetric:
                raise RuntimeError(
                    "Bug encountered! Could not create branch trees from "
                    f"the following missed nodes: {diff}"
                )
            # But if we're not a symmetric forest, then this will occur in
            # most cases as (for anything but extremely simple files) there
            # will be nodes which can't be reached directly, so inform on
            # return that this is the case
            else:
                return 1

        for node, (pre_node, dependency) in branch_start_nodes.items():
            new_tree = TraceTree.from_node(
                node,
                dependency,
                self.symmetric,
                pre_node=pre_node,
                exclude=self.node_coverage,
            )
            if new_tree is not None:
                self.forest.append(new_tree)
                self.N_trees += 1
                _gather_nodes(new_tree, self.node_coverage)

        return self._add_beamsplitter_branch_trees()

    cdef int _add_backwards_nonsymm_trees(self) except -1:
        cdef:
            TraceTree tree
            # twisted tree root and branch
            TraceTree ttr, ttb

            object comp
            bint is_dependency_changing

        # Get all the nodes we can't reach due to the asymmetric trace
        unreachable_nodes = self.find_untraversed_nodes()
        for node in unreachable_nodes:
            tree = self.find_tree_from_node(node.opposite)
            if tree is None:
                continue

            is_dependency_changing = tree.dependency.is_changing
            # Here we begin the process of making a "twisted tree" where
            # the left sub-tree node is actually a pre-coupling of the
            # parent tree node, this will allow us to apply the inverse
            # ABCD law transformation to left sub-tree node during tracing
            ttr = TraceTree.initialise(
                tree.node, tree.dependency, &is_dependency_changing
            )
            ttb = TraceTree.initialise(
                node, tree.dependency, &is_dependency_changing
            )

            if ttb.node.is_input:
                comp = ttb.node.component
            else:
                comp = ttb.node.space

            ttr.left = ttb
            ttb.parent = ttr

            try:
                # Check that there is a coupling from unreachable node -> opposite
                comp.check_coupling(ttb.node, ttr.node)

                try:
                    # Just to re-iterate, here we get the ABCD matrix coupling from
                    # the left tree to the parent tree (opposite to usual) in order
                    # to use this matrix in the inverse ABCD law transformation
                    ttr.sym_left_abcd_x, ttr.left_abcd_x = comp.ABCD(
                        ttb.node, ttr.node, direction="x", copy=False, retboth=True,
                    )
                    ttr.sym_left_abcd_y, ttr.left_abcd_y = comp.ABCD(
                        ttb.node, ttr.node, direction="y", copy=False, retboth=True,
                    )
                except TotalReflectionError:
                    raise

                ttr.is_left_surf_refl = is_surface_refl(comp, ttb.node, ttr.node)

                ttb.is_x_changing |= (
                    ttr.sym_left_abcd_x is not None
                    and is_abcd_changing(ttr.sym_left_abcd_x)
                )
                ttb.is_y_changing |= (
                    ttr.sym_left_abcd_y is not None
                    and is_abcd_changing(ttr.sym_left_abcd_y)
                )

                # Now mark the twisted tree root as an inverse transformation tree
                ttr.do_inv_transform = True
            except ValueError:
                # No coupling exists from ttb.node -> ttr.node (typically means no
                # reflection coupling) so mark the root as needing a -q* operation
                # instead now as there is no other way to set the node q otherwise
                ttr.do_nonsymm_reverse = True

            self.forest.append(ttr)
            self.N_trees += 1
            _gather_nodes(ttr, self.node_coverage)

    cpdef set find_untraversed_nodes(self):
        """Finds all the optical nodes in the model which are not
        covered by the trace forest."""
        cdef:
            set nodes_traversed = set(self.node_coverage)
            set nominal_diff = set(self.model.optical_nodes).difference(nodes_traversed)
            set real_diff = set()

        if not self.symmetric:
            return nominal_diff

        for node in nominal_diff:
            if node.opposite not in nodes_traversed:
                real_diff.add(node)

        return real_diff

    cpdef TraceTree find_tree_from_node(self, object node):
        """Given an optical node, this finds the :class:`.TraceTree` instance
        corresponding to this node (if one exists).

        Parameters
        ----------
        node : :class:`.OpticalNode`
            An optical node.

        Returns
        -------
        tree : :class:`.TraceTree`
            The tree corresponding to `node`, or ``None`` if none found.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree, found

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            found = tree.find_tree_at_node(node, self.symmetric)
            if found is not None:
                return found

        return None

    cpdef object find_dependency_from_node(self, object node, bint raise_not_found=True):
        """Finds the dependency object associated with the optical `node`.

        If no tree is found associated with this node, and `raise_not_found` is true,
        then a ``RuntimeError`` is raised. Otherwise `None` is returned.

        Parameters
        ----------
        node : :class:`.OpticalNode`
            An optical node.

        raise_not_found : bool, optional; default: True
            Raises a RuntimeError if no dependency found. Returns `None` if False.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree, found

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            found = tree.find_tree_at_node(node, self.symmetric)
            if found is not None:
                return found.dependency

        if raise_not_found:
            raise RuntimeError(
                "Bug encountered! Could not find a dependency object "
                f"associated with node {node.full_name} in the trace forest."
            )
        else:
            return None

    cpdef set gather_nodes(self):
        """Generates a set of all the optical nodes covered by the forest."""
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

            list gather = []

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            _gather_nodes(tree, gather)

        return set(gather)

    cdef object node_from_name(self, name):
        return self.model.network.nodes[name]["weakref"]()

    cdef TraceForest make_changing_forest(self):
        """Constructs a new TraceForest from this forest, consisting
        of only the trees which will have changing beam parameters.

        This method is called in BaseSimulation._initialise for setting
        up the simulation trace forest used for efficient beam tracing.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree, chtree

            list changing_trees = []
            bint branch_added = False
            TraceForest changing_forest = TraceForest(self.model)

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]
            branch_added = False
            # For branched beamsplitter trees, need to see if the root
            # node opposite is already present in the changing trees
            # list --- if so then add the branch tree as this will also
            # be changing
            for chtree in changing_trees:
                if chtree.find_tree_at_node(tree.node.opposite) is not None:
                    changing_trees.append(tree)
                    branch_added = True
                    break

            if not branch_added:
                # From this tree, obtain the broadest sub-trees which
                # will have changing beam parameters
                changing_trees.extend(tree.get_broadest_changing_subtrees())

        cdef Py_ssize_t Nchanging_nominal = len(changing_trees)
        cdef set roots = set() # Parents of changing trees
        cdef set trees_to_remove = set()
        for tree_idx in range(Nchanging_nominal):
            tree = changing_trees[tree_idx]
            # Now set each changing tree to the parent tree so that
            # the root is used in beam tracing...
            if tree.parent is not None:
                # ... but only do this for parents not yet added
                # otherwise could get duplicate trees
                if tree.parent not in roots:
                    changing_trees[tree_idx] = tree.parent
                    roots.add(tree.parent)
                else:
                    # This tree will already be encapsulated by the previous
                    # parent so just mark it to be removed
                    trees_to_remove.add(tree)

        for tree in trees_to_remove:
            changing_trees.remove(tree)

        changing_forest.forest = changing_trees
        changing_forest.N_trees = len(changing_trees)
        changing_forest.symmetric = self.symmetric
        changing_forest.internal_cavity_nodes = self.internal_cavity_nodes

        return changing_forest

    cpdef bint contains_space(self, object space):
        """Whether this trace forest contains the specified space.

        Parameters
        ----------
        space : :class:`.Space`
            A space instance.

        Returns
        -------
        flag : bool
            True if the forest contains `space`, False otherwise.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            if tree.contains_space(space):
                return True

        return False

    cpdef bint contains_comp(self, object comp):
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            if tree.contains_comp(comp):
                return True

        return False

    cpdef tuple find_potential_mismatch_couplings(self, TraceForest other=None):
        """Retrieves the node couplings which are potentially mode mismatched. If
        `other` is not given then the couplings which are local to this forest only
        will be found, otherwise couplings between this forest and `other` will
        be retrieved.

        If this forest is asymmetric, then calling this method is equivalent to
        calling :meth:`.TraceForest.find_intersection_couplings`.

        This method is used internally for obtaining all the possible mode mismatch
        couplings between a changing trace forest (held by a modal simulation) and
        the main model trace forest.

        Parameters
        ----------
        other : :class:`.TraceForest`
            Find dependencies from a different trace forest than this one
            when checking for mode mismatch couplings.

        Returns
        -------
        couplings : tuple
            A tuple of the node couplings where each element is ``(from_node, to_node)``.
        """
        from finesse.components.general import InteractionType

        intersect_couplings = self.find_intersection_couplings(other)

        cdef list refls = []
        cdef list fake_refl_mismatches = []
        cdef tuple other_mrefls
        cdef object[:, ::1] refl_abcd_sym_x
        cdef object[:, ::1] refl_abcd_sym_y
        # If we're doing a symmetric trace then self-reflections from mirror-type components
        # can be potential mode mismatch couplings so need to add these too
        if self.symmetric:
            refls.extend(self.get_mirror_reflection_couplings())
            for node1, node2 in refls:
                opp_surface_onode = None
                # Find the output node on the other side of the surface
                for n1s_name in list(self.model.optical_network.successors(node1.full_name)):
                    n1s = self.node_from_name(n1s_name)
                    if node1.component.interaction_type(node1, n1s) == InteractionType.TRANSMISSION:
                        opp_surface_onode = n1s
                        break

                # If none found then nothing else needs to be done for this coupling
                if opp_surface_onode is None:
                    continue

                # Reflection coupling on other side of surface is in the potential
                # mismatch couplings so this one can remain too
                if (opp_surface_onode.opposite, opp_surface_onode) in refls:
                    continue

                # Get the dependencies associated with the two sides of the surface
                dep1 = self.find_dependency_from_node(node1)
                dep2 = self.find_dependency_from_node(opp_surface_onode, raise_not_found=False)
                if dep2 is None and other is not None:
                    dep2 = other.find_dependency_from_node(opp_surface_onode)

                # Finally, if the dependencies of the trees on both sides are the same
                # then this isn't really a mismatch coupling (as beam params on both sides
                # are guaranteed to be mode matched in such a case) so mark it to be removed
                if dep1 is dep2:
                    fake_refl_mismatches.append((node1, node2))

            for fnodes in fake_refl_mismatches:
                refls.remove(fnodes)

            # In addition, if the model trace forest is specified via other
            # then we need to check for reflection couplings here which
            # impinge against connectors with changing ABCDs as these will
            # also be potential mode mismatch couplings
            if other is not None:
                other_mrefls = other.get_mirror_reflection_couplings(
                    skip_dependencies=self.dependencies,
                )

                for node1, node2 in other_mrefls:
                    # Don't add the coupling if we already determined that it
                    # was a "fake" mismatch coupling (see above)
                    if (node1, node2) in fake_refl_mismatches:
                        continue

                    comp = node1.component
                    # Get the symbolic ABCDs upon reflection from the surface...
                    refl_abcd_sym_x = comp.ABCD(
                        node1, node2, "x", copy=False, symbolic=True
                    )
                    refl_abcd_sym_y = comp.ABCD(
                        node1, node2, "y", copy=False, symbolic=True
                    )

                    # ... and check if they're changing, if so we have another
                    # possible mode mismatch coupling which needs to be added
                    if is_abcd_changing(refl_abcd_sym_x) or is_abcd_changing(refl_abcd_sym_y):
                        refls.append((node1, node2))

        return intersect_couplings + tuple(set(refls))


    cpdef tuple find_intersection_couplings(self, TraceForest other=None):
        """Finds the node couplings at which trees with differing trace dependencies intersect.

        Parameters
        ----------
        other : :class:`.TraceForest`
            Find dependencies from a different trace forest than this one
            when checking for intersections.

        Returns
        -------
        couplings : tuple
            A tuple of the node couplings where each element is ``(from_node, to_node)``.
        """
        cdef:
            Py_ssize_t otree_idx, itree_idx
            TraceTree tree

            list couplings = []

        if not self.N_trees:
            return ()

        for otree_idx in range(self.N_trees):
            tree = self.forest[otree_idx]

            # Get the final *input* nodes at the end of the tree, across all branches
            last_nodes = tree.get_last_input_nodes()
            # Need to also add the reverse node of the tree if it's a source
            # tree so that intersections are checked in the other propagation
            if tree.is_source and tree.node.opposite not in last_nodes:
                last_nodes.append(tree.node.opposite)

            for node in last_nodes:
                # Obtain the successor nodes of this (if any) from the network
                succ_nodes = list(self.model.optical_network.successors(node.full_name))

                for snode_name in succ_nodes:
                    snode = self.node_from_name(snode_name)
                    # Then for each successor node find its TraceTree in the forest
                    # and obtain the dependency that this relies upon
                    if other is None:
                        snode_dep = self.find_dependency_from_node(snode)
                    else:
                        snode_dep = other.find_dependency_from_node(snode)

                    # If this dependency is not the same object as the original tree's
                    # dependency then we've found an intersection so add this coupling
                    if snode_dep is not tree.dependency:
                        # Here we do some sanity checks on the coupling we've found
                        comp = node.component
                        scomp = snode.component
                        if node.component is not snode.component:
                            raise RuntimeError(
                                "Bug encountered! Found an intersection coupling "
                                f"{node.full_name} -> {snode.full_name} which "
                                "does not occur across the same connector."
                            )
                        node.component.check_coupling(node, snode)

                        couplings.append((node, snode))
                        # Add the reverse coupling too if it exists
                        try:
                            node.component.check_coupling(snode.opposite, node.opposite)
                            couplings.append((snode.opposite, node.opposite))
                        except:
                            pass

        return tuple(set(couplings))

    cpdef tuple get_mirror_reflection_couplings(
        self,
        bint ignore_internal_cavities=True,
        list skip_dependencies=None,
    ):
        """Get the node couplings in the forest which correspond to self-reflections
        from mirror-like components.

        Parameters
        ----------
        ignore_internal_cavities : bool, default: True
            Ignore the node couplings inside cavities.

        skip_dependencies : list
            Optional list of trees to skip based on their dependencies.

        Returns
        -------
        couplings : tuple
            A sequence of tuples consisting of the node1 -> node2 self
            reflection couplings.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

            list couplings = []

        from finesse.components import Cavity

        if skip_dependencies is None:
            skip_dependencies = []

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]

            if tree.dependency in skip_dependencies:
                continue

            if ignore_internal_cavities:
                # The tree is an internal cavity tree itself so skip the whole thing
                if tree.is_source and isinstance(tree.dependency, Cavity):
                    continue

                # If it's a tree coming directly from an internal cavity tree then
                # get the reflection couplings only from the second node onwards
                if tree.node in self.internal_cavity_nodes:
                    if tree.left is not None:
                        couplings.extend(tree.left.get_mirror_reflection_couplings())
                else:
                    couplings.extend(tree.get_mirror_reflection_couplings())
            else:
                couplings.extend(tree.get_mirror_reflection_couplings())

        return tuple(set(couplings))

    cdef void trim(self):
        cdef:
            Py_ssize_t i, j
            TraceTree tree1, tree2

            list tree1_nodes = []
            set trees_to_remove = set()

        from finesse.components import Gauss

        for i in range(self.N_trees):
            tree1 = self.forest[i]
            tree1_nodes = []
            _gather_nodes(tree1, tree1_nodes)

            for j in range(i + 1, self.N_trees):
                tree2 = self.forest[j]
                # Don't attempt to trim common nodes for internal cavity trees
                if not tree2.is_source or isinstance(tree2.dependency, Gauss):
                    # If any parts of tree2 overlap with tree1 then trim off
                    # these branches of tree2 to ensure uniqueness of trees
                    tree2.trim_at_nodes(tree1_nodes, self.symmetric)

                    if not tree2.is_source:
                        # Tree has no branches left so can be removed entirely
                        if tree2.left is None and tree2.right is None:
                            trees_to_remove.add(tree2)

        for tree in trees_to_remove:
            self.forest.remove(tree)
            self.N_trees -= 1

    cpdef draw_by_dependency(self):
        """Draws the forest as a string representation.

        All the trees in the forest are sorted by their dependency and
        stored in the resultant string by these dependency sub-headings. Each
        tree also has its index (i.e. tracing priority) stored in the string
        above the drawn tree.

        Returns
        -------
        forest_str : str
            A string representation of the forest, sorted by dependency with
            tracing priority indices displayed for each tree.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

            list dependencies = []

            all_trees_str = ""

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]
            if tree.dependency not in dependencies:
                dependencies.append(tree.dependency)

        for dependency in dependencies:
            # Make sub-heading for each dependency, giving its name and type name
            all_trees_str += f"\nDependency: {dependency.name} [{type(dependency).__name__}]\n\n"
            for tree_idx in range(self.N_trees):
                tree = self.forest[tree_idx]
                if tree.dependency == dependency:
                    # Give the index of the tree in the forest before drawing each tree
                    # -> indicates tracing order of the tree
                    all_trees_str += (
                        f"  (Index: {tree_idx})\n" + tree.draw(left_pad="    ") + "\n\n"
                    )

        return all_trees_str

    cpdef draw(self):
        """Draws the forest, by trace priority, as a string representation.

        The order in which trees appear in this string represents the order in which
        they will be traced during the beam tracing algorithm.

        In the rare cases where a subsequent tree contains a duplicate node (from an
        earlier tree), the latter tree trace will overwrite the former. This is only
        applicable to configurations with overlapping cavities, and this overwriting
        behaviour will take account of the desired cavity ordering given by the user.

        Returns
        -------
        forest_str : str
            A string representation of the ordered forest.
        """
        cdef:
            Py_ssize_t tree_idx
            TraceTree tree

            object last_dep = None
            all_trees_str = ""

        for tree_idx in range(self.N_trees):
            tree = self.forest[tree_idx]
            dep = tree.dependency

            if dep is not last_dep:
                all_trees_str += f"\nDependency: {dep.name} [{type(dep).__name__}]\n\n"
            else:
                all_trees_str += "\n"

            all_trees_str += tree.draw(left_pad="  ") + "\n"

            last_dep = dep

        return all_trees_str

    def __str__(self):
        return self.draw()


cdef class TraceTree:
    """A binary tree data structure representing all the beam tracing
    paths from some root optical node of a model.

    Each instance of this class has a `left` and `right` sub-tree (of the
    class type) and a parent tree. These linked tree attributes can be None. If
    the tree has a left / right sub-tree then the memoryviews `left_abcd_x`,
    `left_abcd_y` etc. will be initialised from the numerical ABCD matrix from
    the tree's optical node to the next tree's optical node.

    Every sub-tree has a `dependency` attribute which is the object that the
    trace tree depends on - either a :class:`.Cavity` or a :class:`.Gauss`
    instance."""
    def __init__(self, object node, object dependency):
        self.parent = None
        self.left = None
        self.right = None

        self.dependency = dependency # the source object (a cavity or gauss)
        self.node = node # the optical node

        self.is_source = False

        # These will get set in TraceTree.initialise afterwards anyway
        self.is_x_changing = False
        self.is_y_changing = False

        self.left_abcd_x = None
        self.left_abcd_y = None
        self.right_abcd_x = None
        self.right_abcd_y = None
        self.is_left_surf_refl = False

        self.sym_left_abcd_x = None
        self.sym_left_abcd_y = None
        self.sym_right_abcd_x = None
        self.sym_right_abcd_y = None

        self.nr = refractive_index(self.node)

        self.node_id = 0
        self.opp_node_id = 0

        self.do_inv_transform = False
        self.do_nonsymm_reverse = False

    def __deepcopy__(self, memo):
        raise RuntimeError("TraceTree instances cannot be copied.")

    @staticmethod
    cdef TraceTree initialise(
        object node, object dependency, bint* is_dependency_changing=NULL
    ):
        cdef TraceTree tree = TraceTree(node, dependency)

        cdef bint is_dep_changing
        if is_dependency_changing == NULL:
            if dependency is None:
                is_dep_changing = False
            else:
                is_dep_changing = dependency.is_changing
        else:
            is_dep_changing = is_dependency_changing[0]

        tree.is_x_changing = is_dep_changing
        tree.is_y_changing = is_dep_changing

        return tree

    @classmethod
    def from_cavity(cls, cavity):
        """Construct a TraceTree from a cavity instance.

        The resulting tree decays to a linked list as it
        just includes the internal path of the cavity.

        Parameters
        ----------
        cavity : :class:`.Cavity`
            The cavity object.

        Returns
        -------
        tree : :class:`.TraceTree`
            The tree representing the internal cavity path.
        """
        cdef:
            list path = cavity.path.nodes_only
            Py_ssize_t num_nodes = len(path)
            TraceTree parent = None
            TraceTree root

            object node

            bint cav_is_changing = cavity.is_changing

        root = TraceTree.initialise(path[0], cavity, &cav_is_changing)
        root.is_source = True
        parent = root

        cdef Py_ssize_t i
        for i in range(1, num_nodes):
            node = path[i]

            parent = parent.add_left(TraceTree.initialise(node, cavity, &cav_is_changing))

        # Add the final reflection ABCDs for last tree node back to source
        # so that round-trip ABCD can be efficiently computed from root
        parent.left_abcd_x = parent.node.component.ABCD(
            parent.node, root.node, direction='x', copy=False
        )
        parent.left_abcd_y = parent.node.component.ABCD(
            parent.node, root.node, direction='y', copy=False
        )

        # co-ordinate system transformation on reflection due
        # to rotation around vertical axis (inversion)
        parent.is_left_surf_refl = is_surface_refl(
            parent.node.component, parent.node, root.node
        )

        return root

    @staticmethod
    def from_path(list path):
        """Construct a TraceTree from a list of optical nodes.

        The resulting tree decays to a linked list as the path
        is 1D - no branches will occur.

        Parameters
        ----------
        path : list
            A list of optical nodes representing the node path. This
            can be obtained from a :class:`.OpticalPath` instance
            by invoking :attr:`.OpticalPath.nodes_only`.

        Returns
        -------
        tree : :class:`.TraceTree`
            The tree representing the node path.
        """
        cdef:
            Py_ssize_t num_nodes = len(path)
            TraceTree parent = None
            TraceTree root

            object node

        if not num_nodes:
            return None

        root = TraceTree.initialise(path[0], None)
        parent = root

        cdef Py_ssize_t i
        for i in range(1, num_nodes):
            node = path[i]

            parent = parent.add_left(TraceTree.initialise(node, None))

        return root

    @classmethod
    def from_node(
        cls,
        node,
        object dependency,
        bint symmetric,
        pre_node=None,
        bint is_gauss=False,
        list exclude=None,
    ):
        """Construct a TraceTree from an optical node root.

        The resulting tree includes all optical node paths traced
        forward from `node`.

        Parameters
        ----------
        node : :class:`.OpticalNode`
            The root node.

        dependency : :class:`.Cavity` or :class:`.Gauss`
            The dependency object - i.e. what the trace sub-trees depend on.

        symmetric : bool
            Flag indicating whether the tree should be constructed assuming
            that opposite node beam parameters will be set via the reverse
            of the original node beam parameter (true indicates this will be
            the case). In practice, this means that the resultant tree will
            not include any duplicate ports.

        pre_node : :class:`.OpticalNode`, optional; default: None
            An optional node to add before the root for the root sub-tree.

        is_gauss : bool, optional; default: False
            Whether the root node is a gauss node or not.

        Returns
        -------
        tree : :class:`.TraceTree`
            The tree of all paths from `node`.
        """
        cdef:
            object model = node._model

            TraceTree new_root = None
            TraceTree root = None
            TraceTree parent

            dict sub_trees = {}

            unicode n_name
            unicode nbr_name
            dict nbrsdict

            set excl = set()

            bint is_dependency_changing = dependency.is_changing

        if pre_node is not None:
            new_root = TraceTree.initialise(pre_node, dependency, &is_dependency_changing)

        if exclude is not None:
            excl = set(exclude)

        node_from_name = lambda n: model.network.nodes[n]["weakref"]()
        tree = nx.bfs_tree(model.optical_network, node.full_name)
        sub_trees = {}
        cdef Py_ssize_t i, j

        for i, (n_name, nbrsdict) in enumerate(tree.adjacency()):
            n = node_from_name(n_name)

            if n in excl or (symmetric and n.opposite in excl):
                if not i:
                    break

                continue

            excl.add(n)

            if not i:
                root = parent = TraceTree.initialise(n, dependency, &is_dependency_changing)
            else:
                parent = sub_trees.get(n_name, None)
                if parent is None:
                    continue

            for j, nbr_name in enumerate(nbrsdict.keys()):
                nbr = node_from_name(nbr_name)

                if nbr in excl or (symmetric and nbr.opposite in excl):
                    continue

                if not j:
                    sub_trees[nbr_name] = parent.add_left(
                        TraceTree.initialise(nbr, dependency, &is_dependency_changing)
                    )
                else:
                    sub_trees[nbr_name] = parent.add_right(
                        TraceTree.initialise(nbr, dependency, &is_dependency_changing)
                    )

        if root is None:
            return None

        if new_root is not None:
            new_root.add_left(root)
            new_root.is_source = is_gauss
        else:
            root.is_source = is_gauss

        return new_root or root

    cpdef TraceTree add_left(self, TraceTree sub_tree):
        """Add a left sub-tree to the tree.

        Parameters
        ----------
        sub_tree : :class:`.TraceTree`
            The tree to add to the left.

        Returns
        -------
        sub_tree : :class:`.TraceTree`
            The same tree that was added. This is useful for
            looping over a single branch of the tree as a parent
            tree can be set to the return of this method on each iteration.
        """
        cdef:
            object comp
            object parent_node = self.node

        self.left = sub_tree
        sub_tree.parent = self

        if parent_node.is_input:
            comp = parent_node.component
        else:
            comp = parent_node.space

        try:
            self.sym_left_abcd_x, self.left_abcd_x = comp.ABCD(
                parent_node, sub_tree.node, direction='x', copy=False, retboth=True
            )
            self.sym_left_abcd_y, self.left_abcd_y = comp.ABCD(
                parent_node, sub_tree.node, direction='y', copy=False, retboth=True
            )
        except TotalReflectionError:
            raise

        # co-ordinate system transformation on reflection due
        # to rotation around vertical axis (inversion)
        self.is_left_surf_refl = is_surface_refl(comp, parent_node, sub_tree.node)

        sub_tree.is_x_changing |= (
            self.sym_left_abcd_x is not None
            and is_abcd_changing(self.sym_left_abcd_x)
        )
        sub_tree.is_y_changing |= (
            self.sym_left_abcd_x is not None
            and is_abcd_changing(self.sym_left_abcd_y)
        )

        return sub_tree

    cpdef TraceTree add_right(self, TraceTree sub_tree):
        """Add a right sub-tree to the tree.

        Parameters
        ----------
        sub_tree : :class:`.TraceTree`
            The tree to add to the right.

        Returns
        -------
        sub_tree : :class:`.TraceTree`
            The same tree that was added. This is useful for
            looping over a single branch of the tree as a parent
            tree can be set to the return of this method on each iteration.
        """
        cdef:
            object comp
            object parent_node = self.node

        self.right = sub_tree
        sub_tree.parent = self

        if parent_node.is_input:
            comp = parent_node.component
        else:
            comp = parent_node.space

        try:
            self.sym_right_abcd_x, self.right_abcd_x = comp.ABCD(
                parent_node, sub_tree.node, direction='x', copy=False, retboth=True
            )
            self.sym_right_abcd_y, self.right_abcd_y = comp.ABCD(
                parent_node, sub_tree.node, direction='y', copy=False, retboth=True
            )
        except TotalReflectionError:
            raise

        sub_tree.is_x_changing |= (
            self.sym_right_abcd_x is not None
            and is_abcd_changing(self.sym_right_abcd_x)
        )
        sub_tree.is_y_changing |= (
            self.sym_right_abcd_y is not None
            and is_abcd_changing(self.sym_right_abcd_y)
        )

        return sub_tree

    cpdef bint remove_left(self):
        if self.left is None:
            return False

        self.left = None
        self.left_abcd_x = None
        self.left_abcd_y = None
        self.is_left_surf_refl = False

        return True

    cpdef bint remove_right(self):
        if self.right is None:
            return False

        self.right = None
        self.right_abcd_x = None
        self.right_abcd_y = None

        return True

    cdef void trim_at_nodes(
        self, list nodes, bint include_opposite=False
    ):
        if self.left is not None:
            if self.left.node in nodes or (include_opposite and self.left.node.opposite in nodes):
                self.remove_left()
            else:
                self.left.trim_at_nodes(nodes, include_opposite)

        if self.right is not None:
            if self.right.node in nodes or (include_opposite and self.right.node.opposite in nodes):
                self.remove_right()
            else:
                self.right.trim_at_nodes(nodes, include_opposite)

    cdef TraceTree _propagate_find_tree_at_node(
        self,
        TraceTree tree,
        object node,
        bint include_opposite
    ):
        if tree.node == node or (include_opposite and tree.node.opposite == node):
            return tree

        if tree.left is not None:
            lftree = self._propagate_find_tree_at_node(tree.left, node, include_opposite)
            if lftree is not None:
                return lftree

        if tree.right is not None:
            rftree = self._propagate_find_tree_at_node(tree.right, node, include_opposite)
            if rftree is not None:
                return rftree

        return None

    cpdef TraceTree find_tree_at_node(self, object node, bint include_opposite=False):
        return self._propagate_find_tree_at_node(self, node, include_opposite)

    cdef _get_last_input_nodes(self, list last_nodes):
        if self.left is None and self.right is None:
            if self.node.is_input:
                last_nodes.append(self.node)
            else:
                last_nodes.append(self.parent.node)
                # If we're at a beamsplitter then get opposite node
                # of reflection to last node so that both transmission
                # intersections can be picked up properly
                # TODO (sjr) Not sure if this is appropriate for asymmetric
                #            tracing yet, need to think about it
                if self.node.port is not self.parent.node.port:
                    last_nodes.append(self.node.opposite)

        if self.left is not None:
            self.left._get_last_input_nodes(last_nodes)

        if self.right is not None:
            self.right._get_last_input_nodes(last_nodes)

    cpdef list get_last_input_nodes(self):
        cdef:
            list last_nodes = []

        if self.left is None and self.right is None:
            last_nodes.append(self.node)

        if self.left is not None:
            self.left._get_last_input_nodes(last_nodes)

        if self.right is not None:
            self.right._get_last_input_nodes(last_nodes)

        return last_nodes

    cpdef bint contains_node(self, object node):
        return self.find_tree_at_node(node) is not None

    cpdef bint contains_space(self, object space):
        if not self.node.is_input:
            tspace = self.node.space
            if tspace is space:
                return True

        cdef bint left_contains_space = False
        if self.left is not None:
            left_contains_space = self.left.contains_space(space)

        cdef bint right_contains_space = False
        if self.right is not None:
            right_contains_space = self.right.contains_space(space)

        return left_contains_space or right_contains_space

    cpdef bint contains_comp(self, object comp):
        for node in comp.optical_nodes:
            if self.contains_node(node):
                return True

        return False

    cdef __append_mirror_refl_coupling(self, list couplings):
        from finesse.components.surface import Surface

        opp_node = self.node.opposite
        comp = self.node.component
        if opp_node.port is self.node.port and isinstance(comp, Surface):
            # Make sure both sides of the surface get included if encountered
            if self.node.is_input:
                node1 = self.node
                node2 = opp_node
            else:
                node1 = opp_node
                node2 = self.node

            # Check that the reflection coupling makes sense
            if comp.is_valid_coupling(node1, node2):
                couplings.append((node1, node2))

    cdef _get_mirror_refl_couplings(self, list couplings):
        self.__append_mirror_refl_coupling(couplings)

        if self.left is not None:
            self.left._get_mirror_refl_couplings(couplings)

        if self.right is not None:
            self.right._get_mirror_refl_couplings(couplings)

    cpdef list get_mirror_reflection_couplings(self):
        cdef list couplings = []

        self.__append_mirror_refl_coupling(couplings)

        if self.left is not None:
            self.left._get_mirror_refl_couplings(couplings)

        if self.right is not None:
            self.right._get_mirror_refl_couplings(couplings)

        return couplings

    @staticmethod
    cdef bint subtrees_changing(TraceTree sub_tree):
        cdef TraceTree child

        for child in (sub_tree.left, sub_tree.right):
            if child is None:
                continue

            if child.is_x_changing or child.is_y_changing:
                return True

            if TraceTree.subtrees_changing(child):
                return True

        return False

    cpdef bint is_changing(self, bint recursive=True):
        if not recursive:
            return self.is_x_changing or self.is_y_changing

        if self.is_x_changing or self.is_y_changing:
            return True

        return TraceTree.subtrees_changing(self)

    cdef list get_broadest_changing_subtrees(self):
        cdef:
            list changing_trees = []

        _gather_changing_sub_trees(self, changing_trees)
        return changing_trees

    cpdef draw(self, unicode left_pad=""):
        cdef:
            unicode first = self.node.full_name
            list lines = [left_pad + "o" + " " + first]

        _draw_tree(self, "", lines)
        treestr = f"\n{left_pad}".join(lines)

        return treestr

    def __str__(self):
        return self.draw()

    cpdef trace_beam(self, dict trace, double lambda0, bint symmetric):
        """Trace the beam through the tree, placing the beam parameter
        entries at each node in the `trace` dict.
        """
        cdef:
            object node

        if self.is_source:
            node = self.node
            qx = self.dependency.qx
            qy = self.dependency.qy
            trace[node] = qx, qy
            if symmetric:
                trace[node.opposite] = qx.reverse(), qy.reverse()

        propagate(self, trace, lambda0, symmetric)


cdef void _draw_tree(TraceTree tree, unicode lpad, list lines):
    cdef:
        unicode pad
        unicode branch = "├─"
        unicode pipe = "│"
        unicode end = "╰─"
        unicode dash = "─"

        TraceTree ltree = tree.left
        TraceTree rtree = tree.right

    if ltree is not None:
        s = branch + dash
        if rtree is None:
            s = end + dash
            pad = "   "
        else:
            s = branch + dash
            pad = pipe + "   "
        lines.append(lpad + s + "o" + " " + ltree.node.full_name)
        _draw_tree(ltree, lpad + pad, lines)

    if rtree is not None:
        s = end + dash
        pad = "   "
        lines.append(lpad + s + "o" + " " + rtree.node.full_name)
        _draw_tree(rtree, lpad + pad, lines)

cdef void _gather_nodes(TraceTree tree, list gather):
    gather.append(tree.node)

    if tree.left is not None:
        _gather_nodes(tree.left, gather)

    if tree.right is not None:
        _gather_nodes(tree.right, gather)

cdef void _gather_changing_sub_trees(TraceTree tree, list changing_trees):
    cdef:
        TraceTree ltree = tree.left
        TraceTree rtree = tree.right

    if tree.is_changing(recursive=False):
        changing_trees.append(tree)
        return

    if ltree is not None:
        _gather_changing_sub_trees(ltree, changing_trees)
    if rtree is not None:
        _gather_changing_sub_trees(rtree, changing_trees)


cpdef TraceTree get_last_left_branch(TraceTree tree):
    while tree.left is not None:
        if tree.left is None:
            break

        tree = tree.left

    return tree


cpdef bint is_abcd_changing(object[:, ::1] M):
    cdef:
        Py_ssize_t i, j
        bint is_changing

    for i in range(2):
        for j in range(2):
            is_changing = getattr(M[i][j], "is_changing", False)
            if is_changing:
                return True

    return False


cpdef void update_rt_abcd(
    TraceTree tree,
    double[:, ::1] ABCDx,
    double[:, ::1] ABCDy
):
    cdef:
        TraceTree t = tree
        Py_ssize_t i, j

    # Reset round trip ABCD to identity
    for i in range(2):
        for j in range(2):
            if i == j:
                ABCDx[i][j] = 1.0
                ABCDy[i][j] = 1.0
            else:
                ABCDx[i][j] = 0.0
                ABCDy[i][j] = 0.0

    # Find the bottom first as round-trip matrix is
    # computed from multiplying each ABCD "upwards"
    # in the internal tree
    while t.left is not None:
        if t.left is None:
            break

        t = t.left

    while t is not None:
        abcd_multiply(ABCDx, t.left_abcd_x, out=ABCDx, m2_refl_transform=t.is_left_surf_refl)
        abcd_multiply(ABCDy, t.left_abcd_y, out=ABCDy)

        t = t.parent


def update_single_rt_abcd(
    TraceTree tree,
    double[:, ::1] ABCD,
    unicode direction
):
    cdef:
        TraceTree t = tree
        Py_ssize_t i, j
        bint is_x_plane = direction == 'x'

    # Reset round trip ABCD to identity
    for i in range(2):
        for j in range(2):
            if i == j:
                ABCD[i][j] = 1.0
            else:
                ABCD[i][j] = 0.0

    while t.left is not None:
        if t.left is None:
            break

        t = t.left

    while t is not None:
        if is_x_plane:
            abcd_multiply(ABCD, t.left_abcd_x, out=ABCD, m2_refl_transform=t.is_left_surf_refl)
        else:
            abcd_multiply(ABCD, t.left_abcd_y, out=ABCD)

        t = t.parent


cdef void propagate(TraceTree tree, dict trace, double lambda0, bint symmetric):
    cdef:
        object this_node = tree.node
        TraceTree ltree = tree.left
        TraceTree rtree = tree.right
        object left_node = None if ltree is None else ltree.node
        object right_node = None if rtree is None else rtree.node

        tuple q1 = trace[this_node]
        complex_t qx1_q = q1[0].q
        complex_t qy1_q = q1[1].q

        complex_t qx2_q, qy2_q

    if ltree is not None:
        # For non-symmetric traces we have some special checks
        # to do on trees which couldn't be reached from the
        # other dependency trees. Note these are only performed
        # on the left tree; see TraceForest._add_backwards_nonsymm_trees
        # for details.
        if symmetric or (not tree.do_nonsymm_reverse and not tree.do_inv_transform):
            qx2_q = transform_q(tree.left_abcd_x, qx1_q, tree.nr, ltree.nr)
            qy2_q = transform_q(tree.left_abcd_y, qy1_q, tree.nr, ltree.nr)
        elif tree.do_inv_transform:
            # Can't reach tree directly but there is a coupling from ltree.node
            # to tree.node so apply the inverse abcd law to get correct q
            qx2_q = inv_transform_q(tree.left_abcd_x, qx1_q, tree.nr, ltree.nr)
            qy2_q = inv_transform_q(tree.left_abcd_y, qy1_q, tree.nr, ltree.nr)
        else:
            # Really is no way to get to the node (no coupling from ltree.node to
            # tree.node) so only option now is to reverse q for ltree node entry
            qx2_q = -conj(qx1_q)
            qy2_q = -conj(qy1_q)

        qx2 = BeamParam(q=qx2_q, wavelength=lambda0, nr=ltree.nr)
        qy2 = BeamParam(q=qy2_q, wavelength=lambda0, nr=ltree.nr)

        trace[left_node] = qx2, qy2
        if symmetric:
            trace[left_node.opposite] = qx2.reverse(), qy2.reverse()

        propagate(ltree, trace, lambda0, symmetric)

    if rtree is not None:
        qx2_q = transform_q(tree.right_abcd_x, qx1_q, tree.nr, rtree.nr)
        qy2_q = transform_q(tree.right_abcd_y, qy1_q, tree.nr, rtree.nr)

        qx2 = BeamParam(q=qx2_q, wavelength=lambda0, nr=rtree.nr)
        qy2 = BeamParam(q=qy2_q, wavelength=lambda0, nr=rtree.nr)

        trace[right_node] = qx2, qy2
        if symmetric:
            trace[right_node.opposite] = qx2.reverse(), qy2.reverse()

        propagate(rtree, trace, lambda0, symmetric)


cdef bint is_surface_refl(comp, parent_node, sub_node):
    # TODO (sjr) Want to move these imports to module level but we are
    #            losing the war against circular dependencies right now
    from finesse.components.general import InteractionType
    from finesse.components.surface import Surface

    return (
        isinstance(comp, Surface) and
        comp.interaction_type(parent_node, sub_node) == InteractionType.REFLECTION
    )
