import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time
import numpy as np
from PIL import Image


def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_


def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype="float32")


def reduce_step(args):
    b, e, s, elemshape = args
    # b: begin index
    # e: end index
    # s: stepsize
    # elemshape: chunk size?

    # print(f"{b=}, {e=}, {s=}")
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    # print(arr)
    # print(args)
    # print(arr.shape)
    # Change the code below to compute a step of the reduction
    # ---------------------------8<---------------------------
    # print(arr[b])
    arr[b] = np.sum(arr[b:e:s], axis=0)
    # print(arr[b:e:s])
    # print(arr[b])
    # print(arr[:])

    # arr[b:e:s] = 1.0 - arr[b:e:s]  # <-- Dummy op. Replace with correct


if __name__ == "__main__":
    n_processes = 1
    chunk = 2

    # Create shared array
    data_path = sys.argv[1]
    data = np.load(data_path)
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run parallel sum
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))

    # Change the code below to compute a step of the reduction
    # ---------------------------8<---------------------------
    c = 2
    s = 1
    Ni = int(np.ceil(np.log2(len(arr))))
    for i in range(0, Ni):
        print(f"{i=}")
        pool.map(
            reduce_step,
            [(b, b + c * s, s, elemshape) for b in range(0, len(arr), c*s)],
            chunksize=1,
        )

        s *= c
        break

    # Write output
    print(time() - t)
    final_image = arr[0]
    # final_image /= len(arr) # For mean
    # print(arr)
    Image.fromarray((255 * final_image.astype(float)).astype("uint8")).save(
        "result.png"
    )


# uv run 1_1.py /dtu/projects/02613_2025/data/celeba/celeba_200.npy