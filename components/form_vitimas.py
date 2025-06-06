import streamlit as st
import datetime
from services.supabase_storage import upload_imagem_supabase

def exibir_formulario():
    """
    Renderiza o formulário de vítimas de forma dinâmica.
    Retorna uma lista de dicionários com os dados de cada vítima.
    """
    vitimas = []

    # Quantidade de vítimas a serem registradas
    num_vitimas = st.number_input("Quantas vítimas?", min_value=1, max_value=10, value=1, key="num_vitimas")

    # Para cada vítima, criar um conjunto de campos
    for i in range(num_vitimas):
        with st.expander(f"Vítima {i+1}"):
            nome = st.text_input(f"Nome da Vítima {i+1}", key=f"nome_vitima_{i}")
            nasc = st.date_input(f"Data de Nasc. Vítima {i+1}", value=datetime.date(2000,1,1), key=f"nasc_vitima_{i}")
            rg = st.text_input(f"RG Vítima {i+1}", key=f"rg_vitima_{i}")
            cpf = st.text_input(f"CPF Vítima {i+1}", key=f"cpf_vitima_{i}")
            endereco = st.text_input(f"Endereço Vítima {i+1}", key=f"end_vitima_{i}")
            obs = st.text_area(f"Observações Vítima {i+1}", key=f"obs_vitima_{i}")

            # Upload da foto da vítima (opcional)
            foto = st.file_uploader(f"Foto da Vítima {i+1} (opcional)", type=["jpg", "jpeg", "png"], key=f"foto_vitima_{i}")
            foto_url = ""
            if foto:
                foto_url = upload_imagem_supabase("vitimas", foto, foto.name)
                st.success(f"Foto enviada com sucesso: {foto_url}")

            vitimas.append({
                "nome": nome,
                "nasc": str(nasc),
                "rg": rg,
                "cpf": cpf,
                "endereco": endereco,
                "obs": obs,
                "foto_url": foto_url
            })

    return vitimas
