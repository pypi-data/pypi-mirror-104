from finesse.cymath cimport complex_t
from finesse.cymath.complex cimport cexp, crotate
from finesse.cymath.math cimport sqrt, radians
from finesse.cymath.gaussbeam cimport bp_gouy
from finesse.cmatrix cimport SubCCSView, SubCCSView1DArray
from finesse.knm cimport KnmMatrix
from finesse.simulations.base cimport NodeBeamParam
from finesse.frequency cimport frequency_info_t
from finesse.cymath.math cimport sgn
from finesse.simulations.basematrix cimport MatrixSystemSolver, CarrierSignalMatrixSimulation

import numpy as np
cimport numpy as np
cimport cython

from cpython.ref cimport PyObject, Py_XINCREF, Py_XDECREF
from libc.string cimport strcmp, memcpy
from libc.stdlib cimport free, calloc

ctypedef (double*, double*, double*) ptr_tuple_3

cdef extern from "constants.h":
    long double PI
    double C_LIGHT
    double DEG2RAD

cdef class LaserConnections:
    def __cinit__(self, MatrixSystemSolver mtx):
        cdef:
            int Nfo =  mtx.optical_frequencies.size

        # There are no carrier connections at a laser, just signals
        self.SIGAMP_P1o = SubCCSView2DArray(1, Nfo)
        self.SIGFRQ_P1o = SubCCSView2DArray(1, Nfo)
        self.SIGPHS_P1o = SubCCSView2DArray(1, Nfo)

        self.ptrs.SIGAMP_P1o = <PyObject***>self.SIGAMP_P1o.views
        self.ptrs.SIGFRQ_P1o = <PyObject***>self.SIGFRQ_P1o.views
        self.ptrs.SIGPHS_P1o = <PyObject***>self.SIGPHS_P1o.views

cdef class LaserValues(BaseCValues):
    def __init__(self):
        cdef ptr_tuple_3 ptr = (&self.P, &self.phase, &self.f)
        cdef tuple params = ("P", "phase", "f")
        self.setup(params, sizeof(ptr), <double**>&ptr)


cdef class LaserWorkspace(ConnectorWorkspace):
    def __init__(self, object owner, CarrierSignalMatrixSimulation sim, bint refill):
        super().__init__(
                owner,
                sim,
                refill,
                refill,
                None,
                LaserConnections(sim.signal) if sim.signal else None,
                LaserValues()
                )
        self.v = self.values
        self.lc = self.signal.connections if sim.signal else None
        self.PIj_2 = PI*0.5j

        # indexes for beam tracing
        self.P1o_id = sim.carrier.node_id(owner.p1.o)


laser_carrier_fill_rhs = FillFuncWrapper.make_from_ptr(c_laser_carrier_fill_rhs)
cdef object c_laser_carrier_fill_rhs(ConnectorWorkspace cws):
    r"""
    Fills the right hand side (RHS) vector corresponding to the light source `laser`.

    The field amplitude is set as

    .. math::
        a_{\mathrm{in}} = \sqrt{\frac{2P}{\epsilon_c}}~\exp{\left(i \varphi\right)},

    where :math:`P` is the laser power and :math:`\varphi` is the specified phase of
    the laser.

    Parameters
    ----------

    laser : :class:`.Laser`
        The laser object to fill.

    sim : :class:`.CarrierSignalMatrixSimulation`
        A handle to the simulation.

    values : dict
        Dictionary of evaluated model parameters.

    fsrc_index : int
        Index of source frequency bin.
    """
    cdef:
        LaserWorkspace ws = <LaserWorkspace>cws

        # Carrier laser injection
        complex_t Ein = sqrt(2 * ws.v.P / ws.sim.model_data.EPSILON0_C) * cexp(1.0j * radians(ws.v.phase))

        Py_ssize_t i

    if not ws.sim.is_modal:
        ws.sim.carrier.set_source_fast(
            ws.node_car_id, ws.fsrc_car_idx, 0, Ein,
        )
    else:
        for i in range(ws.sim.model_data.num_HOMs):
            ws.sim.carrier.set_source_fast(
                ws.node_car_id, ws.fsrc_car_idx, i, Ein * ws.power_coeffs[i],
            )


