import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

sns.boxplot(
    data=df,
    x="categoria",
    y="preco_unitario"
)

plt.title("Distribuição de Preços por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Preço Unitário")

plt.savefig("boxplot.png")
plt.show()