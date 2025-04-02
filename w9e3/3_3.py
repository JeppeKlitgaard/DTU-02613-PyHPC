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

def get_bpg(n, tpb):
    return (n + (tpb - 1)) // tpb

tpb = 16
bpg = 16
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