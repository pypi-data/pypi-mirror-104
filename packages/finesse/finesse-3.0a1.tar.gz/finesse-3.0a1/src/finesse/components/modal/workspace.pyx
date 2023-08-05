cimport cython

import numpy as np
cimport numpy as np
import logging

from libc.stdlib cimport free, malloc, calloc

from finesse.knm cimport (
    KnmMatrix,
    knm_bh_workspace,
    knm_bh_ws_init,
    knm_bh_ws_free,
    knm_bh_ws_is_changing,
    knm_bh_ws_recompute_mismatch,
    knm_bh_ws_recompute,
    knm_bh_ws_recompute_misalignment,
)
from finesse.knm.bayerhelms cimport (
    fast_compute_refl_knm_matrix_bh__k00_zeroed,
    fast_compute_trns_knm_matrix_bh__k00_zeroed,
    fast_compute_refl_knm_matrix_bh,
    fast_compute_trns_knm_matrix_bh,
)
from finesse.knm.matrix cimport knm_loss
from finesse.cmatrix cimport SubCCSView
from finesse.components.workspace cimport ConnectorWorkspace, FillFuncWrapper, NoiseInfo
from finesse.components.general import NodeType, NoiseType
from finesse.cymath.gaussbeam cimport c_transform_q
from finesse.frequency cimport frequency_info_t
from finesse.simulations.base cimport NodeBeamParam

import finesse.components as components


LOGGER = logging.getLogger(__name__)

cdef double[:,::1] abcd_unity = np.eye(2, dtype=float)


