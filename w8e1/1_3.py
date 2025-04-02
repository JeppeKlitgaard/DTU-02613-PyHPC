from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

DF_IN = Path("/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip")
DF_OUT = Path(__file__).resolve().parent / "1_3.parquet"
CHUNK_SIZE = 100_000

if __name__ == "__main__":
    dfc = pd.read_csv(DF_IN, chunksize=CHUNK_SIZE)

    first = True
    writer = None

    for chunk in dfc:
        chunk_table = pa.Table.from_pandas(chunk)
        schema = chunk_table.schema
        if first:
            first = False
            writer = pq.ParquetWriter(DF_OUT, schema=schema)

        writer.write_table(chunk_table)
    writer.close()