import datetime as data
import streamlit as st
import pandas as pd

# Definir a data atual
today = data.date.today()

# Calcular a data de 18 anos atrás
min_date = today - data.timedelta(days=18*365)

def gravar_dados(nome, nasc_dat, tipo, id):
    if nome and nasc_dat <= min_date:
        if tipo == "Pessoa Fisica":
           with open("Clientes.csv","a",encoding="utf-8") as file:
               file.write(f"{nome},{nasc_dat},{tipo},,{id}\n")
        else:
           with open("Clientes.csv","a",encoding="utf-8") as file:
               file.write(f"{nome},{nasc_dat},{tipo},{id},\n")
        st.session_state["gravar"] = True
    else:
        st.session_state["gravar"] = False

st.set_page_config(
    page_title="Cadastro",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    }
)

st.header("Cadastro de Cliente")
st.divider()

nome = st.text_input("Digite o nome do cliente:",
                    key="name_client")
nasc_dat = st.date_input("Data de Nascimento:",
                         format="DD/MM/YYYY",
                         min_value= data.date(1924, 1, 1),
                         key="data_nasc")
tipo = st.selectbox("Tipo de cliente:",
                    ["Pessoa Fisica", "Pessoa Juridica"],
                    index=None,
                    key="tipo_Cl")
if tipo == "Pessoa Fisica":
    id = st.text_input("Digite o CPF:",
                         key="cpf",
                         max_chars=11)
    id = id[:3]+"."+id[3:6]+"."+id[6:9]+"-"+id[9:]
    st.text(id)
elif tipo == "Pessoa Juridica":
    id = st.text_input("Digite o CNPJ:",
                         key="cnpj",
                         max_chars=14)
    id=id[:2]+"."+id[2:5]+"."+id[5:8]+"/"+id[8:12]+"-"+id[12:14]
    st.text(id)

btn_bot = st.button("Cadastrar",
                    on_click=gravar_dados,
                    args=[nome, nasc_dat, tipo, id])

if btn_bot:
    if st.session_state["gravar"]:
        st.success("Cadastro realizado com sucesso!",
                   icon="✔")
    else:
        st.success("Cadastro com idade menor que 18 anos!",
                   icon="❌")