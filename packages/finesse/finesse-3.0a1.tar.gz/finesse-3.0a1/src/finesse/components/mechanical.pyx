
import logging
LOGGER = logging.getLogger(__name__)

cimport cython
import finesse.constants
from finesse.cmatrix import SubCCSView
from finesse.cmatrix cimport SubCCSView
from finesse.components.workspace cimport ConnectorWorkspace, FillFuncWrapper
from finesse.components.workspace import Connections
from finesse.cymath cimport complex_t
from finesse.components import Connector, NodeType, NodeDirection
from finesse.parameter import float_parameter
from finesse.components.general import DOFDefinition

from cpython.ref cimport PyObject, Py_XINCREF, Py_XDECREF
from libc.string cimport strcmp, memcpy
from libc.stdlib cimport free, calloc

cimport numpy as np
import numpy as np

cdef extern from "constants.h":
    long double PI


def get_mechanical_port(connect_to):
    # Handle different types of elements or mech ports to connect to
    if isinstance(connect_to, Connector):
        mech_ports = [p for p in connect_to.ports if p.type == NodeType.MECHANICAL]
        if len(mech_ports) > 1:
            raise Exception(f"{connect_to} has more than one mechanical node so please specify which to use.")
        return mech_ports[0]
    else:
        return connect_to


cdef class MIMOTFWorkspace(ConnectorWorkspace):
    """Workspace that contains MIMO transfer functions stored
    in a numerator/denominator basis.
    """

    cdef:
        double[::1] denom
        Py_ssize_t N_num_allocd
        Py_ssize_t curr_num
        double** numerators
        int* numerator_sizes
        complex_t curr_denom
        complex_t s

    def __cinit__(self, owner, sim, refill, unsigned int N_numerators):
        self.N_num_allocd = N_numerators
        self.numerators = <double**>calloc(N_numerators, sizeof(double*))
        if not self.numerators:
            raise MemoryError()
        self.numerator_sizes = <int*>calloc(N_numerators, sizeof(int))
        if not self.numerator_sizes:
            raise MemoryError()
        self.curr_num = 0
        self.curr_denom = 0

    def __init__(self, owner, sim, bint refill, unsigned int N_numerators):
        super().__init__(
            owner,
            sim,
            refill,
            refill,
            Connections(),
            Connections()
        )
        self.signal.add_fill_function(mimo_fill, refill)

    def __dealloc__(self):
        if self.numerators:
            free(self.numerators)
        if self.numerator_sizes:
            free(self.numerator_sizes)

    @property
    def num_numerators(self):
        return self.curr_num

    def set_denominator(self, double[::1] denom):
        self.denom = denom

    def add_numerator(self, double[::1] num):
        if self.curr_num == self.N_num_allocd:
            raise Exception("Added more numerators than were allocated for.")
        self.numerators[self.curr_num] = &num[0]
        self.numerator_sizes[self.curr_num] = len(num)
        self.curr_num += 1

    cpdef void set_s(self, complex_t s):
        self.s = s
        self.curr_denom = eval_tf_term(s, &self.denom[0], len(self.denom))

    cpdef complex_t H(self, int numerator_idx):
        if not (0 <= numerator_idx < self.curr_num):
            raise Exception("Unexpected index")

        return eval_tf(
            self.s,
            self.numerators[numerator_idx],
            self.numerator_sizes[numerator_idx],
            self.curr_denom
        )


@cython.wraparound(False)
@cython.boundscheck(False)
@cython.initializedcheck(False)
cdef inline complex_t eval_tf_term(complex_t s, const double* coeffs, int N):
    cdef:
        int i
        complex res = 0
    for i in range(N):
        res = res * s + coeffs[i]

    return res


@cython.wraparound(False)
@cython.boundscheck(False)
@cython.initializedcheck(False)
cdef inline complex_t eval_tf(complex_t s, const double* num, int N, complex_t den):
    return eval_tf_term(s, num, N)/den


