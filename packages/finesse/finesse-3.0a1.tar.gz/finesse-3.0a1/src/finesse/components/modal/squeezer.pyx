from finesse.cmatrix cimport SubCCSView, SubCCSView2DArray
from finesse.cymath cimport complex_t
from finesse.cymath.complex cimport cexp, crotate, conj
from finesse.cymath.math cimport radians, cosh, sinh
from finesse.simulations.base cimport frequency_info_t, NodeBeamParam
from finesse.simulations.basematrix cimport MatrixSystemSolver, CarrierSignalMatrixSimulation
import numpy as np
cimport numpy as np
cimport cython

ctypedef (double*, double*, double*) ptr_tuple_3

cdef extern from "constants.h":
    long double PI
    double C_LIGHT
    double DEG2RAD
    double DB2R

cdef class SqueezerConnections:
    def __cinit__(self):
        pass

cdef class SqueezerNoiseSources:
    def __cinit__(self, MatrixSystemSolver mtx):
        cdef:
            int Nfo =  mtx.optical_frequencies.size

        self.P1o = SubCCSView2DArray(Nfo, Nfo)
        self.ptrs.P1o = <PyObject***>self.P1o.views

cdef class SqueezerValues(BaseCValues):
    def __init__(self):
        cdef ptr_tuple_3 ptr = (&self.db, &self.angle, &self.f)
        cdef tuple params = ("db","angle","f")
        self.setup(params, sizeof(ptr), <double**>&ptr)

cdef class SqueezerWorkspace(ConnectorWorkspace):
    def __init__(self, object owner, CarrierSignalMatrixSimulation sim, bint refill):
        super().__init__(
            owner,
            sim,
            refill,
            refill,
            values=SqueezerValues(),
            noise_sources=SqueezerNoiseSources(sim.signal) if sim.signal else None
        )
        self.v = self.values
        self.ns = self.signal.noise_sources if sim.signal else None
        self.qn_coeffs = np.zeros((sim.model_data.num_HOMs, sim.model_data.num_HOMs), dtype=np.complex128)
        self.qn_coeffs_diag = np.zeros(sim.model_data.num_HOMs, dtype=np.complex128)


squeezer_fill_qnoise = FillFuncWrapper.make_from_ptr(c_squeezer_fill_qnoise)
cdef object c_squeezer_fill_qnoise(ConnectorWorkspace cws):
    r"""
    Fills the quantum noise right hand side (RHS) vector corresponding
    to the squeezed-light source `squeezer`.
    """
    cdef:
        SqueezerWorkspace ws = cws

        # Laser quantum noise injection
        complex_t n = ws.sim.model_data.UNIT_VACUUM / 2
        complex_t phs = crotate(1, 2 * radians(ws.v.angle))
        double r = ws.v.db * DB2R
        complex_t qn
        squeezer_noise_sources noises = ws.ns.ptrs
        frequency_info_t *ifreq
        frequency_info_t *ofreq

        Py_ssize_t i

    # TODO: Shouldn't this quantum noise be frequency-dependent, as for other noise sources?
    ws.qn_coeffs_diag[:] = n

    for i in range(ws.sim.signal.optical_frequencies.size):
        ifreq = &(ws.sim.signal.optical_frequencies.frequency_info[i])
        if ifreq.audio_carrier_index != ws.fsrc_car_idx:
            (<SubCCSView>noises.P1o[ifreq.index][ifreq.index]).fill_za(n)
            continue
        for j in range(ws.sim.signal.optical_frequencies.size):
            ofreq = &(ws.sim.signal.optical_frequencies.frequency_info[j])
            if ofreq.audio_carrier_index != ws.fsrc_car_idx:
                continue
            # Reflections

            if ws.sim.signal.optical_frequencies.frequency_info[i].audio_order > 0:
                if i == j:
                    qn = n * cosh(2 * r)
                else:
                    qn = n * sinh(2 * r) * phs
            else:
                if i == j:
                    qn = conj(n * cosh(2 * r))
                else:
                    qn = conj(n * sinh(2 * r) * phs)

            # We only want to squeeze the main mode of the interferometer, so just set the first
            # element of the relevant matrix/diagonal
            if i == j:
                ws.qn_coeffs_diag[0] = qn
                (<SubCCSView>noises.P1o[ifreq.index][ofreq.index]).fill_zd(ws.qn_coeffs_diag)
            else:
                ws.qn_coeffs[0][0] = qn
                (<SubCCSView>noises.P1o[ifreq.index][ofreq.index]).fill_zm(ws.qn_coeffs)


squeezer_fill_rhs = FillFuncWrapper.make_from_ptr(c_squeezer_fill_rhs)
cdef object c_squeezer_fill_rhs(ConnectorWorkspace cws):
    cdef:
        SqueezerWorkspace ws = <SqueezerWorkspace>cws

    if not ws.sim.is_modal:
        ws.sim.set_source_fast(
            ws.node_id, ws.fsrc_car_idx, 0, 0,
        )
    else:
        for i in range(ws.signal.nhoms):
            ws.sim.set_source_fast(
                ws.node_id, ws.fsrc_car_idx, i, 0,
            )
