import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")

numericas = df.select_dtypes(include="number")

correlacao = numericas.corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlacao,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlação entre Variáveis Numéricas")

plt.savefig("heatmap.png")
plt.show()