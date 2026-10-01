import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

df["faturamento"] = df["quantidade"] * df["preco_unitario"]

resultado = df.groupby("regiao")["faturamento"].sum()

plt.pie(
    resultado,
    labels=resultado.index,
    autopct="%1.1f%%"
)

plt.title("Distribuição do Faturamento por Região")

plt.savefig("faturamento_por_regiao.png")
plt.show()