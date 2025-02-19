import numpy as np
from numpy.linalg import matrix_power
import sys
from time import perf_counter


if __name__ == "__main__":
    # Generate test case
    if len(sys.argv) > 3:
        arr = np.asarray([[1, 3], [5, 7]])
        np.save("2_5_in.npy", arr)

    t_start = perf_counter()

    fn = sys.argv[1]
    p = int(sys.argv[2])

    mat = np.load(fn)

    mat_out = matrix_power(mat, p+1)

    t_stop = perf_counter()

    np.save("2_5_out.npy", mat_out)
    print(t_stop - t_start)
