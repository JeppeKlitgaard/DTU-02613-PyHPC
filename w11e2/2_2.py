import sys
from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

EXERCISE_DIR = Path(__file__).resolve().parent

if __name__ == "__main__":
    subhist_paths = list(EXERCISE_DIR.glob("subhist_*.npy"))

    subhist_arrs = []
    for path in subhist_paths:
        subhist_arr = np.load(path)
        subhist_arrs.append(subhist_arr)

    arrs = np.asarray(subhist_arrs)

    hist = np.sum(arrs, axis=0)

    x = np.linspace(0, 255, 64 + 1)

    rs = []
    for i in range(len(x) - 1):
        r = f"[{x[i]:.2f}, {x[i + 1]:.2f}]"
        rs.append(r)

    plt.figure(figsize=(20, 10))
    plt.bar(rs, hist)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.xlabel("Hue")
    plt.ylabel("Count")
    plt.title("Hue Histogram")
    plt.savefig("huehist.png", bbox_inches="tight")