#cython: boundscheck=False, wraparound=False, initializedcheck=False

"""Standard mathematical functions for non-complex calculations.

Most of the standard functions of the C ``"math.h"`` header are exposed
at a C level via this module. Refer to the `Common Mathematical Functions C reference
<https://en.cppreference.com/w/c/numeric/math>`_ for the names, arguments
and further details on these functions. One can ``cimport`` such functions
in the same way as cimporting any other C exposed Cython function. For example::

    from finesse.cymath.math cimport sin

will ``cimport`` the `sin <https://en.cppreference.com/w/c/numeric/math/sin>`_ function
for use on ``double`` data types in another Cython extension.
"""

cdef double NATLOGS_N[101]
cdef int NATLOG_MAX = 0

# TODO can probably just store many more than [0-20]!
# pre-computed factorials up to (and including) 20!
# -> stored as double to avoid integer overflow, factorials
#    required for just floating point calcs (so far) anyway
cdef double* FACTORIALS = [
    1.0,
    1.0,
    2.0,
    6.0,
    24.0,
    120.0,
    720.0,
    5040.0,
    40320.0,
    362880.0,
    3628800.0,
    39916800.0,
    479001600.0,
    6227020800.0,
    87178291200.0,
    1307674368000.0,
    20922789888000.0,
    355687428096000.0,
    6402373705728000.0,
    121645100408832000.0,
    2432902008176640000.0
]

cdef double* SQRT_FACTORIALS = [
    1.0,
    1.0,
    1.4142135623730951,
    2.4494897427831779,
    4.8989794855663558,
    10.9544511501033224,
    26.8328157299974777,
    70.9929573971953971,
    200.7984063681781208,
    602.3952191045343625,
    1904.9409439665053014,
    6317.9743589223280651,
    21886.1051811417564750,
    78911.4744508046860574,
    295259.7012800764641725,
    1143535.9058639130089432,
    4574143.6234556520357728,
    18859677.3062531463801861,
    80014834.2854498475790024,
    348776576.6344293951988220,
    1559776268.6284978389739990,
]


cpdef double factorial(int n) nogil:
    global FACTORIALS

    if n < 21:
        return FACTORIALS[n]

    cdef int i

    global NATLOGS_N
    global NATLOG_MAX

    if n <= NATLOG_MAX:
        return exp(NATLOGS_N[n])

    for i in range(NATLOG_MAX + 1, n + 1):
        NATLOGS_N[i] = NATLOGS_N[i - 1] + log(i)

    NATLOG_MAX = n

    return exp(NATLOGS_N[n])

cpdef double sqrt_factorial(int n) nogil:
    global SQRT_FACTORIALS

    if n < 21:
        return SQRT_FACTORIALS[n]

    return sqrt(factorial(n))

cpdef double hermite(int n, double x) nogil:
    if n == 0:
        return (1.0)
    if n == 1:
        return (2.0 * x)
    if n == 2:
        return (4.0 * x * x - 2.0)
    if n == 3:
        return (8.0 * x * x * x - 12.0 * x)
    if n == 4:
        return (16.0 * x * x * x * x - 48.0 * x * x + 12.0)
    if n == 5:
        return (32.0 * x * x * x * x * x - 160.0 * x * x * x + 120.0 * x)
    if n == 6:
        return (64.0 * x * x * x * x * x * x - 480.0 * x * x * x * x + 720.0 * x * x - 120.0)
    if n == 7:
        return (128.0 * x**7 - 1344.0 * x * x * x * x * x + 3360.0 * x * x * x -
                1680.0 * x)
    if n == 8:
        return (256.0 * x**8 - 3584.0 * x * x * x * x * x * x + 13440.0 * x * x * x * x
                - 13440.0 * x * x + 1680.0)
    if n == 9:
        return (512.0 * x**9 - 9216.0 * x**7 + 48384.0 * x * x * x * x * x
                - 80640.0 * x * x * x + 30240.0 * x)
    if n == 10:
        return (1024.0 * x**10 - 23040.0 * x**8 + 161280.0 * x * x * x * x * x * x
                - 403200.0 * x * x * x * x + 302400.0 * x * x - 30240.0)
    if n == 11:
        return (2048.0 * x**11 - 56320.0 * x**9 + 506880.0 * x**7 - 1774080.0 * x * x * x * x * x
                + 2217600.0 * x * x * x - 665280.0 * x)
    if n == 12:
        return (4096.0 * x**12 - 135168.0 * x**10 + 1520640.0 * x**8 - 7096320.0 * x * x * x * x * x * x
                + 13305600.0 * x * x * x * x - 7983360.0 * x*x + 665280.0)
    if n == 13:
        return (8192.0 * x**13 - 319488.0 * x**11 + 4392960.0 * x**9 - 26357760.0 * x**7
                + 69189120.0 * x * x * x * x * x - 69189120.0 * x * x * x + 17297280.0 * x)
    if n == 14:
        return (16384.0 * x**14 - 745472.0 * x**12 + 12300288.0 * x**10 - 92252160.0 * x**8
                + 322882560.0 * x * x * x * x * x * x - 484323840.0 * x * x * x * x + 242161920.0 * x*x - 17297280.0)
    if n == 15:
        return (32768.0 * x**15 - 1720320.0 * x**13 + 33546240.0 * x**11
                - 307507200.0 * x**9 + 1383782400.0 * x**7 - 2905943040.0 * x * x * x * x * x
                + 2421619200.0 * x * x * x - 518918400.0 * x)
    if n == 16:
        return (65536.0 * x**16 - 3932160.0 * x**14 + 89456640.0 * x**12 - 984023040.0 * x**10
                + 5535129600.0 * x**8 - 15498362880.0 * x * x * x * x * x * x + 19372953600.0 * x * x * x * x
                - 8302694400.0 * x*x + 518918400.0)
    if n == 17:
        return (131072.0 * x**17 - 8912896.0 * x**15 + 233963520.0 * x**13 - 3041525760.0 * x**11
                + 20910489600.0 * x**9 - 75277762560.0 * x**7 + 131736084480.0 * x * x * x * x * x
                - 94097203200.0 * x * x * x + 17643225600.0 * x)
    if n == 18:
        return (262144.0 * x**18 - 20054016.0 * x**16 + 601620480.0 * x**14  -9124577280.0 * x**12
                + 75277762560.0 * x**10 - 338749931520.0 * x**8 + 790416506880.0 * x * x * x * x * x * x
                - 846874828800.0 * x * x * x * x + 317578060800.0 * x*x - 17643225600.0)
    if n == 19:
        return (524288.0 * x**19 - 44826624.0 * x**17 + 1524105216.0 * x**15 - 26671841280.0 * x**13
                + 260050452480.0 * x**11 - 1430277488640.0 * x**9 + 4290832465920.0 * x**7 -
                6436248698880.0 * x * x * x * x * x + 4022655436800.0 * x * x * x - 670442572800.0 * x)
    if n == 20:
        return (1048576.0 * x**20 - 99614720.0 * x**18 + 3810263040.0 * x**16 - 76205260800.0 * x**14
                + 866834841600.0 * x**12 - 5721109954560.0 * x**10 + 21454162329600.0 * x**8
                - 42908324659200.0 * x * x * x * x * x * x + 40226554368000.0 * x * x * x * x - 13408851456000.0 * x*x + 670442572800.0)

    return (2 * x * hermite(n - 1, x) - 2 * (n - 1) * hermite(n - 2, x))