laser_fill_qnoise = FillFuncWrapper.make_from_ptr(c_laser_fill_qnoise)
cdef object c_laser_fill_qnoise(ConnectorWorkspace cws):
    r"""
    Fills the quantum noise input matrix corresponding to the light source `laser`.
    """
    cdef:
        LaserWorkspace ws = <LaserWorkspace>cws
        PyObject ***noises = ws.output_noise.ptrs
        frequency_info_t *freq

        # Laser quantum noise injection
        complex_t qn

    for i in range(ws.sim.signal.optical_frequencies.size):
        freq = &(ws.sim.signal.optical_frequencies.frequency_info[i])
        qn = ws.sim.model_data.UNIT_VACUUM / 2 * (1 + freq.f_car[0] / ws.sim.model_data.f0)
        (<SubCCSView>noises[0][freq.index]).fill_za(qn)


laser_fill_signal = FillFuncWrapper.make_from_ptr(c_laser_fill_signal)
cdef object c_laser_fill_signal(ConnectorWorkspace cws):
    cdef:
        LaserWorkspace ws = <LaserWorkspace>cws
        laser_connections conns = <laser_connections>ws.lc.ptrs
        Py_ssize_t i, j
        double factor = ws.sim.model_data.EPSILON0_C

        complex_t phs_sig
        complex_t frq_sig

        frequency_info_t *f
        complex_t* car

    for i in range(2):
        f = &ws.sim.signal.optical_frequencies.frequency_info[ws.fcar_sig_sb_idx[i]]
        # NOTE shouldn't need multiplication by corresponding power_coeff
        #      factor as this was taken into account in DC computations
        # Update this so that frequency rhs idx is store in workspace
        j = ws.sim.carrier.field_fast(ws.node_car_id, f.audio_carrier_index, 0)
        car = <complex_t*>&(ws.sim.carrier.out_view[j])
        # TODO ddb - these are all assuming a single electronic frequency here
        if conns.SIGAMP_P1o[0][f.index]:
            (<SubCCSView>conns.SIGAMP_P1o[0][f.index]).fill_negative_za_zm_2(factor * 0.5 * 0.5, car, 1, 1)

        if conns.SIGFRQ_P1o[0][f.index]:
            frq_sig =  0.5 / ws.sim.model_data.fsig * sgn(f.audio_order)
            (<SubCCSView>conns.SIGFRQ_P1o[0][f.index]).fill_negative_za_zm_2(factor * frq_sig, car, 1, 1)

        if conns.SIGPHS_P1o[0][f.index]:
            phs_sig = 1j * 0.5
            (<SubCCSView>conns.SIGPHS_P1o[0][f.index]).fill_negative_za_zm_2(factor * phs_sig, car, 1, 1)


laser_set_gouy = GouyFuncWrapper.make_from_ptr(set_tem_gouy_phases)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cdef int set_tem_gouy_phases(ConnectorWorkspace ws) except -1:
    cdef:
        const NodeBeamParam* q_p1o = &ws.sim.trace[ws.P1o_id]

        double gouy_x
        double gouy_y
        double phase00 = 0.0
        double phase

        Py_ssize_t i
        int n, m

    if not q_p1o.is_changing:
        return 0

    gouy_x = bp_gouy(&q_p1o.qx)
    gouy_y = bp_gouy(&q_p1o.qy)

    if ws.sim.model_data.zero_tem00_gouy:
        phase00 = 0.5 * gouy_x + 0.5 * gouy_y

    for i in range(ws.sim.model_data.num_HOMs):
        n = ws.sim.model_data.homs_view[i][0]
        m = ws.sim.model_data.homs_view[i][1]

        phase = (n + 0.5) * gouy_x + (m + 0.5) * gouy_y
        ws.power_coeffs[i] = crotate(ws.power_coeffs[i], phase - phase00)

    return 0
