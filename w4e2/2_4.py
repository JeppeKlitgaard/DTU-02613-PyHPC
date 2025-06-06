import line_profiler
import sys
import numpy as np

# Optimised version of 1-loop

@line_profiler.profile
def distance_matrix(p1, p2):
    p1, p2 = np.radians(p1), np.radians(p2)
    assert p1.shape == p2.shape
    # shape[0] = N: Which point this is
    # shape[1] = 2: latitude/longitude

    # UNOPTIMIZED, 2-LOOP
    # D = np.empty((len(p1), len(p2)))
    # for i in range(len(p1)):
    #     for j in range(len(p2)):
    #         dsin2 = np.sin(0.5 * (p1[i] - p2[j])) ** 2
    #         cosprod = np.cos(p1[i, 0]) * np.cos(p2[j, 0])
    #         a = dsin2[0] + cosprod * dsin2[1]
    #         D[i, j] = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    D = np.empty((len(p1), len(p2)))
    cos_lat_1 = np.cos(p1[:, 0])
    cos_lat_2 = np.cos(p2[:, 0])
    for i in range(len(p1)):
        delta_p = p1[i] - p2[:] #  (N, 2)
        delta_sin2 = np.sin(0.5 * (delta_p)) ** 2
        delta_sin22_lat = delta_sin2[:, 0]  # (N,)
        # print(f"{delta_sin22_lat.shape=}")
        delta_sin22_long = delta_sin2[:, 1]  # (N,)
        a = delta_sin22_lat + cos_lat_1[i] * cos_lat_2 * delta_sin22_long
        D[i, :] = 2 * np.arcsin(np.sqrt(a))

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
# fname = "/dtu/projects/02613_2025/data/locations/locations_100.csv"
points = load_points(fname)
D = distance_matrix(points, points)
stats = distance_stats(D)
print(stats)