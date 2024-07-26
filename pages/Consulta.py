import streamlit as st
import pandas as pd

dados = pd.read_csv("Clientes.csv")

st.set_page_config(
    page_title="Consulta",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    }
)

st.title("Clientes Cadastrados")
st.divider()

st.dataframe(dados)