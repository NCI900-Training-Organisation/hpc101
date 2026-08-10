"""Compare a serial and a parallel reduction using Numba.

Both functions do exactly the same work: they add ``tmp`` into ``result`` n
times, so every element of the answer should end up equal to n. The only
difference between them is ``parallel=True``, which lets Numba spread the
``prange`` loop across the cores the job asked for.
"""

import time

import numpy as np
import numba
from numba import jit, prange

N = 10000000


@jit(nopython=True)
def reduction_without_parallel(n):
    shp = (13, 17)
    result1 = np.zeros(shp, np.int64)
    tmp = np.ones(shp, np.int64)

    for i in prange(n):
        result1 += tmp

    return result1


@jit(nopython=True, parallel=True)
def reduction_with_parallel(n):
    shp = (13, 17)
    result1 = np.zeros(shp, np.int64)
    tmp = np.ones(shp, np.int64)

    for i in prange(n):
        result1 += tmp

    return result1


def time_it(func, n):
    """Return how long func(n) took, along with its result."""
    start = time.time()
    result = func(n)
    end = time.time()
    return end - start, result


if __name__ == "__main__":
    max_threads = numba.get_num_threads()
    print("Threads available to Numba:", max_threads)

    # Numba compiles each function the first time it is called, and compiling
    # a parallel=True function is considerably slower. Call both with a tiny
    # value first, so that what we time below is the computation itself and
    # not the one-off cost of compiling it.
    reduction_without_parallel(1)
    reduction_with_parallel(1)

    serial_time, serial_result = time_it(reduction_without_parallel, N)
    print("Time without parallel:", serial_time)

    parallel_time, parallel_result = time_it(reduction_with_parallel, N)
    print("Time with parallel:", parallel_time)

    print("Speedup: {:.2f}x".format(serial_time / parallel_time))

    # Not all of that speedup comes from using more cores. Compiling with
    # parallel=True also changes the code Numba generates, so run the same
    # parallel function on a single thread to separate the two effects.
    numba.set_num_threads(1)
    one_thread_time, _ = time_it(reduction_with_parallel, N)
    numba.set_num_threads(max_threads)

    print("  of which, from compiling with parallel=True: {:.2f}x".format(
        serial_time / one_thread_time))
    print("  of which, from using {} threads:             {:.2f}x".format(
        max_threads, one_thread_time / parallel_time))

    # both versions must agree, and every element should be exactly N.
    assert (serial_result == N).all()
    assert (parallel_result == serial_result).all()
    print("Both versions agree: every element equals", N)
