import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="Set2")

regioes = ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"]

estados = indicador_1[
    ~indicador_1["uf_regiao"].isin(["Brasil"] + regioes)
].copy()

# GRAFICO 1 - BARRAS HORIZONTAIS

fig, ax = plt.subplots(figsize=(9, 8))

ordem = estados.sort_values("total", ascending=False)

sns.barplot(
    data=ordem,
    y="uf_regiao",
    x="total",
    ax=ax,
    color="steelblue"
)

ax.axvline(
    media_nacional,
    color="crimson",
    linestyle="--",
    label=f"Média Brasil ({media_nacional:.1f} h)"
)

ax.set_title("Horas semanais de afazeres domésticos por UF")
ax.set_xlabel("Horas / semana")
ax.set_ylabel("UF")
ax.legend()

plt.tight_layout()
plt.show()


# GRAFICO 2 - HOMENS X MULHERES POR REGIAO

reg = indicador_1[
    indicador_1["uf_regiao"].isin(regioes)
].copy()

reg["homens"] = (
    reg["homem_branca"] + reg["homem_preta_parda"]
) / 2

reg["mulheres"] = (
    reg["mulher_branca"] + reg["mulher_preta_parda"]
) / 2

reg_long = reg.melt(
    id_vars="uf_regiao",
    value_vars=["homens", "mulheres"],
    var_name="sexo",
    value_name="horas"
)

fig, ax = plt.subplots(figsize=(9, 5))

sns.barplot(
    data=reg_long,
    x="uf_regiao",
    y="horas",
    hue="sexo",
    ax=ax
)

ax.set_title("Afazeres domésticos por região e sexo")
ax.set_xlabel("Região")
ax.set_ylabel("Horas / semana")

plt.tight_layout()
plt.show()


# GRAFICO 3 - HISTOGRAMA E BOXPLOT

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(
    estados["total"],
    bins=8,
    kde=True,
    ax=axes[0]
)

axes[0].axvline(
    media_nacional,
    color="crimson",
    linestyle="--"
)

axes[0].set_title("Frequência das horas médias por UF")
axes[0].set_xlabel("Horas / semana")
axes[0].set_ylabel("Número de UFs")

sns.boxplot(
    y=estados["total"],
    ax=axes[1]
)

axes[1].axhline(
    media_nacional,
    color="crimson",
    linestyle="--"
)

axes[1].set_title("Box plot das horas por UF")
axes[1].set_ylabel("Horas / semana")

plt.tight_layout()
plt.show()


# GRAFICO 4 - BOXPLOT POR SEXO E COR

box_df = estados[
    [
        "homem_branca",
        "homem_preta_parda",
        "mulher_branca",
        "mulher_preta_parda"
    ]
].melt(
    var_name="grupo",
    value_name="horas"
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.boxplot(
    data=box_df,
    x="grupo",
    y="horas",
    ax=ax
)

ax.set_title("Distribuição das horas por sexo e cor (UFs)")
ax.set_xlabel("Grupo")
ax.set_ylabel("Horas / semana")

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()