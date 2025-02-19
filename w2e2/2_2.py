import numpy as np
from numpy.linalg import norm
import sys

def magnitude(arr) -> float:
    return norm(arr)


if __name__ == "__main__":
    arr = np.array(list(map(float, sys.argv[1:])))
    print(magnitude(arr))
