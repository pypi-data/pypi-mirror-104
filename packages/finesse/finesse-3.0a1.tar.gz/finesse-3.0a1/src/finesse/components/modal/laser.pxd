from finesse.cmatrix cimport SubCCSView, SubCCSView2DArray
from finesse.knm cimport KnmMatrix
from finesse.cymath cimport complex_t
from finesse.cymath.complex cimport conj, cexp
from finesse.simulations.base cimport ModelData
from finesse.frequency cimport frequency_info_t
from finesse.simulations.basematrix cimport CarrierSignalMatrixSimulation
from finesse.components.workspace cimport ConnectorWorkspace, FillFuncWrapper, GouyFuncWrapper
from finesse.element cimport BaseCValues

import numpy as np
cimport numpy as np
from cpython.ref cimport PyObject

cdef struct laser_connections:
    # 1D array of SubCCSViews
    PyObject*** SIGAMP_P1o
    PyObject*** SIGFRQ_P1o
    PyObject*** SIGPHS_P1o

cdef class LaserConnections:
    cdef public:
        int SIGAMP_P1o_idx
        int SIGFRQ_P1o_idx
        int SIGPHS_P1o_idx

    cdef readonly:
        SubCCSView2DArray SIGAMP_P1o
        SubCCSView2DArray SIGFRQ_P1o
        SubCCSView2DArray SIGPHS_P1o
    cdef:
        laser_connections ptrs

cdef class LaserValues(BaseCValues):
    cdef public:
        double P
        double phase
        double f


cdef class LaserWorkspace(ConnectorWorkspace):
    cdef public:
        Py_ssize_t fsrc_car_idx
        Py_ssize_t fcar_sig_sb_idx[2]
        complex_t[::1] power_coeffs # length sim.model_data.num_HOMs
        Py_ssize_t node_car_id, node_sig_id
        LaserValues v
        LaserConnections lc
        complex_t PIj_2
        Py_ssize_t P1o_id


cdef object c_laser_carrier_fill_rhs(ConnectorWorkspace cws)
