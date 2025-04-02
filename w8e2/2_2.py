import multiprocessing
import sys
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100


def chunk_processor(points, x_idxes, y_idxes, mm_arr):
    for point, x_idx, y_idx, in zip(points, x_idxes, y_idxes):
        mm_arr[x_idx, y_idx] = mandelbrot_escape_time(point)


def generate_mandelbrot_set_chunks(points, x_idxes, y_idxes, num_processes, mm_arr):
    chunks_points = np.array_split(points, num_processes)
    chunks_x_idxes = np.array_split(x_idxes, num_processes)
    chunks_y_idxes = np.array_split(y_idxes, num_processes)

    pool = multiprocessing.Pool(num_processes)
    results_async = [
        pool.apply_async(chunk_processor, (chunk_points, chunk_x_idxes, chunk_y_idxes, mm_arr))
        for (chunk_points, chunk_x_idxes, chunk_y_idxes) in zip(chunks_points, chunks_x_idxes, chunks_y_idxes)
    ]
    _ = [r.get() for r in results_async]


if __name__ == "__main__":
    N = int(sys.argv[1])
    width = N
    height = N
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = 4

    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    x_idxes, y_idxes = np.indices((width, height))
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    # Set up memory-mapped array
    mm_arr = np.memmap("2_2.raw", mode="w+", dtype="int32", shape=(width, height))

    # Compute set
    generate_mandelbrot_set_chunks(points, x_idxes, y_idxes, num_proc, mm_arr)

    mm_arr.flush()

    plt.imshow(mm_arr, cmap="hot", extent=(-2, 2, -2, 2))
    plt.axis("off")
    plt.savefig("2_2.png", bbox_inches="tight", pad_inches=0)

    # This one does not work. Too lazy to fix


    # # Save set as image
    # mandelbrot_set = mandelbrot_set.reshape((height, width))
    # plot_mandelbrot(mandelbrot_set)
