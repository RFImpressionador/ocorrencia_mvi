# config.py

"""
Este arquivo armazena configurações globais do sistema, incluindo as credenciais
para acessar o Supabase (URL da API e chave de autenticação).
NUNCA compartilhe essas informações publicamente.
"""

# URL base da API do Supabase
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")

# Chave da API (service role ou anon key, dependendo da segurança desejada)
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
