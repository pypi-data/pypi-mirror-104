
cdef class TraceForest:
    cdef public:
        bint symmetric # Should beam traces on this forest set opposite node q to -q*?

    cdef readonly:
        list forest
        Py_ssize_t N_trees

        list dependencies # the Cavities and Gausses in order of tracing priority

        object model

    cdef:
        list node_coverage
        list internal_cavity_nodes

    cpdef void clear(self)

    cdef int _add_internal_cavity_trees(self, list cavities) except -1
    cdef int _handle_overlapping_cavities(self) except -1
    cdef int _add_external_cavity_tree(self, object cav) except -1
    cdef int _add_gauss_tree(self, object gauss) except -1

    cdef int _add_beamsplitter_branch_trees(self) except -1
    cdef int _add_backwards_nonsymm_trees(self) except -1

    cpdef set find_untraversed_nodes(self)

    cpdef TraceTree find_tree_from_node(self, object node)
    cpdef object find_dependency_from_node(self, object node, bint raise_not_found=?)
    cpdef set gather_nodes(self)

    cdef object node_from_name(self, name)

    cdef TraceForest make_changing_forest(self)

    cpdef bint contains_space(self, object space)
    cpdef bint contains_comp(self, object comp)

    cpdef tuple find_potential_mismatch_couplings(self, TraceForest other=?)
    cpdef tuple find_intersection_couplings(self, TraceForest other=?)
    cpdef tuple get_mirror_reflection_couplings(
        self,
        bint ignore_internal_cavities=?,
        list skip_dependencies=?,
    )

    cdef void trim(self)

    cpdef draw_by_dependency(self)
    cpdef draw(self)


cdef class TraceTree:
    cdef readonly:
        TraceTree parent
        TraceTree left
        TraceTree right

        # Either a Cavity or a Gauss
        object dependency
        object node

        bint is_x_changing
        bint is_y_changing

        # Is this tree an internal cavity representation or directly
        # froma Gauss command node?
        bint is_source

        # Numeric views on the component ABCD matrices - the initial
        # numeric ABCD memory for each component is only ever modified,
        # never re-allocated, so these views will always be valid
        double[:, ::1] left_abcd_x
        double[:, ::1] left_abcd_y
        double[:, ::1] right_abcd_x
        double[:, ::1] right_abcd_y
        # Is the left tree a reflection from a surface? Important for
        # computing composite / round-trip ABCDs so co-ordinate transformation
        # in x plane can be taken into account
        bint is_left_surf_refl

        # Symbolic ABCD views - only to be used for utility beam tracing code
        # such as computing a composite ABCD matrix over a path
        object[:, ::1] sym_left_abcd_x
        object[:, ::1] sym_left_abcd_y
        object[:, ::1] sym_right_abcd_x
        object[:, ::1] sym_right_abcd_y

        double nr

    cdef:
        # Indices of the node (and opposite for symmetric tracing) to be
        # set and used by a BaseSimulation
        Py_ssize_t node_id
        Py_ssize_t opp_node_id

        # Only used for non-symmetric traces on trees which couldn't be
        # reached from any other dependency branch. This flag indicates
        # the next (left) tree node is a reverse coupling so need to
        # apply the inverse abcd law transform when tracing.
        bint do_inv_transform

        # Again, only used for non-symmetric traces on trees which couldn't
        # be reached from any other dependency branch AND for which the node
        # doesn't have a reverse coupling; e.g. reverse node at a Laser. This
        # flag indicates that the next tree node needs -q* applied during tracing
        # as there is really no other option for setting it at this point.
        bint do_nonsymm_reverse

    @staticmethod
    cdef TraceTree initialise(
        object node, object dependency, bint* is_dependency_changing=?
    )

    cpdef TraceTree add_left(self, TraceTree sub_tree)
    cpdef TraceTree add_right(self, TraceTree sub_tree)

    cpdef bint remove_left(self)
    cpdef bint remove_right(self)

    cdef void trim_at_nodes(
        self, list nodes, bint include_opposite=?
    )

    cdef TraceTree _propagate_find_tree_at_node(
        self,
        TraceTree tree,
        object node,
        bint include_opposite,
    )
    cpdef TraceTree find_tree_at_node(self, object node, bint include_opposite=?)

    cdef _get_last_input_nodes(self, list last_nodes)
    cpdef list get_last_input_nodes(self)

    cpdef bint contains_node(self, object node)
    cpdef bint contains_space(self, object space)
    cpdef bint contains_comp(self, object comp)

    cdef __append_mirror_refl_coupling(self, list couplings)
    cdef _get_mirror_refl_couplings(self, list couplings)
    cpdef list get_mirror_reflection_couplings(self)

    @staticmethod
    cdef bint subtrees_changing(TraceTree sub_tree)
    cpdef bint is_changing(self, bint recursive=?)

    cdef list get_broadest_changing_subtrees(self)
    cpdef draw(self, unicode left_pad=?)

    cpdef trace_beam(self, dict trace, double lambda0, bint symmetric)


cpdef TraceTree get_last_left_branch(TraceTree tree)

cpdef bint is_abcd_changing(object[:, ::1] M)

cpdef void update_rt_abcd(
    TraceTree tree,
    double[:, ::1] ABCDx,
    double[:, ::1] ABCDy
)
