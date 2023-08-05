cimport numpy as np
from finesse.cymath cimport complex_t
from finesse.cymath.gaussbeam cimport beam_param
from finesse.tracing.ctracer cimport TraceForest, TraceTree
from finesse.frequency cimport frequency_info_t, FrequencyContainer
from cpython.ref cimport PyObject


cdef struct NodeInfoEntry:
    Py_ssize_t index
    Py_ssize_t rhs_index
    Py_ssize_t freq_index
    Py_ssize_t nfreqs # number of frequencies
    Py_ssize_t nhoms # number of HOMs
    frequency_info_t *frequencies # Frequencies present at this node, size nfreqs


cdef struct NodeBeamParam:
    beam_param qx
    beam_param qy
    bint is_changing


cdef class ModelData:
    cdef public:
        double fsig
    cdef readonly:
        double EPSILON0_C, UNIT_VACUUM, lambda0
        double f0, k0
        int num_HOMs
        int[:, ::1] homs_view
        int maxtem
        int max_n # Maximum mode index in tangential plane
        int max_m # Maximum mode index in sagittal plane
        double x_scale
        bint zero_K00 # should phase of k0000 coefficients be zeroed
        bint zero_tem00_gouy # should Gouy phase of TEM00 be zeroed
        bint v2_transmission_phase
    cdef:
        # Flat contiguous ptr to homs_view
        int* homs_ptr


# Contains non-physical configuration data, as low-level values, to be
# used during a simulation
cdef struct SimConfigData:
    # Number of threads to use for prange loops whose
    # size is proportional to the number of modes
    int nthreads_homs
