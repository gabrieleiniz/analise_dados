import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

df["faturamento"] = df["quantidade"] * df["preco_unitario"]

resultado = df.groupby("loja")["faturamento"].sum()

plt.bar(resultado.index, resultado.values)

plt.title("Faturamento por Loja")
plt.xlabel("Nome da Loja")
plt.ylabel("Valor do Faturamento")

plt.tight_layout()
plt.show()