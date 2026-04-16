def transform(df):
    import pandas as pd

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "revenue" not in df.columns and {"sales", "price"}.issubset(df.columns):
        df["revenue"] = df["sales"] * df["price"]

    return df