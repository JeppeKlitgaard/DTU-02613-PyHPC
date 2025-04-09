# import numpy as cp
import cupy as cp
import sys

def distance_matrix_oneloop_given(p1, p2):
    p1 = cp.radians(p1)
    p2 = cp.radians(p2)

    D = cp.empty((len(p1), len(p2)))
    for i in range(len(p1)):
        dsin2 = cp.sin(0.5 * (p1[i] - p2)) ** 2
        cosprod = cp.cos(p1[i, 0]) * cp.cos(p2[:, 0])
        a = dsin2[:, 0] + cosprod * dsin2[:, 1]
        row = 2 * cp.arctan2(cp.sqrt(a), cp.sqrt(1 - a))
        D[i, :] = row

    D *= 6371  # Earth radius in km
    return D

def distance_matrix_noloop_given(p1, p2):
    p1 = cp.radians(p1)
    p2 = cp.radians(p2)
    dsin2 = cp.sin(0.5 * (p1[:, None, :] - p2[None, :, :])) ** 2
    cosprod = cp.cos(p1[:, None, 0]) * cp.cos(p2[None, :, 0])
    D = 2 * cp.arcsin(cp.sqrt(dsin2[:, :, 0] + cosprod * dsin2[:, :, 1]))
    D *= 6371  # Earth radius in km
    return D


def distance_matrix_oneloop(p1, p2):
    p1, p2 = cp.radians(p1), cp.radians(p2)
    assert p1.shape == p2.shape

    D = cp.empty((len(p1), len(p2)))
    cos_lat_1 = cp.cos(p1[:, 0])
    cos_lat_2 = cp.cos(p2[:, 0])
    for i in range(len(p1)):
        delta_p = p1[i] - p2[:] #  (N, 2)
        delta_sin2 = cp.sin(0.5 * (delta_p)) ** 2
        delta_sin22_lat = delta_sin2[:, 0]  # (N,)
        delta_sin22_long = delta_sin2[:, 1]  # (N,)
        a = delta_sin22_lat + cos_lat_1[i] * cos_lat_2 * delta_sin22_long
        D[i, :] = 2 * cp.arcsin(cp.sqrt(a))

    D *= 6371  # Earth radius in km
    return D



def distance_matrix_noloop(p1, p2):
    p1, p2 = cp.radians(p1), cp.radians(p2)
    assert p1.shape == p2.shape
    N = p1.shape[0]
    # shape[0] = N: Which point this is
    # shape[1] = 2: latitude/longitude

    D = cp.empty((N, N))
    # This should have been avoided. Makes it substantially slower and is not needed
    # It does copy, not view I guess
    p1_tiled = cp.tile(p1[:, None, :], (1, N, 1))
    p2_tiled = cp.tile(p2[None, :, :], (N, 1, 1))

    delta_lat = p1_tiled[:, :, 0] - p2_tiled[:, :, 0]
    delta_long = p1_tiled[:, :, 1] - p2_tiled[:, :, 1]

    delta_sin22_lat = cp.sin(0.5 * delta_lat) ** 2
    delta_sin22_long = cp.sin(0.5 * delta_long) ** 2

    cos_lat_1 = cp.cos(p1[:, 0])  # (N,)
    cos_lat_2 = cp.cos(p2[:, 0])  # (N,)

    a = delta_sin22_lat + cos_lat_1[:, None] * cos_lat_2 * delta_sin22_long

    D = 2 * cp.arcsin(cp.sqrt(a))
    D *= 6371  # Earth radius in km

    return D


def load_points(fname):
    data = cp.loadtxt(fname, delimiter=',', skiprows=1, usecols=(1, 2))
    return data


def distance_stats(D):
    # Extract upper triangular part to avoid duplicate entries
    assert D.shape[0] == D.shape[1], 'D must be square'
    idx = cp.triu_indices(D.shape[0], k=1)
    distances = D[idx]
    return {
        'mean': float(distances.mean()),
        'std': float(distances.std()),
        'max': float(distances.max()),
        'min': float(distances.min()),
    }


fname = sys.argv[1]
points = load_points(fname)
D = distance_matrix_noloop(points, points)
stats = distance_stats(D)
print(stats)