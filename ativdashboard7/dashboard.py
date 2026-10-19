
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from models.dados import carregar_grafico

st.set_page_config(
    page_title="Dashboard - Indicador 7",
    page_icon="📊",
    layout="wide"
)

sns.set_theme(style="whitegrid")

st.title("Dashboard - Indicador 7")
st.subheader(
    "Meios de transporte utilizados por mulheres segundo cor/raça"
)
st.write("Dados referentes ao ano de 2022.")

# Carregar os dados
df = carregar_grafico()

# Verificar os dados
if df is None or df.empty:
    st.error("Não foi possível carregar os dados.")
    st.stop()

st.sidebar.header("Filtros")

# Selecionar a cor ou raça
grupos = ["Branca", "Preta ou Parda", "Indígena"]

grupo = st.sidebar.selectbox(
    "Selecione a cor/raça:",
    grupos
)

# Indicadores principais
col1, col2 = st.columns(2)

col1.metric("Grupo selecionado", grupo)
col2.metric("Meios de transporte", len(df))

st.divider()

# Gráfico de barras
st.subheader("Comparação dos meios de transporte")

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=df,
    x="Meio de Transporte",
    y=grupo,
    ax=ax,
    color="steelblue"
)

ax.set_title(f"Meios de transporte - {grupo}")
ax.set_xlabel("Meio de transporte")
ax.set_ylabel("Percentual (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Gráfico de pizza
st.subheader("Distribuição percentual")

fig, ax = plt.subplots(figsize=(8, 5))

ax.pie(
    df[grupo],
    labels=df["Meio de Transporte"],
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title(f"Distribuição dos transportes - {grupo}")
st.pyplot(fig)
plt.close(fig)

# Tabela de dados
st.subheader("Tabela de dados")

st.dataframe(
    df[["Meio de Transporte"] + grupos],
    use_container_width=True
)
