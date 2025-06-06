from supabase import create_client, Client
import os

# Carrega as variáveis de ambiente do Streamlit Secrets
SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

# Inicializa o cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_occurrence(dados: dict):
    """
    Insere os dados de ocorrência na tabela 'ocorrencias' do Supabase.
    """
    try:
        resposta = supabase.table("ocorrencias").insert(dados).execute()
        return resposta
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar no Supabase: {e}")