@cython.wraparound(False)
@cython.boundscheck(False)
@cython.initializedcheck(False)
cpdef eval_tf_vec(const complex_t[::1] s, const double[::1] num, const double[::1] den, complex_t[::1] out):
    cdef:
        int i
        complex_t oden = 0
        int N = len(s)
        int Nn = len(num)
        int Nd = len(den)

    if len(out) != len(s):
        raise Exception("Length of `s` differs from output `out`")

    for i in range(N):
        out[i] = eval_tf_term(s[i], &num[0], Nn)/eval_tf_term(s[i], &den[0], Nd)

    return 0

mimo_fill = FillFuncWrapper.make_from_ptr(c_mimo_fill)
@cython.wraparound(False)
@cython.boundscheck(False)
@cython.initializedcheck(False)
cdef c_mimo_fill(ConnectorWorkspace cws):
    cdef MIMOTFWorkspace ws = <MIMOTFWorkspace>cws
    cdef complex_t s = 0
    cdef tuple key
    s.imag = 2 * PI * ws.sim.model_data.fsig
    # Sets the complex s value for this step and precomputes the denominator
    ws.set_s(s)
    for i in range(ws.curr_num):
        key = (ws.owner_id,i,0,0)
        if key in ws.sim.signal._submatrices:
            (<SubCCSView>ws.sim.signal._submatrices[key]).fill_negative_za(ws.H(i))


class Joint(Connector):
    """Represents a mechanical joint between two mechanical ports in the model.

    TODO:
        - Need some way of specifying transfer functions for coupling
          between the two ports in question.

    Parameters
    ----------
    name : str, optional
        Name of newly created joint.

    portA, portB : :class:`.Port`, optional
        Ports to connect.

    connections : ?
    """

    def __init__(self, name=None, portA=None, portB=None, connections=None):
        if (portA is None) != (portB is None):
            LOGGER.warn(
                "Can't construct a joint with only one port "
                "connected, ignoring ports."
            )
            portA = None
            portB = None

        if portA is not None and portA.type != NodeType.MECHANICAL:
            raise Exception("PortA argument is not a mechanical port")
        if portB is not None and portB.type != NodeType.MECHANICAL:
            raise Exception("PortB argument is not a mechanical port")

        if name is None:
            if portA is not None and portB is not None:
                compA = portA.component.name
                compB = portB.component.name
                name = f"{compA}_{portA.name}__{compB}_{portB.name}"
            else:
                raise ValueError(
                    "Cannot create an unconnected wire without " "providing a name"
                )

        super().__init__(name)
        self._add_to_model_namespace = False

        self.portA = portA
        self.portB = portB

        """
        The mechanical ports have nodes that are the motion degrees of
        freedom, so there can potentially be many, but the usual are z,
        yaw, pitch. We just make copies of the nodes here that are in
        each mechanical port.
        """
        self._add_port("n1", NodeType.MECHANICAL)
        self._add_port("n2", NodeType.MECHANICAL)

        if portA is not None and portB is not None:
            self.connect(portA, portB)

    def connect(self, portA, portB):
        """
        Sets the ports of this `Joint`.

        Parameters
        ----------
        portA : :class:`.Port`, optional
            Port to connect

        portB : :class:`.Port`, optional
            Port to connect
        """
        for n in portA.nodes:
            self.n1._add_node(n.name, None, n)

        for n in portB.nodes:
            self.n2._add_node(n.name, None, n)
        """
        I'm not sure of the perfect way to link up two mechanical ports.
        For now I'm going to link up matching names. So z motion of one
        mech port is linked to the z node of the other.

        If there is only one node in a port in both then just connect
        them up.
        """
        if len(portA.nodes) == len(portB.nodes) == 1:
            self._register_node_coupling(portA.nodes[0], portB.nodes[0])
        else:
            for na in portA.nodes:
                for nb in portB.nodes:
                    if na.name == nb.name:
                        self._register_node_coupling(na, nb)

    def _on_init(self, sim):
        # TODO: (sjr) does this need to have rows > 1 for HOM simulations?
        self.__I = np.eye(sim.model_data.num_HOMs, dtype=np.complex128)

    def _fill_matrix(self, sim):
        for c in list(self._registered_connections):
            with sim.signal.component_edge_fill(self, c, None, None) as mat:
                mat[:] = self.__I


