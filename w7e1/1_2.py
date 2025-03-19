from pathlib import Path
import pandas as pd

CSV_PATH = Path("/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip")

df = pd.read_csv(CSV_PATH)

def reduce_dmi_df(df):
    df_out = df.copy()
    df_out["created"] = pd.to_datetime(df_out["created"], format="ISO8601")
    df_out["observed"] = pd.to_datetime(df_out["observed"], format="ISO8601")
    df_out["parameterId"] = df["parameterId"].astype("category")

    return df_out


def summarize_columns(df):
    print(
        pd.DataFrame(
            [
                (
                    c,
                    df[c].dtype,
                    len(df[c].unique()),
                    df[c].memory_usage(deep=True) // (1024**2),
                )
                for c in df.columns
            ],
            columns=["name", "dtype", "unique", "size (MB)"],
        )
    )
    print("Total size:", df.memory_usage(deep=True).sum() / 1024**2, "MB")

print(summarize_columns(df))
print(summarize_columns(reduce_dmi_df(df)))
