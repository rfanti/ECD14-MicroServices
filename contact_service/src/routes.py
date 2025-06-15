from fastapi import APIRouter, HTTPException, Form
from typing import Dict, List
from models import Contato, CategoriaContato, Telefone, TipoTelefone


router = APIRouter(tags=["Contatos"])

contatos_db: Dict[str, Contato] = {}

@router.get("/")
def hello_world():
    """
    Endpoint que retorna uma mensagem de saudação.

    Retorna:
        dict: Um dicionário contendo a mensagem "Hello, World!".

    Exemplo de resposta:
        {
            "message": "Hello, World!"
        }
    """
    return {"message": "Hello, World!"}

@router.post("/contato", response_model=dict)
def criar_contato_form(
    nome: str = Form(...),
    numero: str = Form(...),
    tipo: TipoTelefone = Form(...),
    categoria: CategoriaContato = Form(...)
):
    """
    Cria um novo contato.

    Este endpoint permite criar um novo contato no banco de dados. 
    Se um contato com o mesmo nome já existir, retorna um erro.

    Parâmetros:
    - contato (Contato): Objeto contendo os dados do contato a ser criado.

    Respostas:
    - 200: Contato criado com sucesso.
        - Exemplo de resposta: {"message": "Contato criado com sucesso"}
    - 400: Contato já existe.
        - Exemplo de resposta: {"detail": "Contato já existe"}
    """
    if nome in contatos_db:
        raise HTTPException(status_code=400, detail="Contato já existe")
    
    telefone = Telefone(numero=numero, tipo=tipo)
    contato = Contato(nome=nome, telefones=[telefone], categoria=categoria)

    contatos_db[contato.nome] = contato
    return {"message": "Contato criado com sucesso"}

@router.get("/contato/{nome}", response_model=Contato)
def consultar_contato(nome: str):
    """
    Consulta um contato pelo nome.

    Este endpoint retorna as informações de um contato específico, identificado pelo nome.

    Parâmetros:
    - nome (str): Nome do contato a ser consultado.

    Retornos:
    - 200: Um dicionário contendo os dados do contato.
    - 404: Contato não encontrado.

    Exemplo de resposta de sucesso:
    {
        "nome": "João",
        "telefone": "123456789",
        "email": "joao@email.com"
    }
    """
    if nome not in contatos_db:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contatos_db[nome]

@router.get("/contatos", response_model=List[Contato])
def listar_contatos():
    """
    Lista todos os contatos cadastrados.

    Retorna:
        list: Uma lista contendo todos os contatos presentes no banco de dados.

    Exemplo de resposta:
        [
            {
                "id": 1,
                "nome": "João Silva",
                "email": "joao@email.com",
                "telefone": "123456789"
            },
            ...
        ]
    """
    return list(contatos_db.values())
