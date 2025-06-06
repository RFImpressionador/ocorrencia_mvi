import streamlit as st
import datetime
from services.supabase_storage import upload_imagem_supabase

def exibir_formulario():
    """
    Renderiza o formulário de testemunhas de forma dinâmica.
    Retorna uma lista de dicionários com os dados de cada testemunha.
    """
    testemunhas = []

    # Quantidade de testemunhas a serem registradas
    num_test = st.number_input("Quantas testemunhas?", min_value=0, max_value=10, value=0, key="num_testemunhas")

    # Para cada testemunha, criar um conjunto de campos
    for i in range(num_test):
        with st.expander(f"Testemunha {i+1}"):
            nome = st.text_input(f"Nome Testemunha {i+1}", key=f"nome_test_{i}")
            contato = st.text_input(f"Contato Testemunha {i+1}", key=f"contato_test_{i}")
            obs = st.text_input(f"Observação Testemunha {i+1}", key=f"obs_test_{i}")

            # Upload da foto da testemunha (opcional)
            foto = st.file_uploader(f"Foto da Testemunha {i+1} (opcional)", type=["jpg", "jpeg", "png"], key=f"foto_test_{i}")
            foto_url = ""
            if foto:
                foto_url = upload_imagem_supabase("testemunhas", foto, foto.name)
                st.success(f"Foto enviada com sucesso: {foto_url}")

            testemunhas.append({
                "nome": nome,
                "rg": rg,
                "cpf": cpf,
                "endereco": endereco,
                "contato": contato,
                "obs": obs,
                "foto_url": foto_url
            })

    return testemunhas

