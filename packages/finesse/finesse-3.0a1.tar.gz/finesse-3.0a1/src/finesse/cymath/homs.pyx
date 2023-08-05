#cython: boundscheck=False, wraparound=False, initializedcheck=False

"""Fast computations of Higher-Order Mode related properties.

This module provides functions for computing properties of HOMs, such as
the spatial distribution :math:`u_{nm}(x,y,z;q_x,q_y)` of Hermite-Gauss
modes.

.. note::
    These are low-level functions intended for use, by developers, in Cython
    extensions. To calculate HG mode profiles, for example, users should
    instead use the Python class :class:`.HGMode` defined in :mod:`finesse.gaussian`.
"""

from libc.stdlib cimport calloc, free

cimport numpy as np
import numpy as np

from cython.parallel import prange

from finesse.cymath.complex cimport complex_t, inverse_unsafe, ceq, cpow_re, cexp
from finesse.cymath.gaussbeam cimport waist_size, beam_size, gouy
from finesse.cymath.math cimport ceil, floor
from finesse.cymath.math cimport factorial, sqrt_factorial, hermite, nmin

from finesse.utilities.cyomp cimport determine_nthreads_even


cdef extern from "complex.h" nogil:
    double cimag(double complex z)
    double creal(double complex z)
    double complex csqrt(double complex z)
    double complex conj(double complex z)

cdef extern from "math.h" nogil:
    double exp(double arg)
    double sqrt(double arg)

cdef extern from "constants.h":
    long double PI
    double TWO_ON_PI_QRT # (2/pi)^{1/4}
    double ROOT2
    double complex COMPLEX_0


### Spatial distribution (u_m, u_m) functions and workspace for HG modes ###

# See Eq. (9.34) in "Interferometer Techniques for Gravitational Wave Detection"
# as main point of reference for equations used in functions below

## General workspace struct for u_nm calculations ##

cdef void unm_ws_recache_from_bp(
    unm_workspace* uws,
    const beam_param* qx,
    const beam_param* qy,
    int* n=NULL,
    int* m=NULL,
): # Initialise uws from beam_param constructs
    unm_ws_recache(uws, qx.q, qy.q, qx.nr, qx.wavelength, n, m)

cdef void unm_ws_recache(
    unm_workspace* uws,
    complex_t qx,
    complex_t qy,
    double nr,
    double lambda0,
    int* n=NULL,
    int* m=NULL,
) nogil:
    cdef:
        double zrx = cimag(qx)
        double zry

    uws.k = 2.0 * PI / lambda0 * nr
    uws.root_w0x = sqrt(waist_size(qx, nr, lambda0))
    uws.gouyx = gouy(qx)
    uws.root2_on_wx = ROOT2 / beam_size(qx, nr, lambda0)
    uws.inv_qx = inverse_unsafe(qx)
    uws.xgauss_exponent = -1j * 0.5 * uws.k * uws.inv_qx
    uws.z1x = csqrt((0.0 + zrx * 1j) / qx)
    uws.z2x = csqrt((0.0 + zrx * 1j) * conj(qx) / ((0.0 - zrx * 1j) * qx))
    # If n is given then store it and calculate the terms
    # before Hn(x') present in the u_n equation
    if n != NULL:
        uws.n = n[0]
        uws.xpre_factor = (
            TWO_ON_PI_QRT
            * 1 / (sqrt(2**uws.n) * sqrt_factorial(uws.n) * uws.root_w0x)
            * uws.z1x * cpow_re(uws.z2x, uws.n)
        )
    else:
        uws.n = -1
        uws.xpre_factor = COMPLEX_0

    # Equality check quicker than other calculations
    if ceq(qx, qy):
        uws.root_w0y = uws.root_w0x
        uws.gouyy = uws.gouyx
        uws.root2_on_wy = uws.root2_on_wx
        uws.inv_qy = uws.inv_qx
        uws.ygauss_exponent = uws.xgauss_exponent
        uws.z1y = uws.z1x
        uws.z2y = uws.z2x
    else:
        zry = cimag(qy)
        uws.root_w0y = sqrt(waist_size(qy, nr, lambda0))
        uws.gouyy = gouy(qy)
        uws.root2_on_wy = ROOT2 / beam_size(qy, nr, lambda0)
        uws.inv_qy = inverse_unsafe(qy)
        uws.ygauss_exponent = -1j * 0.5 * uws.k * uws.inv_qy
        uws.z1y = csqrt((0.0 + zry * 1j) / qy)
        uws.z2y = csqrt((0.0 + zry * 1j) * conj(qy) / ((0.0 - zry * 1j) * qy))

    # If m is given then store it and calculate the terms
    # before Hm(x') present in the u_m equation
    if m != NULL:
        uws.m = m[0]
        uws.ypre_factor = (
            TWO_ON_PI_QRT
            * 1 / (sqrt(2**uws.m) * sqrt_factorial(uws.m) * uws.root_w0y)
            * uws.z1y * cpow_re(uws.z2y, uws.m)
        )
    else:
        uws.m = -1
        uws.ypre_factor = COMPLEX_0

