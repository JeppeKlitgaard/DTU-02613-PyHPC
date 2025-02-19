from time import perf_counter as timer

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

MIN = 1
MAX = 4.5
SIZES = np.logspace(MIN, MAX, 16, endpoint=True)
REPETITIONS = 2500

data = []
for size in SIZES:
    size = int(round(size))
    mat = np.random.rand(size, size)

    t_col = timer()
    for _ in range(REPETITIONS):
        2 * mat[:, 0]
    dt_col = timer() - t_col

    t_row = timer()
    for _ in range(REPETITIONS):
        2 * mat[0, :]
    dt_row = timer() - t_row

    mflops_row = mat.shape[1] / (10**6 * dt_row)
    mflops_col = mat.shape[0] / (10**6 * dt_col)
    size_kb = 8 * mat.size / 1000

    data.append({
        "size": size,
        "size_kb": size_kb,
        "dt_row": dt_row,
        "dt_col": dt_col,
        "mflops_row": mflops_row,
        "mflops_col": mflops_col,
    })

    print(f"{size=}, {dt_row=}, {dt_col=}")

df = pd.DataFrame(data)
df_melted = pd.melt(df, id_vars=["size_kb"], value_vars=["mflops_row", "mflops_col"])



plt.figure()
sns.lineplot(data=df_melted, x="size_kb", y="value", hue="variable")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Matrix Size, $S$ [KB]")
plt.ylabel("Computational Throughput, $t$ [MFLOPS]")
plt.tight_layout()
plt.savefig("1_4_1.png")

plt.figure()
df["ratio"] = df["mflops_row"] / df["mflops_col"]
sns.lineplot(data=df, x="size_kb", y="ratio")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Matrix Size, $S$ [KB]")
plt.ylabel("Ratio of Computational Throughput, $r$")
plt.tight_layout()
plt.savefig("1_4_2.png")
