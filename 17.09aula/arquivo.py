import pandas as pd

# 1. Ler as três tabelas separadamente
t2012 = pd.read_csv("Tabela5-sem_emprego_2012.csv", sep=";", decimal=",")
t2026 = pd.read_csv("Tabela5-sem_emprego_2026.csv", sep=";", decimal=",")
t_ibge = pd.read_excel("Tabela 1.1.1.xlsx", sheet_name="2022", header=None)

# 2. Juntar as Tabelas 5 de 2012 e 2026
comp = t2012.merge(
    t2026,
    on=["Sigla", "Código", "Estado"],
    how="inner"
)

# 3. Organizar a tabela do IBGE
ibge = t_ibge.iloc[8:, [0, 1, 5]].copy()
ibge.columns = [
    "Estado",
    "Horas domésticas - total (2022)",
    "Horas domésticas - mulheres (2022)"
]

ibge = ibge[ibge["Estado"].notna()]
ibge = ibge[~ibge["Estado"].isin(
    ["Brasil", "Norte", "Nordeste", "Sudeste",
     "Sul", "Centro-Oeste"]
)]

# 4. Juntar o resultado das Tabelas 5 com a tabela do IBGE
resultado = comp.merge(
    ibge,
    on="Estado",
    how="left"
)

# 5. Mostrar a tabela final
print(resultado)

# 6. Salvar o resultado gerado pelo código
resultado.to_csv(
    "resultado_final.csv",
    index=False,
    sep=";",
    decimal=","
)
