import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

df["data"] = pd.to_datetime(df["data"])
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

lojas = df.groupby("loja")["faturamento"].sum()

mensal = df.groupby(
    df["data"].dt.to_period("M")
)["faturamento"].sum()

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].bar(lojas.index, lojas.values)
ax[0].set_title("Faturamento por Loja")
ax[0].set_xlabel("Loja")
ax[0].set_ylabel("Faturamento")

ax[1].plot(
    mensal.index.astype(str),
    mensal.values,
    marker="o"
)

ax[1].set_title("Faturamento Mensal")
ax[1].set_xlabel("Mês")
ax[1].set_ylabel("Faturamento")

plt.tight_layout()
plt.savefig("layout_graficos.png")
plt.show()