import pandas as pd

df = pd.read_csv("vendas.csv")

df["quantidade"] = df["quantidade"].fillna(df["quantidade"].mean())
df["preco_unitario"] = df["preco_unitario"].fillna(df["preco_unitario"].mean())

print(df)