cdef class KnmConnectorWorkspace(ConnectorWorkspace):
    def __init__(self, object owner, CarrierSignalMatrixSimulation sim, *args, **kwargs):
        ConnectorWorkspace.__init__(self, owner, sim, *args, **kwargs)

        # Here we automatically generate the coupling strings used
        # for generating the Knm matricies. We use the optical to optical
        # connections that have been registered, the port number is taken
        # from the order in which they are added to the component. I guess
        # there could also be a more explicit defition of the port "index"
        # given in the _add_port method but we'll use this for now.

        # TODO ddb could store index in port object perhaps, along with the
        # list of optical ports
        self.o2o = owner.all_optical_connections
        oports = list(p for p in owner.ports if p.type == NodeType.OPTICAL)

        self.N_opt_ports = len(oports)
        self.N_opt_conns = len(self.o2o)

        self.onode_ids = <Py_ssize_t*> malloc(sizeof(Py_ssize_t) * self.N_opt_ports * 2)
        if not self.onode_ids:
            raise MemoryError()

        self.oconn_info = <KnmInfo*> calloc(sizeof(KnmInfo), self.N_opt_conns)
        if not self.oconn_info:
            raise MemoryError()

        # 2 lots per connection because of x and y planes
        self.Kws = <knm_bh_workspace*> calloc(sizeof(knm_bh_workspace), 2*self.N_opt_conns)
        if not self.Kws:
            raise MemoryError()

        # need these node ids for the simulation for indexing traces
        for i, p in enumerate(oports):
            self.onode_ids[2*i] = sim.carrier.node_id(p.i)
            self.onode_ids[2*i+1] = sim.carrier.node_id(p.o)

        cdef np.ndarray[double, ndim=1, mode='c'] scatter_loss
        for i, (conn, (f, t)) in enumerate(self.o2o.items()):
            # TODO ddb should probably use some fixed index rather than a list of the order
            # they are defined in the element definition
            a = oports.index(f.port)
            b = oports.index(t.port)
            coupling = f"{a+1}{b+1}"
            self.oconn_info[i].from_port_idx = a
            self.oconn_info[i].to_port_idx = b
            self.oconn_info[i].K_ws_x = &self.Kws[2*i]
            self.oconn_info[i].K_ws_y = &self.Kws[2*i+1]
            self.oconn_info[i].abcd_x = &abcd_unity[0,0]
            self.oconn_info[i].abcd_y = &abcd_unity[0,0]

            knm = KnmMatrix(self.sim.model_data.homs_view, self.owner.name, coupling)
            self.oconn_info[i].mtx = &knm.mtx
            # Create the actual Knm matrix here based on the optical
            # port coupling indices
            setattr(self, f"K{coupling}", knm)

            # Make the buffer of knm loss data
            scatter_loss = np.zeros(self.sim.model_data.num_HOMs)
            setattr(self, f"K{coupling}_loss", scatter_loss)
            # Keep ptr to the buffer for use in compute_knm_losses
            self.oconn_info[i].loss = &scatter_loss[0]

        self.total_losses = np.zeros(self.sim.model_data.num_HOMs)
        if sim.signal:
            self.signal.set_fill_noise_function(NoiseType.QUANTUM, optical_quantum_noise_knm)

    def __dealloc__(self):
        if self.onode_ids:
            free(self.onode_ids)
        if self.oconn_info:
            free(self.oconn_info)
        if self.Kws:
            free(self.Kws)

    cpdef set_knm_info(self, connection,
        double[:,::1] abcd_x = abcd_unity,
        double[:,::1] abcd_y = abcd_unity,
        double nr_from=1, double nr_to=1,
        bint is_transmission=False,
        Parameter beta_x = None,
        double beta_x_factor = 0,
        Parameter beta_y = None,
        double beta_y_factor = 0,
        Parameter alpha = None
    ):
        """Python facing method to set how Knm calculations should be handled for a
        particular connection. When the workspace is being created this should be called if modal
        simualtions are being used. This then sets which ABCD matricies to use, various parameters
        required, and whether the connection is a transmission or reflection.
        """
        cdef:
            KnmInfo *conn
            int index

        if abcd_x.shape[0] != abcd_x.shape[1] != 2:
            raise Exception("ABCD X is not 2x2")
        if abcd_y.shape[0] != abcd_y.shape[1] != 2:
            raise Exception("ABCD Y is not 2x2")
        # First find the connection str in our connections then store the information)
        if connection not in self.o2o:
            raise Exception(f"Connection {connection} is not a valid connection in the element {self.owner}")

        index = list(self.o2o.keys()).index(connection)
        conn = &self.oconn_info[index]
        conn.has_been_set = True
        conn.abcd_x = &abcd_x[0, 0]
        conn.abcd_y = &abcd_y[0, 0]
        conn.is_transmission = is_transmission
        conn.nr_from = nr_from
        conn.nr_to = nr_to
        if beta_x:
            conn.beta_x = &beta_x.__cvalue
            conn.beta_x_is_changing = beta_x.is_changing if beta_x else False
            conn.beta_x_factor = beta_x_factor
        if beta_y:
            conn.beta_y = &beta_y.__cvalue
            conn.beta_y_is_changing = beta_y.is_changing if beta_y else False
            conn.beta_y_factor = beta_y_factor
        if alpha:
            conn.alpha = &alpha.__cvalue
            conn.alpha_is_changing = alpha.is_changing
            if alpha.is_changing:
                raise NotImplementedError("Changing angle of incidence not supported yet")

        # Set the appropriate scatter matrix function to use based on
        # whether this is a transmission or reflection coupling, and
        # also whether the 00->00 coupling coefficient should have
        # zeroed phase (i.e. zero_K00 config flag)
        if conn.is_transmission:
            if self.sim.model_data.zero_K00:
                conn.bhelms_mtx_func = fast_compute_trns_knm_matrix_bh__k00_zeroed
            else:
                conn.bhelms_mtx_func = fast_compute_trns_knm_matrix_bh
        else:
            if self.sim.model_data.zero_K00:
                conn.bhelms_mtx_func = fast_compute_refl_knm_matrix_bh__k00_zeroed
            else:
                conn.bhelms_mtx_func = fast_compute_refl_knm_matrix_bh

    cdef initialise_knm_workspaces(KnmConnectorWorkspace self):
        cdef:
            NodeBeamParam *q_from
            NodeBeamParam *q_to
            KnmInfo *info
            # From Beam parameters transformed by ABCD
            complex_t qx_from_trns, qy_from_trns

            double lambda0 = self.sim.model_data.lambda0
            int maxtem = self.sim.model_data.maxtem
            int i = 0
            double beta_x, beta_y

        oconn_names = tuple(self.o2o.keys())
        # Loop over the node ids stored in input, output pairs and get the
        # beam param data
        for i in range(self.N_opt_conns):
            info = &self.oconn_info[i]
            if not info.has_been_set:
                raise Exception(f"Information for connection {oconn_names[i]} at {self.owner.name} has not been set with `set_knm_info`")

            if info.abcd_x == NULL:
                raise Exception(f"Knm info ABCDx for connection {oconn_names[i]} at {self.owner.name} is NULL")
            if info.abcd_y == NULL:
                raise Exception(f"Knm info ABCDy for connection {oconn_names[i]} at {self.owner.name} is NULL")
            if info.beta_x == NULL and info.beta_x_factor != 0:
                raise Exception(f"Knm info beta_x for connection {oconn_names[i]} at {self.owner.name} is NULL but has a beta_x_factor set")
            if info.beta_y == NULL and info.beta_y_factor != 0:
                raise Exception(f"Knm info beta_y for connection {oconn_names[i]} at {self.owner.name} is NULL but has a beta_y_factor set")

            ni_idx = self.onode_ids[2*info.from_port_idx]
            no_idx = self.onode_ids[2*info.to_port_idx+1]
            q_from = &self.sim.trace[ni_idx]
            q_to = &self.sim.trace[no_idx]
            # 'From' Beam parameters after propagation through the connections ABCD
            qx_from_trns = c_transform_q(info.abcd_x, q_from.qx.q, info.nr_from, info.nr_to)
            qy_from_trns = c_transform_q(info.abcd_y, q_from.qy.q, info.nr_from, info.nr_to)
            # Get any misalignment factor is one has been set
            beta_x = info.beta_x[0] if info.beta_x else 0
            beta_y = info.beta_y[0] if info.beta_y else 0
            # Initialise the Knm workspaces with the current values
            knm_bh_ws_init(
                info.K_ws_x, qx_from_trns, q_to.qx.q, beta_x, info.beta_x_factor, info.nr_to, lambda0, maxtem
            )
            knm_bh_ws_init(
                info.K_ws_y, qy_from_trns, q_to.qy.q, beta_y, info.beta_y_factor, info.nr_to, lambda0, maxtem,
            )

    cdef void free_knm_workspaces(KnmConnectorWorkspace self) nogil:
        cdef:
            int i
            knm_bh_workspace *kws = NULL

        for i in range(2*self.N_opt_conns):
            knm_bh_ws_free(&self.Kws[i])

    cdef void flag_changing_knm_workspaces(KnmConnectorWorkspace self):
        cdef:
            KnmInfo *info
            bint is_mm_changing
            Py_ssize_t ni_idx, no_idx
            const NodeBeamParam* q_from
            const NodeBeamParam* q_to

        for i in range(self.N_opt_conns):
            info = &self.oconn_info[i]
            ni_idx = self.onode_ids[2*info.from_port_idx]
            no_idx = self.onode_ids[2*info.to_port_idx+1]
            q_from = &self.sim.trace[ni_idx]
            q_to = &self.sim.trace[no_idx]

            # Mode mismatch is only changing if this node coupling is
            # in the pre-determined mismatched_node_couplings of the sim
            is_mm_changing = (
                list(self.o2o.values())[i] in self.sim.mismatched_node_couplings
                # Or if the component is misaligned and we have changing beam parameters
                # at this coupling then also need to recompute scatter matrix
                or (
                    (not info.K_ws_x.aligned or not info.K_ws_y.aligned)
                    and (q_from.is_changing or q_to.is_changing)
                )
            )
            info.K_ws_x.is_mm_changing = is_mm_changing
            info.K_ws_y.is_mm_changing = is_mm_changing
            info.K_ws_x.is_alignment_changing = info.beta_x_is_changing
            info.K_ws_y.is_alignment_changing = info.beta_y_is_changing

            if knm_bh_ws_is_changing(info.K_ws_x) or knm_bh_ws_is_changing(info.K_ws_y):
                LOGGER.debug(f"{self.owner.name}.K{info.from_port_idx+1}{info.to_port_idx+2} is changing", )

    cdef void update_changing_knm_workspaces(KnmConnectorWorkspace self) nogil:
        cdef:
            NodeBeamParam *q_from
            NodeBeamParam *q_to
            KnmInfo *info
            complex_t qx_from_trns, qy_from_trns

        for i in range(self.N_opt_conns):
            info = &self.oconn_info[i]
            ni_idx = self.onode_ids[2*info.from_port_idx]
            no_idx = self.onode_ids[2*info.to_port_idx+1]
            q_from = &self.sim.trace[ni_idx]
            q_to = &self.sim.trace[no_idx]

            # if there's some changing Knm then we need to recompute it. Which parts need
            # to be recomputed are decided here then performed
            if info.K_ws_x.is_mm_changing:
                qx_from_trns = c_transform_q(info.abcd_x, q_from.qx.q, info.nr_from, info.nr_to)
                if info.beta_x == NULL:
                    knm_bh_ws_recompute_mismatch(info.K_ws_x, qx_from_trns, q_to.qx.q)
                else:
                    knm_bh_ws_recompute(info.K_ws_x, qx_from_trns, q_to.qx.q, info.beta_x[0])

            elif info.K_ws_x.is_alignment_changing and info.beta_x != NULL:
                knm_bh_ws_recompute_misalignment(info.K_ws_x, info.beta_x[0])

            if info.K_ws_y.is_mm_changing:
                qy_from_trns = c_transform_q(info.abcd_y, q_from.qy.q, info.nr_from, info.nr_to)
                if info.beta_y == NULL:
                    knm_bh_ws_recompute_mismatch(info.K_ws_y, qy_from_trns, q_to.qy.q)
                else:
                    knm_bh_ws_recompute(info.K_ws_y, qy_from_trns, q_to.qy.q, info.beta_y[0])

            elif info.K_ws_y.is_alignment_changing and info.beta_y != NULL:
                knm_bh_ws_recompute_misalignment(info.K_ws_y, info.beta_y[0])

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.initializedcheck(False)
    cdef void compute_scattering_matrices(KnmConnectorWorkspace self):
        cdef:
            KnmInfo *info
            Py_ssize_t i

        for i in range(self.N_opt_conns):
            info = &self.oconn_info[i]
            if knm_bh_ws_is_changing(info.K_ws_x) or knm_bh_ws_is_changing(info.K_ws_y):
                info.bhelms_mtx_func(
                    info.K_ws_x,
                    info.K_ws_y,
                    self.sim.model_data.homs_ptr,
                    info.mtx.ptr,
                    self.sim.model_data.num_HOMs,
                    self.sim.config_data.nthreads_homs,
                )

    @cython.boundscheck(False)
    @cython.wraparound(False)
    @cython.initializedcheck(False)
    cdef void compute_knm_losses(KnmConnectorWorkspace self) nogil:
        cdef:
            KnmInfo *info
            Py_ssize_t i

        for i in range(self.N_opt_conns):
            info = &self.oconn_info[i]
            if knm_bh_ws_is_changing(info.K_ws_x) or knm_bh_ws_is_changing(info.K_ws_y):
                knm_loss(info.mtx.ptr, info.loss, self.sim.model_data.num_HOMs)


