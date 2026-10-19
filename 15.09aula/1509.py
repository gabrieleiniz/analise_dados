import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Tabela4.csv",
    sep=";",
    decimal=","
)

print("\n===== TABELA ORIGINAL =====")
print(df.head())


df = df.dropna(axis=1, how="all")

df.columns = df.columns.astype(str).str.strip()

print("\n===== COLUNAS =====")
print(df.columns.tolist())


df["2024"] = pd.to_numeric(df["2024"], errors="coerce")

df_ordenado = df.sort_values(
    "2024",
    ascending=False
)

print("\n===== ESTADOS ORDENADOS PELO IDH DE 2024 =====")
print(df_ordenado[["Sigla", "Estado", "2024"]].to_string(index=False))


df["1991"] = pd.to_numeric(df["1991"], errors="coerce")

df["Melhora"] = df["2024"] - df["1991"]

melhoras = df.sort_values(
    "Melhora",
    ascending=False
)

print("\n===== MELHORA DO IDH: 1991 -> 2024 =====")
print(
    melhoras[["Sigla", "Estado", "1991", "2024", "Melhora"]]
    .to_string(index=False)
)

maior_melhora = df.loc[df["Melhora"].idxmax()]

print("\n===== MAIOR MELHORA =====")
print(f"Estado: {maior_melhora['Estado']} ({maior_melhora['Sigla']})")
print(f"IDH em 1991: {maior_melhora['1991']:.3f}")
print(f"IDH em 2024: {maior_melhora['2024']:.3f}")
print(f"Melhora: {maior_melhora['Melhora']:.3f}")


piorou = df[df["Melhora"] < 0]

print("\n===== ESTADOS EM QUE O IDH PIOROU =====")

if piorou.empty:
    print("Nenhum estado apresentou piora entre 1991 e 2024.")
else:
    print(
        piorou[["Sigla", "Estado", "1991", "2024", "Melhora"]]
        .to_string(index=False)
    )


anos = [c for c in df.columns if str(c).isdigit()]

print("\n===== ANOS =====")
print(anos)

id_vars = [c for c in df.columns if c not in anos]

df_longo = df.melt(
    id_vars=id_vars,
    value_vars=anos,
    var_name="Ano",
    value_name="IDH",
)

df_longo["Ano"] = df_longo["Ano"].astype(int)


df_longo["IDH"] = pd.to_numeric(
    df_longo["IDH"],
    errors="coerce"
)

print("\n===== TABELA NO FORMATO LONGO =====")
print(df_longo.head(10).to_string(index=False))

mg = df_longo[
    df_longo["Sigla"] == "MG"
].copy()

mg = mg.sort_values("Ano")

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    mg["Ano"],
    mg["IDH"],
    marker="o",
    markersize=5,
    linewidth=2,
    label="MG"
)

ax.set_title("Evolução do IDH de Minas Gerais")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)

ax.grid(True, alpha=0.3)

ax.legend()

fig.tight_layout()

plt.show()


fig, ax = plt.subplots(figsize=(12, 7))

for sigla, grupo in df_longo.groupby("Sigla"):

    grupo = grupo.sort_values("Ano")

    ax.plot(
        grupo["Ano"],
        grupo["IDH"],
        marker="o",
        markersize=3,
        linewidth=1.5,
        label=sigla
    )

ax.set_title("Evolução do IDH por estado (1991–2024)")
ax.set_xlabel("Ano")
ax.set_ylabel("IDH")
ax.set_ylim(0.3, 0.9)

ax.legend(
    ncol=3,
    bbox_to_anchor=(1.02, 1),
    loc="upper left",
    title="UF"
)

fig.tight_layout()

plt.show()