## Additional specialised u_nm workspace struct holding pre-factor power caches ##

cdef void unm_factor_store_init(
    unm_factor_store* ufs,
    const unm_workspace* uws,
    int max_n,
    int max_m,
) nogil:
    ufs.nsize = 1 + max_n
    ufs.msize = 1 + max_m
    ufs.xpre_factor_cache = <complex_t*> calloc(ufs.nsize, sizeof(complex_t))
    ufs.ypre_factor_cache = <complex_t*> calloc(ufs.msize, sizeof(complex_t))

    unm_factor_store_recache(ufs, uws)

cdef void unm_factor_store_recache(unm_factor_store* ufs, const unm_workspace* uws) nogil:
    cdef complex_t x_const = TWO_ON_PI_QRT * uws.z1x / uws.root_w0x
    cdef complex_t y_const = TWO_ON_PI_QRT * uws.z1y / uws.root_w0y

    cdef int n
    for n in range(ufs.nsize):
        ufs.xpre_factor_cache[n] = (
            x_const * cpow_re(uws.z2x, n) * 1 / (sqrt(2**n) * sqrt_factorial(n))
        )

    cdef int m
    for m in range(ufs.msize):
        ufs.ypre_factor_cache[m] = (
            y_const * cpow_re(uws.z2y, m) * 1 / (sqrt(2**m) * sqrt_factorial(m))
        )

cdef void unm_factor_store_free(unm_factor_store* ufs) nogil:
    if ufs.xpre_factor_cache != NULL: free(ufs.xpre_factor_cache)
    if ufs.ypre_factor_cache != NULL: free(ufs.ypre_factor_cache)

## The u_n, u_m and u_nm functions themselves ##

cdef complex_t u_nm(const unm_workspace* uws, int n, int m, double x, double y) nogil:
    return u_n(uws, n, x) * u_m(uws, m, y)

cdef complex_t u_nm__fast(
    const unm_workspace* uws,
    const unm_factor_store* ufs,
    int n, int m,
    double x, double y
) nogil:
    return u_n__fast(uws, ufs, n, x) * u_m__fast(uws, ufs, m, y)

cdef complex_t u_nmconst(const unm_workspace* uws, double x, double y) nogil:
    return u_nconst(uws, x) * u_mconst(uws, y)


cdef complex_t u_n(const unm_workspace* uws, int n, double x) nogil:
    return (
        TWO_ON_PI_QRT
        * 1 / (sqrt(2**n) * sqrt_factorial(n) * uws.root_w0x)
        * uws.z1x * cpow_re(uws.z2x, n)
        * hermite(n, uws.root2_on_wx * x)
        * cexp(uws.xgauss_exponent * x * x)
    )

cdef complex_t u_n__fast(
    const unm_workspace* uws,
    const unm_factor_store* ufs,
    int n,
    double x,
) nogil:
    return (
        ufs.xpre_factor_cache[n]
        * hermite(n, uws.root2_on_wx * x)
        * cexp(uws.xgauss_exponent * x * x)
    )

cdef complex_t u_nconst(const unm_workspace* uws, double x) nogil:
    return (
        uws.xpre_factor
        * hermite(uws.n, uws.root2_on_wx * x)
        * cexp(uws.xgauss_exponent * x * x)
    )


cdef complex_t u_m(const unm_workspace* uws, int m, double y) nogil:
    return (
        TWO_ON_PI_QRT
        * 1 / (sqrt(2**m) * sqrt_factorial(m) * uws.root_w0y)
        * uws.z1y * cpow_re(uws.z2y, m)
        * hermite(m, uws.root2_on_wy * y)
        * cexp(uws.ygauss_exponent * y * y)
    )

