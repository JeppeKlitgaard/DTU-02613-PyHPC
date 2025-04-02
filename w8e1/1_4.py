import sys
from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq


if __name__ == "__main__":
    parquet_path = Path(sys.argv[1])
    assert parquet_path.exists()

    pf = pq.ParquetFile(parquet_path)

    total_precip = 0.0
    for i in range(pf.num_row_groups):
        df = pf.read_row_group(i).to_pandas()
        total_precip += df[df["parameterId"] == "precip_past10min"]["value"].sum()

    print(total_precip)