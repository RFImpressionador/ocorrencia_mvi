from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time

class Vitima(BaseModel):
    name: str
    nasc: Optional[date] = None
    rg: Optional[str] = None
    cpf: Optional[str] = None
    address: Optional [ str ] = None
    obs: Optional[str] = None
    foto_url: Optional[str] = None

class Autor(BaseModel):
    name: str
    nasc: Optional[date] = None
    rg: Optional[str] = None
    cpf: Optional[str] = None
    address: Optional [ str ] = None
    antecedents: Optional [ str ] = None
    foto_url: Optional[str] = None

class Testimonah ( BaseModel ):
 
    name: str
    contato: Optional[str] = None
    obs: Optional[str] = None
    foto_url: Optional[str] = None

class Occurrence ( BaseModel ):
 
    bo_num: str
    data: date
    time: time
    city: str
    local: str
    victims: List [Victim]
    authors: List [Author]
    description: str
    motivacao: str
    witnesses: List [Witness]
    obs_finais: Optional[str] = None
