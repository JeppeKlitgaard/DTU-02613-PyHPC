from numba import cuda
import numpy as np
from time import perf_counter as timer

def matmul(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C


@cuda.jit
def matmul_kernel(A, B, C):
    i, j = cuda.grid(2)

    for k in range(A.shape[1]):
        C[i, j] += A[i, k] * B[k, j]

N = 2048
np.random.seed(1)
A = np.random.rand(N, N)
B = np.random.rand(N, N)
C = cuda.device_array_like(B)

def get_bpg(N, tpb):
    if isinstance(tpb, tuple):
        bpg = []
        for n, d in zip(N, tpb):
            bpg.append((n + (d - 1)) // d)

        return tuple(bpg)

tpb = (1, 256)
bpg = get_bpg(A.shape, tpb)

print(tpb, bpg)
matmul_kernel[bpg, tpb](A, B, C)


with cuda.pinned(A, B):
    t = timer()
    for _ in range(100):
        matmul_kernel[bpg, tpb](A, B, C)
    cuda.synchronize() # Ensure all kernels are done
    t_delta = timer() - t
    print("CUDA", t_delta)

# t = timer()
# for _ in range(100):
#     C = A @ B
# cuda.synchronize() # Ensure all kernels are done
# t_delta = timer() - t
# print("Numpy", t_delta)

#! Answer
#? tbp = (256, 1): 141.92801075498573s
#? tbp = (1, 256): 8.142590129049495s
#? This we attribute to cache locality (second run follows cache lines)
