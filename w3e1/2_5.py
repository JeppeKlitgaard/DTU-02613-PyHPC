import os
import blosc
import numpy as np
import sys
from time import perf_counter as timer


def write_numpy(arr, file_name):
    np.save(f"{file_name}.npy", arr)
    os.sync()


def write_blosc(arr, file_name, cname="zstd"):
    b_arr = blosc.pack_array(arr, cname=cname)
    with open(f"{file_name}.bl", "wb") as w:
        w.write(b_arr)
    os.sync()


def read_numpy(file_name):
    return np.load(f"{file_name}.npy")


def read_blosc(file_name):
    with open(f"{file_name}.bl", "rb") as r:
        b_arr = r.read()
    return blosc.unpack_array(b_arr)

if __name__ == "__main__":
    assert len(sys.argv) == 2
    n = int(sys.argv[1])

    arr = np.tile(
        np.arange(256, dtype='uint8'),
        (n // 256) * n * n,
    ).reshape(n, n, n)

    t = timer()
    write_numpy(arr, "numpy")
    t_write_numpy = timer() - t
    print(t_write_numpy)

    t = timer()
    write_blosc(arr, "blosc")
    t_write_blosc = timer() - t
    print(t_write_blosc)

    t = timer()
    arr = read_numpy("numpy")
    t_read_numpy = timer() - t
    print(t_read_numpy)

    t = timer()
    arr = read_blosc("blosc")
    t_read_blosc = timer() - t
    print(t_read_blosc)
