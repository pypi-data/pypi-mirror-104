cimport numpy as np
from finesse.cymath.complex cimport complex_t, DenseZMatrix


cdef class KnmMatrix:
    cdef readonly:
        np.ndarray data
        str name

    cdef:
        complex_t[:, ::1] data_view
        DenseZMatrix mtx
        const int[:, ::1] modes_view

    cdef (Py_ssize_t, Py_ssize_t) field_indices_from(self, key)
    cdef complex_t coupling(self, int n1, int m1, int n2, int m2) nogil


cpdef make_unscaled_X_scatter_knm_matrix(int[:,::1] modes)
cpdef make_unscaled_Y_scatter_knm_matrix(int[:,::1] modes)


# Compute loss from scattering for each coupling,
# required for  quantum noise calculations
cdef void knm_loss(const complex_t* knm_mat, double* out, Py_ssize_t N) nogil
