from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time

class Vitima(BaseModel):
    nome: str
    nasc: Optional[date] = None
    rg: Optional[str] = None
    cpf: Optional[str] = None
    endereco: Optional[str] = None
    obs: Optional[str] = None
    foto_url: Optional[str] = None

class Autor(BaseModel):
    nome: str
    nasc: Optional[date] = None
    rg: Optional[str] = None
    cpf: Optional[str] = None
    endereco: Optional[str] = None
    antecedentes: Optional[str] = None
    foto_url: Optional[str] = None

class Testemunha(BaseModel):
    nome: str
    contato: Optional[str] = None
    obs: Optional[str] = None
    foto_url: Optional[str] = None

class Ocorrencia(BaseModel):
    bo_numero: str
    data: date
    hora: time
    cidade: str
    local: str
    vitimas: List[Vitima]
    autores: List[Autor]
    descricao: str
    motivacao: str
    testemunhas: List[Testemunha]
    observacoes_finais: Optional[str] = None
