import multiprocessing
import numpy as np
import matplotlib.pyplot as plt


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


def generate_mandelbrot_set_chunks(points, num_processes):
    chunks = np.array_split(points, num_processes)

    pool = multiprocessing.Pool(num_processes)
    results_async = [pool.apply_async(chunk_processor, (chunk,)) for chunk in chunks]
    arrs = [r.get() for r in results_async]
    escape_times = np.concatenate(arrs)
    return escape_times


def plot_mandelbrot(escape_times):
    plt.imshow(escape_times, cmap="hot", extent=(-2, 2, -2, 2))
    plt.axis("off")
    plt.savefig("mandelbrot.png", bbox_inches="tight", pad_inches=0)


if __name__ == "__main__":
    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = 4

    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])

    # Compute set
    mandelbrot_set = generate_mandelbrot_set_chunks(points, num_proc)

    # Save set as image
    mandelbrot_set = mandelbrot_set.reshape((height, width))
    plot_mandelbrot(mandelbrot_set)
