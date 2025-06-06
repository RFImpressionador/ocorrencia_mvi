# supabase_client.py

from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

# Inicializa o cliente Supabase
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Função para salvar os dados da ocorrência

def salvar_ocorrencia(dados: dict):
    """
    Insere os dados recebidos do formulário na tabela 'ocorrencias'.
    """
   response = supabase.table("ocorrencias").insert(data).execute()
    return response