cdef complex_t u_m__fast(
    const unm_workspace* uws,
    const unm_factor_store* ufs,
    int m,
    double y,
) nogil:
    return (
        ufs.ypre_factor_cache[m]
        * hermite(m, uws.root2_on_wy * y)
        * cexp(uws.ygauss_exponent * y * y)
    )

cdef complex_t u_mconst(const unm_workspace* uws, double y) nogil:
    return (
        uws.ypre_factor
        * hermite(uws.m, uws.root2_on_wy * y)
        * cexp(uws.ygauss_exponent * y * y)
    )


### Misc. functions ###


cpdef Py_ssize_t field_index(int n, int m, const int[:, ::1] homs) nogil:
    cdef:
        Py_ssize_t i
        Py_ssize_t N = homs.shape[0]
        int ni, mi

    for i in range(N):
        ni = homs[i][0]
        mi = homs[i][1]

        if ni == n and mi == m:
            return i

    # if mode not found return size of homs array
    return N


cpdef bint in_mask(int n, int m, const int[:, ::1] mask) nogil:
    cdef:
        Py_ssize_t i
        Py_ssize_t Nmasks = mask.shape[0]
        int n_mask, m_mask

    for i in range(Nmasks):
        n_mask = mask[i][0]
        m_mask = mask[i][1]

        if n_mask == n and m_mask == m:
            return True

    return False


cdef class HGModeWorkspace:
    """Fast computation of Hermite-Gauss spatial distributions.

    This workspace class is used internally by :class:`.HGMode`. Users should
    only ever interact with the :class:`.HGMode` object rather than this class."""
    def __init__(
        self, int n, int m, complex_t qx, complex_t qy, double nr, double lambda0
    ):
        self.n = n
        self.m = m

        self.set_values(qx, qy, nr, lambda0)

    cpdef set_values(self, qx=None, qy=None, nr=None, lambda0=None):
        cdef:
            complex_t qx_, qy_
            double nr_, lambda0_

        if qx is not None:
            self.qx = complex(qx)

        if qy is not None:
            self.qy = complex(qy)

        self.is_astigmatic = not ceq(self.qx, self.qy)

        if nr is not None:
            self.nr = float(nr)

        if lambda0 is not None:
            self.lambda0 = float(lambda0)

        unm_ws_recache(&self.uws, self.qx, self.qy, self.nr, self.lambda0, &self.n, &self.m)

    cpdef u_n(self, x, complex_t[::1] out=None):
        from finesse.utilities.misc import is_iterable

        if not is_iterable(x):
            return u_nconst(&self.uws, float(x))

        cdef double[::1] xs = x
        cdef Py_ssize_t N = xs.shape[0]

        cdef np.ndarray[complex_t, ndim=1] out_arr
        if out is None:
            out_arr = np.zeros(N, dtype=np.complex128)
            out = out_arr

        cdef int nthreads = determine_nthreads_even(N, 50)

        cdef Py_ssize_t i
        for i in prange(N, nogil=True, num_threads=nthreads):
            out[i] = u_nconst(&self.uws, xs[i])

        return out.base

    cpdef u_m(self, y, complex_t[::1] out=None):
        from finesse.utilities.misc import is_iterable

        if not is_iterable(y):
            return u_mconst(&self.uws, float(y))

        cdef double[::1] ys = y
        cdef Py_ssize_t N = ys.shape[0]

        cdef np.ndarray[complex_t, ndim=1] out_arr
        if out is None:
            out_arr = np.zeros(N, dtype=np.complex128)
            out = out_arr

        cdef int nthreads = determine_nthreads_even(N, 50)

        cdef Py_ssize_t i
        for i in prange(N, nogil=True, num_threads=nthreads):
            out[i] = u_mconst(&self.uws, ys[i])

        return out.base

    cpdef u_nm(self, x, y, out=None):
        U_n = self.u_n(x)
        if self.n != self.m or self.is_astigmatic:
            U_m = self.u_m(y)
        else:
            U_m = U_n

        # NumPy outer product much faster than manually
        # computing u_nm so use this here instead
        U_nm = np.outer(U_n, U_m)
        if out is not None:
            out[:] = U_nm
            return out
        else:
            return U_nm
