from __future__ importar anotações
digitando import List , Opcional​ 
from pydantic importar BaseModel
from data e hora importar data, hora

classe Vitima ( BaseModel ):
 
    nome: str
    nasc: Opcional [data] = Nenhum
    rg: Opcional [ str ] = Nenhum
    cpf: Opcional [ str ] = Nenhum
    endereco: Optional[str] = None
    obs: Opcional [ str ] = Nenhum
    foto_url: Opcional [ str ] = Nenhum

classe Autor ( BaseModel ):
 
    nome: str
    nasc: Opcional [data] = Nenhum
    rg: Opcional [ str ] = Nenhum
    cpf: Opcional [ str ] = Nenhum
    endereco: Optional[str] = None
    antecedentes: Opcional [ str ] = Nenhum
    foto_url: Opcional [ str ] = Nenhum

classe Testimonah ( BaseModel ):
 
    nome: str
    contato: Opcional [ str ] = Nenhum
    obs: Opcional [ str ] = Nenhum
    foto_url: Opcional [ str ] = Nenhum

classe Ocorrência ( BaseModel ):
 
    bo_num: str
    dados: data
    hora: time
    cidade: str
    local: str
    vitimas: List[Vitima]
    autores: List[Autor]
    descricao: str
    motivação: str
    testemunhas: List[Testemunha]
    obs_finais: Opcional [ str ] = Nenhum
