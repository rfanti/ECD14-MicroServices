from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="API de Contatos",
    description="Uma API simples de agenda de contatos com Swagger UI",
    version="1.0.0"
)

app.include_router(router)