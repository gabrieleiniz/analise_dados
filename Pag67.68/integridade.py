import pandas as pd

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])

print(df.info())
print(df.isnull().sum())
print(df.describe())