import numpy as np
from numba import jit
from time import perf_counter as timer

def matmul(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C


np.random.seed(1)
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)
matmul(A, B)

t_start = timer()
matmul(A, B)
print(timer() - t_start)

