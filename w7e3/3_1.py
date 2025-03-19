from pyarrow import parquet, csv
from pathlib import Path
import sys


def load_csv_save_parquet(fn):
    from_path = Path(fn)
    to_path = from_path.stem + ".parquet"

    table = csv.read_csv(from_path)
    parquet.write_table(table, to_path)


if __name__ == "__main__":
    fn = sys.argv[1]
    load_csv_save_parquet(fn)