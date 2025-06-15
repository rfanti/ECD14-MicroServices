from pydantic import BaseModel
from typing import List
from enum import Enum

class TipoTelefone(str, Enum):
    move = "movel"
    fixo = "fixo"
    comercial = "comercial"

class CategoriaContato(str, Enum):
    familiar = "familiar"
    pessoal = "pessoal"
    comercial = "comercial"

class Telefone(BaseModel):
    numero: str
    tipo: TipoTelefone

class Contato(BaseModel):
    nome: str
    telefones: List[Telefone]
    categoria: CategoriaContato
