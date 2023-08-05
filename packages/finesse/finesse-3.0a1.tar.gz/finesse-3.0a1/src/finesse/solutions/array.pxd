from finesse.solutions.base import BaseSolution
from finesse.solutions.base cimport BaseSolution

from cpython.ref cimport PyObject

import numpy as np
cimport numpy as np


cdef class ArraySolution(BaseSolution):
    cdef:
        readonly np.ndarray _outputs
        readonly np.dtype _dtype
        readonly int _axes
        readonly int _num
        public list _units
        readonly tuple x
        readonly tuple params
        readonly tuple detectors
        readonly bint masked
        PyObject** workspaces
        Py_ssize_t num_workspaces

    cpdef int update(self, int index, bint mask)
