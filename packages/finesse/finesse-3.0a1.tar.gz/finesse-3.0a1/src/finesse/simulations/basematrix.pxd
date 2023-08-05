from finesse.cmatrix cimport CCSMatrix
from finesse.cymath cimport complex_t
from finesse.tracing.ctracer cimport TraceForest, TraceTree
from finesse.simulations.base cimport ModelData, NodeBeamParam, NodeInfoEntry, SimConfigData
from finesse.frequency cimport frequency_info_t, FrequencyContainer, Frequency
from cpython.ref cimport PyObject
from finesse.components.workspace cimport ConnectorWorkspace


cdef extern from "constants.h":
    long double PI
    double C_LIGHT
    double complex COMPLEX_0


cdef class MatrixSystemWorkspaces:
    cdef readonly:
        list to_initial_fill
        list to_refill
        list to_rhs_refill
        list to_noise_refill
        list to_noise_input_refill
        list noise_detectors
        int num_to_refill
        int num_to_rhs_refill
        int num_to_noise_refill
        int num_to_noise_input_refill
        int num_noise_detectors
    cdef:
        PyObject** ptr_to_refill
        PyObject** ptr_to_rhs_refill
        PyObject** ptr_to_noise_refill
        PyObject** ptr_to_noise_input_refill
        PyObject** ptr_noise_detectors


cdef class MatrixSystemSolver:
    cdef:
        CCSMatrix _M
        readonly dict _noise_matrices
        readonly dict _submatrices
        readonly dict _noise_submatrices
        Py_ssize_t num_nodes
        readonly dict nodes
        readonly dict nodes_idx
        NodeInfoEntry* _c_node_info
        readonly FrequencyContainer optical_frequencies
        readonly dict mechanical_frequencies
        readonly dict electrical_frequencies
        readonly tuple unique_elec_mech_fcnts # Unique frequency containers for mech/elec
        readonly dict noise_sources
        readonly int nhoms
        readonly complex_t[::1] out_view
        readonly bint any_frequencies_changing
        bint is_signal_matrix
        readonly bint forced_refill
        public bint manual_rhs
        readonly MatrixSystemWorkspaces workspaces

    cpdef setup_nodes(self, list nodes)
    cpdef clear_rhs(self)
    cdef initial_fill(self)
    cdef refill(self)
    cdef fill_rhs(self)
    cdef fill_noise_inputs(self)
    cdef refactor(self)
    cdef factor(self)
    cdef solve(self)
    cdef solve_noises(self)
    cdef construct(self)
    cdef initial_run(self)
    cpdef run(self)

    cdef get_node_matrix_params(self, node, Py_ssize_t *Ns, Py_ssize_t *Nf, frequency_info_t** fptr)
    cdef tuple get_node_frequencies(self, node)

    cdef update_frequency_info(self)
    cdef assign_submatrices(self, workspaces)
    cdef assign_noise_submatrices(self, workspaces)

    cdef add_noise_matrix(self, object key)
    cdef add_rhs(self, unicode key)

    cpdef Py_ssize_t findex(self, object node, Py_ssize_t freq)
    cdef Py_ssize_t findex_fast(self, Py_ssize_t node_id, Py_ssize_t freq) nogil

    cpdef Py_ssize_t field(self, object node, Py_ssize_t freq=?, Py_ssize_t hom=?)
    cdef Py_ssize_t field_fast(self, Py_ssize_t node_id, Py_ssize_t freq=?, Py_ssize_t hom=?) nogil
    cdef inline Py_ssize_t field_fast_2(
        self,
        Py_ssize_t node_rhs_idx,
        Py_ssize_t num_hom,
        Py_ssize_t freq,
        Py_ssize_t hom
    ) nogil

    cpdef complex_t get_out(self, object node, Py_ssize_t freq=?, Py_ssize_t hom=?)
    cdef complex_t get_out_fast(self, Py_ssize_t node_id, Py_ssize_t freq=?, Py_ssize_t hom=?) nogil

    cdef void set_source_fast(self, Py_ssize_t node_id, Py_ssize_t freq_idx, Py_ssize_t hom_idx, complex_t value, unsigned rhs_index=?)
    cdef void set_source_fast_2(self, Py_ssize_t rhs_idx, complex_t value)
    cdef void set_source_fast_3(self, Py_ssize_t rhs_idx, complex_t value, unsigned rhs_index)

    cpdef Py_ssize_t node_id(self, object node)
    cpdef get_node_info(self, name)



cdef class CarrierSignalMatrixSimulation:
    cdef:
        readonly MatrixSystemSolver carrier
        readonly MatrixSystemSolver signal
        readonly bint compute_signals

        readonly unicode name
        readonly set changing_parameters
        readonly set tunable_parameters
        readonly object model
        readonly bint is_modal
        readonly bint do_matrix_solving

        readonly MatrixSystemWorkspaces carrier_ws
        readonly MatrixSystemWorkspaces signal_ws
        readonly list detector_workspaces
        readonly list readout_workspaces

        public list workspaces
        public list variable_workspaces
        readonly list gouy_phase_workspaces

        ### Tracing stuff ###
        public dict cavity_workspaces
        NodeBeamParam* trace
        # The TraceForest of geometrically changing branches. This is an
        # empty forest for any simulation in which geometric parameters
        # are not changing.
        readonly TraceForest trace_forest
        # Node couplings which will have potential mode mismatches,
        # determined from trace_forest via tree intersection searching
        readonly tuple mismatched_node_couplings
        # A dict of {<tuple of newly unstable cavities> : <contingent TraceForest>}
        # required for when a scan results in a geometrically changing cavity becoming
        # unstable -> invalidating self.trace_forest temporarily for that data point
        dict contingent_trace_forests
        bint needs_reflag_changing_q # Used when exiting from unstable cavity regions
        bint retrace

        # List of workspaces for components which scatter modes
        list to_scatter_matrix_compute
        readonly ModelData model_data
        object __weakref__

        SimConfigData config_data

    cdef initialise_model_data(self)
    cdef initialise_sim_config_data(self)

    cpdef initialise_workspaces(self)
    cpdef initialise_noise_matrices(self)
    cpdef initialise_noise_sources(self)
    cpdef initialise_noise_selection_vectors(self)
    cdef initialise_trace_forest(self, optical_nodes)
    cdef void update_all_parameter_values(self)

    cdef void update_cavities(self)
    cdef void compute_knm_matrices(self)
    cdef int set_gouy_phases(self) except -1
    cpdef int modal_update(self) except -1

    cpdef run_carrier(self)
    cpdef run_signal(self)

    # Methods to construct the changing TraceForest for the simulation
    cdef void _determine_changing_beam_params(self, TraceForest forest=?, bint set_tree_node_ids=?)
    cdef void _setup_trace_forest(self, TraceForest forest=?, bint set_tree_node_ids=?)
    cdef void _setup_single_trace_tree(self, TraceTree tree, bint set_tree_node_ids=?)

    # Find the newly unstable cavity instances from the changing forest
    cdef tuple _find_new_unstable_cavities(self)
    cdef TraceForest _initialise_contingent_forest(self, tuple unstable_cavities)

    # Perform the beam trace on the changing TraceForest
    cdef void _propagate_trace(self, TraceTree tree, bint symmetric)
    cdef bint trace_beam(self)
