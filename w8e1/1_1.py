import sys
from pathlib import Path
import pandas as pd


if __name__ == "__main__":
    pandas_path = Path(sys.argv[1])
    assert pandas_path.exists()

    chunk_size = int(sys.argv[2])

    dfc = pd.read_csv(pandas_path, chunksize=chunk_size)
    total_precip = 0.0
    for df in dfc:
        total_precip += df[df["parameterId"] == "precip_past10min"]["value"].sum()

    print(total_precip)