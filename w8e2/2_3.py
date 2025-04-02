import numpy as np
import sys
from pathlib import Path
import matplotlib.pyplot as plt


if __name__ == "__main__":
    arr_path = Path(sys.argv[1])
    assert arr_path.exists()

    N = int(sys.argv[2])
    n = int(sys.argv[3])

    mm_arr = np.memmap(arr_path, mode="r", dtype="int32", shape=(N, N))

    downsampled = mm_arr[::n, ::n]

    plt.imsave("2_3.png", downsampled, cmap="hot")
