import multiprocessing
import numpy as np
import sys
from time import perf_counter as timer

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100


def chunk_processor(points):
    gen = (mandelbrot_escape_time(c) for c in points)
    return np.fromiter(gen, dtype=np.float64, count=len(points))


# Accidentally made 3_3 instead of 3_2
def generate_mandelbrot_set(points, num_processes):
    chunks = np.array_split(points, num_processes)

    pool = multiprocessing.Pool(num_processes)
    results_async = [pool.apply_async(chunk_processor, (chunk,)) for chunk in chunks]
    arrs = [r.get() for r in results_async]
    escape_times = np.concatenate(arrs)
    return escape_times


if __name__ == "__main__":
    time_start = timer()

    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2

    num_proc = int(sys.argv[1])

    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    # Compute set
    mandelbrot_set = generate_mandelbrot_set(points, num_proc)

    time_elapsed = timer() - time_start

    print(f"{num_proc}\t{time_elapsed:3f}")
