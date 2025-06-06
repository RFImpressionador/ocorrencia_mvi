from datetime import datetime
import streamlit as st
from components import form_vitimas, form_autores, form_testemunhas
from services.listar_ocorrencias import listar_ocorrencias
from services.supabase_client import save_occurrence
from models.schema import Ocorrencia
from pydantic import ValidationError

# Configuração da página
st.set_page_config(page_title="Formulário de Ocorrência", layout="wide")

# Menu lateral
menu = st.sidebar.selectbox("Menu", ["Registrar Ocorrência", "Consultar Ocorrências"])

if menu == "Registrar Ocorrência":
    st.title("Formulário de Registro de Ocorrência")

    st.header("1. Dados Gerais")
    bo_num = st.text_input("Nº do B.O.")
    data = st.date_input("Data", value=datetime.today())
    hora = st.time_input("Hora")
    cidade = st.text_input("Cidade")
    local = st.text_area("Local do Fato")

    vitimas = form_vitimas.exibir_formulario()
    autores = form_autores.exibir_formulario()

    st.header("4. Descrição dos Fatos")
    descricao = st.text_area("Narrativa dos Fatos", height=200)

    st.header("5. Motivação Provável")
    motivacao = st.text_area("Motivação", height=100)

    testemunhas = form_testemunhas.exibir_formulario()

    st.header("7. Anexos / Observações Finais")
    obs_finais = st.text_area("Observações Finais", height=100)

    if st.button("Enviar"):
    dados = {
        "bo_numero": bo_num,
        "data": str(data),
        "hora": str(hora),
        "cidade": cidade,
        "local": local,
        "vitimas": vitimas,
        "autores": autores,
        "descricao": descricao,
        "motivacao": motivacao,
        "testemunhas": testemunhas,
        "observacoes_finais": obs_finais
    }

    try:
        ocorrencia = Ocorrencia(**dados)
        resultado = save_occurrence(ocorrencia.dict())
        st.success("Ocorrência registrada com sucesso!")
        st.json(resultado.data)  # opcional: mostrar resposta do Supabase
    except ValidationError as ve:
        st.error(f"Dados inválidos: {ve}")
    except Exception as e:
        st.error(f"Erro ao salvar a ocorrência: {e}")

elif menu == "Consultar Ocorrências":
    listar_ocorrencias()

