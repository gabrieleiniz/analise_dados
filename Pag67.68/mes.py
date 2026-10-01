import pandas as pd

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])

df["mes"] = df["data"].dt.month

print(df)