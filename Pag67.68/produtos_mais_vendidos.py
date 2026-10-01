import pandas as pd

df = pd.read_csv("vendas.csv")

produtos = df.groupby("produto")["quantidade"].sum()

produtos = produtos.sort_values(ascending=False).head(5)

print(produtos)