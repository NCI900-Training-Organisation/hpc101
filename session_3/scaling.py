"""Strong scaling study of the parallel reduction.

Runs exactly the same function on an increasing number of threads, keeping the
problem size fixed. That is the definition of strong scaling, and it is what
Amdahl's Law describes.

Every row uses the *same* parallel=True function, so the speedup column
measures threading alone. Comparing against the serial @jit function instead
would also fold in the difference between the two compilation paths, which has
nothing to do with how many cores you asked for.
"""

import time

import numpy as np
import numba
from numba import jit, prange

N = 10000000


@jit(nopython=True, parallel=True)
def reduction(n):
    shp = (13, 17)
    result1 = np.zeros(shp, np.int64)
    tmp = np.ones(shp, np.int64)

    for i in prange(n):
        result1 += tmp

    return result1


def best_of(func, n, repeats=3):
    """Return the fastest of several runs, to reduce the effect of noise."""
    best = None
    for _ in range(repeats):
        start = time.time()
        func(n)
        elapsed = time.time() - start
        if best is None or elapsed < best:
            best = elapsed
    return best


if __name__ == "__main__":
    max_threads = numba.get_num_threads()
    print("Maximum threads available:", max_threads)

    # Compile once, before any timing.
    reduction(1)

    counts = sorted({c for c in (1, 2, 4, 8, 16, 24, 48) if c <= max_threads}
                    | {1, max_threads})

    results = []
    for count in counts:
        numba.set_num_threads(count)
        results.append((count, best_of(reduction, N)))
    numba.set_num_threads(max_threads)

    baseline = results[0][1]

    print()
    print(" threads       time(s)    speedup   efficiency")
    for count, elapsed in results:
        speedup = baseline / elapsed
        print("{:>8}   {:>11.4f}   {:>7.2f}x   {:>9.0f}%".format(
            count, elapsed, speedup, 100 * speedup / count))
