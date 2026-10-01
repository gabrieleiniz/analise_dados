import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

df["faturamento"] = df["quantidade"] * df["preco_unitario"]

sns.scatterplot(
    data=df,
    x="quantidade",
    y="faturamento"
)

plt.title("Relação entre Quantidade e Faturamento")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Faturamento")

plt.savefig("dispersao.png")
plt.show()