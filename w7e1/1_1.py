from pathlib import Path
import pandas as pd

CSV_PATH = Path("/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip")

df = pd.read_csv(CSV_PATH)

def df_memsize(df):
    usage = df.memory_usage(deep=True)
    return usage.sum()

print(df_memsize(df))
