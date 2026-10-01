import pandas as pd

df = pd.read_csv("vendas.csv")

df["faturamento"] = df["quantidade"] * df["preco_unitario"]

resultado = df.groupby("loja")["faturamento"].sum()
resultado = resultado.sort_values(ascending=False)

print(resultado)