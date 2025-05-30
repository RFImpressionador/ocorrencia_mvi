import streamlit as st
from components import form_vitimas, form_autores, form_testemunhas
from listar_ocorrencias import listar_ocorrencias
import datetime

# Configuração da página inicial do Streamlit
st.set_page_config(page_title="Formulário de Ocorrência", layout="wide")

# Menu lateral
menu = st.sidebar.selectbox("Menu", ["Registrar Ocorrência", "Consultar Ocorrências"])

if menu == "Registrar Ocorrência":
    # Título principal
    st.title("Formulário de Registro de Ocorrência")

    # 1. Dados Gerais
    st.header("1. Dados Gerais")
    bo_num = st.text_input("Nº do B.O.")
    data = st.date_input("Data", value=datetime.date.today())
    hora = st.time_input("Hora")
    cidade = st.text_input("Cidade")
    local = st.text_area("Local do Fato")

    # 2. Vítimas (usando componente modularizado)
    vitimas = form_vitimas.exibir_formulario()

    # 3. Autores (usando componente modularizado)
    autores = form_autores.exibir_formulario()

    # 4. Descrição dos Fatos
    st.header("4. Descrição dos Fatos")
    descricao = st.text_area("Narrativa dos Fatos", height=200)

    # 5. Motivação Provável
    st.header("5. Motivação Provável")
    motivacao = st.text_area("Motivação", height=100)

    # 6. Testemunhas (usando componente modularizado)
    testemunhas = form_testemunhas.exibir_formulario()

    # 7. Anexos / Observações Finais
    st.header("7. Anexos / Observações Finais")
    obs_finais = st.text_area("Observações Finais", height=100)

    # Botão para enviar
    if st.button("Enviar"):
        dados = {
            "bo_num": bo_num,
            "data": str(data),
            "hora": str(hora),
            "cidade": cidade,
            "local": local,
            "vitimas": vitimas,
            "autores": autores,
            "descricao": descricao,
            "motivacao": motivacao,
            "testemunhas": testemunhas,
            "obs_finais": obs_finais
        }

        st.success("Dados coletados com sucesso! Veja o JSON abaixo:")
        st.json(dados)

        # Futuro: salvar os dados via Supabase (a ser implementado no supabase_client.py)
        # from services.supabase_client import salvar_ocorrencia
        # salvar_ocorrencia(dados)

elif menu == "Consultar Ocorrências":
    listar_ocorrencias()
