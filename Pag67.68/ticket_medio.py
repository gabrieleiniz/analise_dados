import pandas as pd

df = pd.read_csv("vendas.csv")

df["faturamento"] = df["quantidade"] * df["preco_unitario"]

faturamento = df.groupby("loja")["faturamento"].sum()
vendas = df.groupby("loja").size()

ticket_medio = faturamento / vendas

print(ticket_medio)