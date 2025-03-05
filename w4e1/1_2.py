def outer(a, b):
    return a[:, None] * b[:, None].T

# import numpy as np

# a = np.asarray([1,2])
# b = np.asarray([3, 4, 5])

# c = outer(a, b)
