from fastapi import APIRouter, HTTPException
from typing import Dict, List
from models import Contato

router = APIRouter()

contatos_db: Dict[str, Contato] = {}

@router.post("/contato")
def criar_contato(contato: Contato):
    if contato.nome in contatos_db:
        raise HTTPException(status_code=400, detail="Contato já existe")
    contatos_db[contato.nome] = contato
    return {"message": "Contato criado com sucesso"}

@router.get("/contato/{nome}")
def consultar_contato(nome: str):
    if nome not in contatos_db:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contatos_db[nome]

@router.get("/contatos")
def listar_contatos():
    return list(contatos_db.values())
