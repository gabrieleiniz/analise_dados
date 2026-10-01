import pandas as pd

df = pd.read_csv("vendas.csv")

df["faturamento"] = df["quantidade"] * df["preco_unitario"]

print(df)