from numba import cuda
import sys
import numpy as np

TPB = 1024  # Threads per block

@cuda.jit
def reduce_kernel(data, out, n):
    # Get the 1D grid and block indices
    tid = cuda.threadIdx.x
    i = cuda.grid(1)

    # Do reduction for threadblock
    s = 1
    while s < cuda.blockDim.x:
        if tid % (2 * s) == 0 and i + s < n:
            data[i] += data[i + s]
        s *= 2
        cuda.syncthreads()  # Ensure block is synchronized

    # Write result for this block to global memory
    if tid == 0:
        out[cuda.blockIdx.x] = data[i]

def get_grid(n, tpb):
    return (n + (tpb - 1)) // tpb  # Blocks per grid

def reduce(x):
    n = len(x)
    bpg = get_grid(n, TPB)
    d_x = cuda.to_device(x)
    out = cuda.device_array(bpg, dtype=x.dtype)
    while bpg > 1:
        reduce_kernel[bpg, TPB](d_x, out, n)
        n = bpg
        bpg = get_grid(n, TPB)
        d_x[:n] = out[:n]
    reduce_kernel[bpg, TPB](d_x, out, n)
    cuda.synchronize()  # Ensure all kernels are done
    out = out.copy_to_host()  # Copy result back to host
    return out[0]


if __name__ == "__main__":
    n = int(sys.argv[1])

    x = np.random.rand(n).astype(np.float32)

    sum_ = reduce(x.copy())
    print(sum_)