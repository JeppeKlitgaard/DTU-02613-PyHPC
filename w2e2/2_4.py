import numpy as np
import sys


if __name__ == "__main__":
    fn = sys.argv[1]
    mat = np.load(fn)

    mean_cols = np.mean(mat, axis=0)
    mean_rows = np.mean(mat, axis=1)

    np.save("cols.npy", mean_cols)
    np.save("rows.npy", mean_rows)
