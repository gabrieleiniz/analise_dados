import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

mensal = df.groupby(
    df["data"].dt.to_period("M")
)["faturamento"].sum()

plt.plot(mensal.index.astype(str), mensal.values, marker="o")

for i, valor in enumerate(mensal.values):
    plt.text(i, valor, f"{valor:.2f}")

plt.title("Evolução Mensal do Faturamento")
plt.xlabel("Mês")
plt.ylabel("Faturamento")

plt.xticks(rotation=45)

plt.savefig("evolucao_mensal.png")
plt.show()