from numba import cuda
import numpy as np
from time import perf_counter as timer

@cuda.jit
def add_kernel(x, y, out):
    i = cuda.grid(1)

    if i < len(x):
        out[i] = x[i] + y[i]

N = 1_000_000
np.random.seed(1)
a = np.empty(N)
x = np.random.rand(N)
y = np.random.rand(N)

def get_bpg(n, tpb):
    return (n + (tpb - 1)) // tpb

tpb = 1024
bpg = get_bpg(len(x), tpb)
add_kernel[bpg, tpb](a, x, y)