class FreeMassWorkspace(ConnectorWorkspace):
    pass


@float_parameter("mass", "Mass", units="kg")
@float_parameter("I_pitch", "Moment of inertia (pitch)", units="kg·m^2")
@float_parameter("I_yaw", "Moment of inertia (yaw)", units="kg·m^2")
class FreeMass(Connector):
    """Simple free mass suspension of an object.

    The object being suspended must have a mechanical port with
    nodes z, pitch, and yaw and forces F_z, F_pitch, and F_yaw.
    """

    def __init__(self, name, connect_to, mass=np.inf, I_yaw=np.inf, I_pitch=np.inf):
        super().__init__(name)
        mech_port = get_mechanical_port(connect_to)
        self.mass = mass
        self.I_yaw = I_yaw
        self.I_pitch = I_pitch

        # Add motion and force nodes to mech port.
        # Here we duplicate the already created mechanical
        # nodes in some other connector element
        self._add_port("mech", NodeType.MECHANICAL)
        self.mech._add_node("z", None, mech_port.z)
        self.mech._add_node("yaw", None, mech_port.yaw)
        self.mech._add_node("pitch", None, mech_port.pitch)
        self.mech._add_node("F_z", None, mech_port.F_z)
        self.mech._add_node("F_yaw", None, mech_port.F_yaw)
        self.mech._add_node("F_pitch", None, mech_port.F_pitch)
        # We just have direct coupling between DOF, no cross-couplings
        self._register_node_coupling(
            "F_to_Z", self.mech.F_z, self.mech.z,
            enabled_check=lambda: float(self.mass) < np.inf and not self.mass.is_changing
        )
        self._register_node_coupling(
            "F_to_YAW", self.mech.F_yaw, self.mech.yaw,
            enabled_check=lambda: float(self.I_yaw) < np.inf and not self.I_yaw.is_changing
        )
        self._register_node_coupling(
            "F_to_PITCH", self.mech.F_pitch, self.mech.pitch,
            enabled_check=lambda: float(self.I_pitch) < np.inf and not self.I_pitch.is_changing
        )
        # Define typical degrees of freedom for this component
        import types
        self.dofs = types.SimpleNamespace()
        self.dofs.z = DOFDefinition(None, self.mech.z, 1)
        self.dofs.F_z = DOFDefinition(None, self.mech.F_z, 1)

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing or any(p.is_changing for p in self.parameters)
            ws = FreeMassWorkspace(self, sim, refill, refill)
            ws.signal.add_fill_function(self.fill, refill)
            return ws
        else:
            return None

    def fill(self, ws):
        f = ws.sim.model_data.fsig
        if ws.signal.connections.F_to_Z_idx >= 0:
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id, ws.signal.connections.F_to_Z_idx, 0, 0,
            ) as mat:
                mat[:] = -1 / (ws.values.mass * (2*PI*f)**2)

        if ws.signal.connections.F_to_YAW_idx >= 0:
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id, ws.signal.connections.F_to_YAW_idx, 0, 0,
            ) as mat:
                mat[:] = -1 / (ws.values.I_yaw * (2*PI*f)**2)

        if ws.signal.connections.F_to_PITCH_idx >= 0:
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id, ws.signal.connections.F_to_PITCH_idx, 0, 0,
            ) as mat:
                mat[:] = -1 / (ws.values.I_pitch * (2*PI*f)**2)


class PendulumMassWorkspace(ConnectorWorkspace):
    pass


