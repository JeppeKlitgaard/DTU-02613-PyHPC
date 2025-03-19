import pandas as pd
from pyarrow import csv
import sys
from pathlib import Path

if __name__ == "__main__":
    fn = sys.argv[1]
    from_path = Path(fn)

    df = csv.read_csv(from_path).to_pandas()

    print(df[df["parameterId"] == "precip_past10min"]["value"].sum())
