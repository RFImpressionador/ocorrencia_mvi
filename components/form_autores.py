import streamlit as st
import datetime
from services.supabase_storage import upload_imagem_supabase

def exibir_formulario():
    """
    Renderiza o formulário de autores de forma dinâmica.
    Retorna uma lista de dicionários com os dados de cada autor.
    """
    autores = []

    # Quantidade de autores a serem registrados
    num_autores = st.number_input("Quantos autores?", min_value=1, max_value=10, value=1, key="num_autores")

    # Para cada autor, criar um conjunto de campos
    for i in range(num_autores):
        with st.expander(f"Autor {i+1}"):
            nome = st.text_input(f"Nome do Autor {i+1}", key=f"nome_autor_{i}")
            nasc = st.date_input(f"Data de Nasc. Autor {i+1}", value=datetime.date(2000,1,1), key=f"nasc_autor_{i}")
            rg = st.text_input(f"RG Autor {i+1}", key=f"rg_autor_{i}")
            cpf = st.text_input(f"CPF Autor {i+1}", key=f"cpf_autor_{i}")
            endereco = st.text_input(f"Endereço Autor {i+1}", key=f"end_autor_{i}")
            antecedentes = st.text_area(f"Antecedentes Autor {i+1}", key=f"ant_autor_{i}")

            # Upload da foto do autor (opcional)
            foto = st.file_uploader(f"Foto do Autor {i+1} (opcional)", type=["jpg", "jpeg", "png"], key=f"foto_autor_{i}")
            foto_url = ""
            if foto:
                foto_url = upload_imagem_supabase("autores", foto, foto.name)
                st.success(f"Foto enviada com sucesso: {foto_url}")

            autores.append({
                "nome": nome,
                "nasc": nasc,
                "rg": rg,
                "cpf": cpf,
                "endereco": endereco,
                "antecedentes": antecedentes,
                "foto_url": foto_url
            })

    return autores
