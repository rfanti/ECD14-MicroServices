import strawberry
from typing import List
from models import TipoTelefone, CategoriaContato, Contato as ContatoModel, Telefone as TelefoneModel

# Criando os enums Strawberry manualmente a partir dos valores
GQLTipoTelefone = strawberry.enum(TipoTelefone)
GQLCategoriaContato = strawberry.enum(CategoriaContato)

@strawberry.type
class Telefone:
    numero: str
    tipo: GQLTipoTelefone
    #tipo: str

@strawberry.type
class Contato:
    nome: str
    telefones: List[Telefone]
    categoria: GQLCategoriaContato
    #categoria: str

@strawberry.input
class TelefoneInput:
    numero: str
    tipo: GQLTipoTelefone
    #tipo: str

@strawberry.input
class ContatoInput:
    nome: str
    telefones: List[TelefoneInput]
    categoria: GQLCategoriaContato
    #categoria: str

# Simulando banco de dados
contatos_db: dict[str, ContatoModel] = {}

@strawberry.type
class Mutation:
    @strawberry.mutation
    def criar_contato(self, input: ContatoInput) -> str:
        if input.nome in contatos_db:
            raise ValueError("Contato já existe")
        contato = ContatoModel(
            nome=input.nome,
            categoria=input.categoria,
            telefones=[TelefoneModel(numero=t.numero, tipo=t.tipo) for t in input.telefones]
        )
        contatos_db[input.nome] = contato
        return "Contato criado com sucesso"

@strawberry.type
class Query:
    @strawberry.field
    def listar_contatos(self) -> List[Contato]:
        return [
            Contato(
                nome=c.nome,
                categoria=c.categoria,
                telefones=[
                    Telefone(numero=t.numero, tipo=t.tipo)
                    for t in c.telefones
                ],
            )
            for c in contatos_db.values()
        ]
