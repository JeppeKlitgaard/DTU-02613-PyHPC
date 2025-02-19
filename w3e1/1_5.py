from time import perf_counter as timer

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

MIN = 2
MAX = 8
SIZES = np.logspace(MIN, MAX, 16, endpoint=True)
REPETITIONS = 250

data = []
for size in SIZES:
    size = int(round(size))
    mat = np.random.rand(1, size)

    t_row = timer()
    for _ in range(REPETITIONS):
        2 * mat[0, :]
    dt_row = timer() - t_row

    mflops_row = mat.shape[1] / (10**6 * dt_row)
    size_kb = 8 * mat.size / 1000

    data.append({
        "size": size,
        "size_kb": size_kb,
        "dt_row": dt_row,
        "mflops_row": mflops_row,
    })

    print(f"{size=}, {dt_row=}")

df = pd.DataFrame(data)
df_melted = pd.melt(df, id_vars=["size_kb"], value_vars=["mflops_row"])

plt.figure()
sns.lineplot(data=df_melted, x="size_kb", y="value", hue="variable")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Matrix Size, $S$ [KB]")
plt.ylabel("Computational Throughput, $t$ [MFLOPS]")
plt.tight_layout()
plt.savefig("1_5_1.png")
