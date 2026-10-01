import pandas as pd

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

df["mes"] = df["data"].dt.strftime("%m/%Y")

faturamento_mes = df.groupby("mes")["faturamento"].sum()

maior = faturamento_mes.idxmax()
menor = faturamento_mes.idxmin()

print("Maior faturamento:", maior)
print("Menor faturamento:", menor)