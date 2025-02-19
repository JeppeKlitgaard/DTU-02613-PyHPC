from time import perf_counter as timer

import numpy as np

SIZES = np.logspace(1, 4.5, 8, endpoint=True)
REPETITIONS = 10000


for size in SIZES:
    size = int(round(size))
    mat = np.random.rand(size, size)

    t_col = timer()
    for _ in range(REPETITIONS):
        2 * mat[:, 0]
    dt_col = timer() - t_col

    t_row = timer()
    for _ in range(REPETITIONS):
        2 * mat[0, :]
    dt_row = timer() - t_row

    print(f"{size=}, {dt_row=}, {dt_col=}")
