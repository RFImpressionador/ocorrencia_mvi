import streamlit as st
from components import form_vitimas, form_autores, form_testemunhas
from services.listar_ocorrencias import listar_ocorrencias
from services.supabase_client import save_occurrence
from models.schema import Ocorrencia
from pydantic import ValidationError
from datetime import datetime
agora = datetime.now()


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

     # Submit button
    if st.button("Enviar"):
        data = {
            "good_number" : good_number,
            "date" : str (date),
            "hour" : str (hour),
            "city" : city,
            "local": local,
            "victims" : victims,
            "authors" : authors,
            "description" : description,
            "motivation" : motivation,
            "witnesses" : witnesses,
            "obs_finals" : obs_finals
        }

        st.json(data)
        try:
            occurrence = Occurrence(**data)
            save_occurrence(occurrence. dict ())
            st.success( "Occurrence registered in Supabase successfully!" )
        except ValidationError as ve:
            st.error( f"Invalid data: {ve} " )
        except Exception as e:
            st.error( f"Error saving occurrence: {e} " )

elif menu == "Consultar Ocorrências":
    listar_ocorrencias()
