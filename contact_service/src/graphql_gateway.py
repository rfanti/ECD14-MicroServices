import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import httpx

API_URL = "http://localhost:8000"

# Schema GraphQL
@strawberry.type
class Telefone:
    numero: str
    tipo: str

@strawberry.type
class Contato:
    nome: str
    telefones: list[Telefone]
    categoria: str

@strawberry.type
class Query:
    @strawberry.field
    async def contatos(self) -> list[Contato]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/contatos")
            return response.json()

    @strawberry.field
    async def contato(self, nome: str) -> Contato:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/contato/{nome}")
            if response.status_code == 404:
                return None
            return response.json()

# Mutations se quiser adicionar:
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def criar_contato(self, nome: str, numero: str, tipo: str, categoria: str) -> str:
        payload = {
            "nome": nome,
            "numero": numero,
            "tipo": tipo,
            "categoria": categoria
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{API_URL}/contato", data=payload)
            return response.json().get("message", "Erro ao criar contato")

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
