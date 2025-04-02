import sys
import numpy as np
import matplotlib.pyplot as plt
import zarr


def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2:
            return i
    return 100


if __name__ == "__main__":
    N = int(sys.argv[1])
    C = int(sys.argv[2])

    z = zarr.open("3_1.zarr", mode="w", shape=(N, N), chunks=(C, C), dtype="int32")
    # z.empty(shape=(N, N), chunks=(C, C))

    # This is a bit dodgy since we allocate arrays here... These would ideally be generate

    xpts, ypts = np.meshgrid(
        # Add 1 to size to make it compatible with previous weeks
        np.linspace(-2, 2, N+1)[:-1],
        np.linspace(-2, 2, N+1)[:-1],
    )

    for idx in np.ndindex((N, N)):
        point = 1j * xpts[idx] + ypts[idx]
        z[idx] = mandelbrot_escape_time(point)

    # plt.imshow(z, cmap="hot", extent=(-2, 2, -2, 2))
    # plt.axis("off")
    # plt.savefig("2_1.png", bbox_inches="tight", pad_inches=0)



