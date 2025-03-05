import numpy as np

def distmat_1d(x, y):
    #D_ij = |x_i - y_j|
    x_ = x[:, None]
    y_ = y[:, None].T
    D = x_ - y_
    return np.abs(D)

x = np.asarray([1, 2])
y = np.asarray([3, 0.5, 1])
print(distmat_1d(x, y))