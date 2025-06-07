from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Telefone(BaseModel):
    numero: str
    tipo: str  # tipos: "móvel", "fixo", "comercial"

class Contato(BaseModel):
    nome: str
    telefones: List[Telefone]
    categoria: str  # categorias: "familiar", "pessoal", "comercial"

contatos_db: Dict[str, Contato] = {}

@app.post("/contato")
def criar_contato(contato: Contato):
    if contato.nome in contatos_db:
        raise HTTPException(status_code=400, detail="Contato já existe")
    contatos_db[contato.nome] = contato
    return {"message": "Contato criado com sucesso"}

@app.get("/contato/{nome}")
def consultar_contato(nome: str):
    if nome not in contatos_db:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contatos_db[nome]

@app.get("/contatos")
def listar_contatos():
    return list(contatos_db.values())