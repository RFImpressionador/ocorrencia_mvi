# listar_ocorrencias.py

import streamlit as st
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

# Inicializa o cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def listar_ocorrencias():
    """
    Recupera e exibe todas as ocorrências da tabela 'ocorrencias'.
    """
    st.header("🔍 Ocorrências Registradas")

    try:
        resposta = supabase.table("ocorrencias").select("*").order("created_at", desc=True).execute()
        ocorrencias = resposta.data

        if not ocorrencias:
            st.info("Nenhuma ocorrência encontrada.")
            return

        for ocorr in ocorrencias:
            with st.expander(f"Ocorrência BO: {ocorr['bo_num']} - {ocorr['cidade']} ({ocorr['data']})"):
                st.write("**Hora:**", ocorr['hora'])
                st.write("**Local:**", ocorr['local'])
                st.write("**Motivação:**", ocorr['motivacao'])
                st.write("**Descrição:**", ocorr['descricao'])
                st.write("**Observações Finais:**", ocorr['obs_finais'])

                st.subheader("👤 Vítimas")
                for v in ocorr['vitimas']:
                    st.markdown(f"- {v['nome']} ({v['cpf']})")
                    if v.get("foto_url"):
                        st.image(v['foto_url'], width=100)

                st.subheader("🚨 Autores")
                for a in ocorr['autores']:
                    st.markdown(f"- {a['nome']} ({a['cpf']})")
                    if a.get("foto_url"):
                        st.image(a['foto_url'], width=100)

                st.subheader("👁 Testemunhas")
                for t in ocorr['testemunhas']:
                    st.markdown(f"- {t['nome']}")
                    if t.get("foto_url"):
                        st.image(t['foto_url'], width=100)

    except Exception as e:
        st.error(f"Erro ao carregar ocorrências: {e}")