@float_parameter("mass", "Mass", units="kg")
@float_parameter("Qz", "Qz", units="")
@float_parameter("fz", "fz", units="Hz")
@float_parameter("I_pitch", "Moment of inertia (pitch)", units="kg·m^2")
@float_parameter("Qyaw", "Qyaw", units="")
@float_parameter("fyaw", "fyaw", units="Hz")
@float_parameter("I_yaw", "Moment of inertia (yaw)", units="kg·m^2")
@float_parameter("Qpitch", "Qpitch", units="")
@float_parameter("fpitch", "fpitch", units="Hz")
class Pendulum(Connector):
    """Simple pendulum suspension of an object.

    The object being suspended must have a mechanical port with
    nodes z, pitch, and yaw and forces F_z, F_pitch, and F_yaw.
    """

    def __init__(self, name, mech_port, mass=np.inf, Qz=1000, fz=1, I_yaw=np.inf, Qyaw=1000, fyaw=1, I_pitch=np.inf, Qpitch=1000, fpitch=1):
        super().__init__(name)
        self.mass = mass
        self.Qz = Qz
        self.fz = fz
        self.Qyaw = Qyaw
        self.fyaw = fyaw
        self.Qpitch = Qpitch
        self.fpitch = fpitch
        self.I_yaw = I_yaw
        self.I_pitch = I_pitch

        # Add motion and force nodes to mech port.
        # Here we duplicate the already created mechanical
        # nodes in some other connector element
        self._add_port("mech", NodeType.MECHANICAL)
        self.mech._add_node("z", None, mech_port.z)
        self.mech._add_node("yaw", None, mech_port.yaw)
        self.mech._add_node("pitch", None, mech_port.pitch)
        self.mech._add_node("F_z", None, mech_port.F_z)
        self.mech._add_node("F_yaw", None, mech_port.F_yaw)
        self.mech._add_node("F_pitch", None, mech_port.F_pitch)
        # We just have direct coupling between DOF, no cross-couplings
        self._register_node_coupling(
            "F_to_Z", self.mech.F_z, self.mech.z,
            enabled_check=lambda: float(self.mass) < np.inf and not self.mass.is_changing
        )
        self._register_node_coupling(
            "F_to_YAW", self.mech.F_yaw, self.mech.yaw,
            enabled_check=lambda: float(self.I_yaw) < np.inf and not self.I_yaw.is_changing
        )
        self._register_node_coupling(
            "F_to_PITCH", self.mech.F_pitch, self.mech.pitch,
            enabled_check=lambda: float(self.I_pitch) < np.inf and not self.I_pitch.is_changing
        )

    def _get_workspace(self, sim):
        if sim.signal:
            refill = sim.model.fsig.f.is_changing or any(p.is_changing for p in self.parameters)
            ws = PendulumMassWorkspace(self, sim, refill, refill)
            ws.signal.add_fill_function(self.fill, refill)
            return ws
        else:
            return None

    def fill(self, ws):
        cdef:
            complex_t s = 2j* PI * ws.sim.model_data.fsig
            complex_t num = 1
            complex_t den = 1
            double omega0

        if ws.signal.connections.F_to_Z_idx >= 0:
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id, ws.signal.connections.F_to_Z_idx, 0, 0,
            ) as mat:
                omega0 = 2 * PI * ws.values.fz
                mat[:] = 1 / ws.values.mass * 1/(s**2  + s * omega0/ws.values.Qz + omega0**2)

        if ws.signal.connections.F_to_YAW_idx >= 0:
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id, ws.signal.connections.F_to_YAW_idx, 0, 0,
            ) as mat:
                omega0 = 2 * PI * ws.values.fyaw
                mat[:] = 1 / ws.values.I_yaw * 1/(s**2  + s * omega0/ws.values.Qyaw + omega0**2)

        if ws.signal.connections.F_to_PITCH_idx >= 0:
            with ws.sim.signal.component_edge_fill3(
                ws.owner_id, ws.signal.connections.F_to_PITCH_idx, 0, 0,
            ) as mat:
                omega0 = 2 * PI * ws.values.fpitch
                mat[:] = 1 / ws.values.I_pitch * 1/(s**2  + s * omega0/ws.values.Qpitch + omega0**2)
