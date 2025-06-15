from fastapi import FastAPI
from routes import router as rest_router
from schema_graphql import Query, Mutation
from strawberry.fastapi import GraphQLRouter
import strawberry

app = FastAPI(
    title="API de Contatos",
    description="Uma API simples de agenda de contatos com Swagger UI",
    version="1.0.0"
)

# REST
app.include_router(rest_router)

# GraphQL
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")