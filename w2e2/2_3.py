import numpy as np
import sys


if __name__ == "__main__":
    arr = np.array(list(map(float, sys.argv[1:])))
    mat = np.identity(len(arr)) * arr

    np.save("2_3_out.npy", mat)
