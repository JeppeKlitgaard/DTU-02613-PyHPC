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
    # elemshape: shape of image

    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b] = np.sum(arr[b:e:s], axis=0)


if __name__ == "__main__":
    # Load data
    n_proc = int(sys.argv[1])
    n_run = int(sys.argv[2])
    data_path = sys.argv[3]
    data = np.load(data_path)

    # Create shared array
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    # Run parallel sum
    t = time()
    pool = mp.Pool(n_proc, initializer=init, initargs=(shared_arr,))

    c = 1000
    s = 1
    Ni = int(np.ceil(np.log2(len(arr))))
    for i in range(0, Ni):
        pool.map(
            reduce_step,
            [(b, b + c * s, s, elemshape) for b in range(0, len(arr), c*s)],
            chunksize=1,
        )

        s *= c

    # Write output
    timed = time() - t
    print(f"{n_proc}\t{n_run}\t{timed}")

    final_image = arr[0]
    final_image /= len(arr) # For mean
    Image.fromarray((255 * final_image.astype(float)).astype("uint8")).save(
        "result.png"
    )



# uv run 1_1.py /dtu/projects/02613_2025/data/celeba/celeba_200.npy