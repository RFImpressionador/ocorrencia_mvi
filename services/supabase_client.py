# supabase_client.py

from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

# Inicializa o cliente Supabase
def conectar_supabase() -> Client:
    """
    Cria e retorna uma conexão com o Supabase usando os dados do config.py
    """
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para salvar os dados da ocorrência

def salvar_ocorrencia(dados: dict):
    """
    Insere os dados recebidos do formulário na tabela 'ocorrencias'.
    """
    supabase = conectar_supabase()
    resposta = supabase.table("ocorrencias").insert(dados).execute()
    return resposta
