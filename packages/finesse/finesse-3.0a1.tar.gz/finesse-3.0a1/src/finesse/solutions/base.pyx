"""Base solution interface.

Solution classes contain the output from a Finesse simulation, and convenience methods for
accessing, plotting and serialising that output.

Solutions intentionally do not contain references to the model that produced its results. This is so
that the solution can be serialised without requiring the model that produced it itself be
serialisable.
"""
from collections.abc import Iterable
from functools import reduce
from finesse.tree cimport TreeNode
from finesse.solutions.array import ArraySolutionSet
from finesse.solutions.array import ArraySolution

cdef class ParameterChangingTreeNode(TreeNode):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.parameters_changing = ()

    def get_all_parameters_changing(self):
        return reduce(
            lambda a, b: (*a, *b.parameters_changing),
            self.get_all_children(),
            (*self.parameters_changing,),
        )


cdef class BaseSolution(ParameterChangingTreeNode):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)

    def __str__(self):
        def fn_name(child):
            if type(child) is not BaseSolution:
                r = f" - {child.__class__.__name__}"
            else:
                r = ""
            return child.name + r

        # Override default show_max_children to 3 so large nested solutions do not print huge trees.
        return self.draw_tree(fn_name, title="Solution Tree", show_max_children=3)

    def __getitem__(self, key):
        if isinstance(key, (slice, int)):
            return self.children[key]
        elif isinstance(key, str) or not isinstance(key, Iterable):
            rtn = tuple(child for child in self.children if child.name == str(key))
            if len(rtn) == 1:
                return rtn[0]
            else:
                # return specific set for certain solutions
                if isinstance(rtn[0], ArraySolution):
                    return ArraySolutionSet(rtn)
                else:
                    return rtn
        else:  # We're an iterable that isn't a string
            if len(key) == 1:
                return self[key[0]]
            elif isinstance(key[0], slice):
                raise NotImplementedError(
                    "Solution indexing only supports slices at the end of a key"
                )
            else:
                return self[key[0]][key[1:]]

    def __repr__(self):
        return f"<{self.__class__.__name__} of {self.get_path()} @ {hex(id(self))} children={len(self.children)}>"
