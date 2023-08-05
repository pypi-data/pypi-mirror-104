import contextlib

import logging

cimport cython

cimport numpy as np
import numpy as np

import networkx as nx

from finesse.cymath cimport complex_t
from finesse.cymath.complex cimport conj
from finesse.cymath.math cimport float_eq
from finesse.cymath.gaussbeam cimport transform_q, inv_transform_q
from finesse.element cimport ElementWorkspace
from finesse.frequency cimport Frequency
from finesse.components.workspace cimport ConnectorCallbacks, ConnectorWorkspace
from finesse.components.node import NodeType

from finesse.components.modal.cavity cimport CavityWorkspace

from cpython.ref cimport PyObject
from libc.stdio cimport printf


cdef extern from "stdlib.h":
    void  free(void* ptr)
    void* malloc(size_t size)
    void* calloc(size_t N, size_t size)


cdef extern from "constants.h":
    long double PI
    double C_LIGHT
    double complex COMPLEX_0


LOGGER = logging.getLogger(__name__)


cdef class ModelData:
    pass
