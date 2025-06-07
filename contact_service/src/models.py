from pydantic import BaseModel
from typing import List

class Telefone(BaseModel):
    numero: str
    tipo: str  # "móvel", "fixo", "comercial"

class Contato(BaseModel):
    nome: str
    telefones: List[Telefone]
    categoria: str  # "familiar", "pessoal", "comercial"
