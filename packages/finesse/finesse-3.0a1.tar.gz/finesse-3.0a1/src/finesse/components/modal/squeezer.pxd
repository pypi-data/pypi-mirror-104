from finesse.cmatrix cimport SubCCSView, SubCCSView2DArray
from finesse.cymath.complex cimport complex_t
from finesse.components.workspace cimport ConnectorWorkspace, FillFuncWrapper
from finesse.element cimport BaseCValues

import numpy as np
cimport numpy as np
from cpython.ref cimport PyObject

cdef struct squeezer_noise_sources:
    # 2D array of SubCCSViews
    PyObject*** P1o

cdef class SqueezerConnections:
    cdef public:
        int P1o_idx
    cdef readonly:
        SubCCSView2DArray P1o

cdef class SqueezerNoiseSources:
    cdef readonly:
        SubCCSView2DArray P1o
    cdef:
        squeezer_noise_sources ptrs

cdef class SqueezerValues(BaseCValues):
    cdef public:
        double db
        double angle
        double f


cdef class SqueezerWorkspace(ConnectorWorkspace):
    cdef public:
        Py_ssize_t fsrc_car_idx
        Py_ssize_t node_id
        SqueezerValues v
        SqueezerNoiseSources ns
        complex_t[:, ::1] qn_coeffs
        complex_t[::1] qn_coeffs_diag


cdef object c_squeezer_fill_rhs(ConnectorWorkspace cws)
