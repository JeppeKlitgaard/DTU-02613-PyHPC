from time import perf_counter as timer

import numpy as np

SIZE = 10000
REPETITIONS = 25000


mat = np.random.rand(SIZE, SIZE)

t1 = timer()
for _ in range(REPETITIONS):
    2 * mat[:, 0]
dt1 = timer() - t1

t2 = timer()
for _ in range(REPETITIONS):
    2 * mat[0, :]
dt2 = timer() - t2

print(f"{dt1=}, {dt2=}")

# dt1 > dt2 as expected