# N.B. This function depends on the order of ports / nodes being consistent between
# ws.onode_ids and ws.oconn_info, and may break if this order is changed.
# TODO: This doesn't consider the couplings in the signal matrix, effectively assuming they're 1,
# which isn't always correct.
optical_quantum_noise_knm = FillFuncWrapper.make_from_ptr(c_optical_quantum_noise_knm)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cdef object c_optical_quantum_noise_knm(ConnectorWorkspace cws):
    cdef:
        KnmConnectorWorkspace ws = <KnmConnectorWorkspace> cws
        NoiseInfo noises = ws.output_noise
        frequency_info_t *freq

        Py_ssize_t i, j, k, h
        Py_ssize_t port_idx

        complex_t factor

    if ws.sim.signal.nhoms == 0:
        return
    for i in range(ws.sim.signal.optical_frequencies.size):
        freq = &(ws.sim.signal.optical_frequencies.frequency_info[i])
        factor = 0.5 * (1 + freq.f_car[0] / ws.sim.model_data.f0)
        for j in range(noises.num_nodes):
            port_idx = -1
            for k in range(ws.N_opt_ports):
                if ws.onode_ids[2 * k + 1] == noises.node_info[j].idx:
                    port_idx = k
                    break
            if port_idx == -1:
                continue
            ws.total_losses[:] = 0
            for k in range(ws.N_opt_conns):
                if ws.oconn_info[k].to_port_idx == port_idx:
                    for h in range(ws.sim.signal.nhoms):
                        ws.total_losses[h] += ws.oconn_info[k].loss[h]
            (<SubCCSView>noises.ptrs[j][freq.index]).fill_za_dd(factor, ws.total_losses)
