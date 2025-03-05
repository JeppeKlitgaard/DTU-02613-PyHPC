import line_profiler
import sys
import numpy as np

@line_profiler.profile
def distance_matrix(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)
    assert p1.shape == p2.shape
    N = p1.shape[0]
    # shape[0] = N: Which point this is
    # shape[1] = 2: latitude/longitude

    D = np.empty((N, N))
    p1_tiled = np.tile(p1[:, None, :], (1, N, 1))
    p2_tiled = np.tile(p2[None, :, :], (N, 1, 1))

    delta_lat = p1_tiled[:, :, 0] - p2_tiled[:, :, 0]
    delta_long = p1_tiled[:, :, 1] - p2_tiled[:, :, 1]

    delta_sin22_lat = np.sin(0.5 * delta_lat) ** 2
    delta_sin22_long = np.sin(0.5 * delta_long) ** 2

    cos_lat_1 = np.cos(p1[:, 0])  # (N,)
    cos_lat_2 = np.cos(p2[:, 0])  # (N,)

    a = delta_sin22_lat + cos_lat_1[:, None] * cos_lat_2 * delta_sin22_long

    D = 2 * np.arcsin(np.sqrt(a))
    D *= 6371  # Earth radius in km

    return D


def load_points(fname):
    data = np.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = np.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix(points, points)
stats = distance_stats(D)
print(stats)