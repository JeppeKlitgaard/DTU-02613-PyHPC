from pyarrow import csv

def pyarrow_load(fname):
    table = csv.read_csv(fname)
    return table.to_pandas()
