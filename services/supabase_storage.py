
# supabase_storage.py

from config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client
import uuid

def upload_imagem_supabase(pasta: str, arquivo_stream, nome_original: str) -> str:
    """
    Faz upload de uma imagem para o bucket 'imagens' do Supabase Storage.
    - pasta: subpasta dentro do bucket (ex: 'vitimas', 'autores', 'testemunhas')
    - arquivo_stream: arquivo carregado com st.file_uploader()
    - nome_original: nome original do arquivo para gerar nome único
    Retorna a URL pública da imagem.
    """
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Gera nome de arquivo único com UUID
    extensao = nome_original.split(".")[-1]
    nome_arquivo = f"{pasta}/{uuid.uuid4()}.{extensao}"

    # Faz o upload
    conteudo = arquivo_stream.read()
    supabase.storage().from_("imagens").upload(nome_arquivo, conteudo, {"content-type": f"image/{extensao}"})

    # Gera URL pública
    url_base = f"{SUPABASE_URL}/storage/v1/object/public/imagens/"
    return f"{url_base}{nome_arquivo}"
