import pandas as pd

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

df["mes"] = df["data"].dt.strftime("%m/%Y")

lojas = df.groupby("loja")["faturamento"].sum()
meses = df.groupby("mes")["faturamento"].sum()
produtos = df.groupby("produto")["quantidade"].sum()

resumo = pd.DataFrame({
    "informacao": [
        "Loja com maior faturamento",
        "Mês com maior faturamento",
        "Produto mais vendido"
    ],
    "resultado": [
        lojas.idxmax(),
        meses.idxmax(),
        produtos.idxmax()
    ]
})

resumo.to_csv("resumo_analitico.csv", index=False)

print(resumo)
