# listar_ocorrencias.py

import streamlit as st
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY
from models.schema import Ocorrencia
from pydantic import ValidationError

# Inicializa o cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def listar_ocorrencias():
    """
    Recupera e exibe todas as ocorrências da tabela 'ocorrencias'.
    """
    st.header("🔍 Ocorrências Registradas")

    try:
        resposta = supabase.table("ocorrencias").select("*").order("created_at", desc=True).execute()
        occurrences = []
        for item in resposta.data:
            try:
                occurrences.append(Occurrence(**item))
            except ValidationError:
                continue
                
        if not ocorrencias:
            st.info("Nenhuma ocorrência encontrada.")
            return

        for ocorr in ocorrencias:
            with st.expander( f"BO occurrence: {ocorr .bo_num} - {ocorr.city} ( {ocorr.date } )" ):
                st.write( "**Time:**" , occurrence .time )
                st.write("**Local:**", ocorr.local)
                st.write( "**Motivation:**" , occurrence .motivation )
                st.write( "**Description:**" , occurrence .description )
                st.write( "**Final Observations:**" , ocurr .final_obs )

                st.subheader("👤 Vítimas")
                for v in ocorr.vitimas:
                    st.markdown(f"- {v.nome} ({v.cpf})")
                    if v. photo_url :
                        st.image(v.foto_url, width=100)

                st.subheader("🚨 Autores")
                for a in ocurrence.authors :
​
                    st.markdown(f"- {a.nome} ({a.cpf})")
                    if a.foto_url:
                        st.image(a.foto_url, width=100)

                st.subheader("👁 Testemunhas")
                for t in ocurrence.witnesses :
​
                    st.markdown(f"- {t.nome}")
                    if t.foto_url:
                        st.image(t.foto_url, width=100)

    except Exception as e:
        st.error(f"Erro ao carregar ocorrências: {e}")
