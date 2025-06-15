FROM python:3.13.3-alpine

WORKDIR /app

COPY ./src /app/src

# Defina o PYTHONPATH para o Python reconhecer src como módulo raiz
ENV PYTHONPATH=/app/src

RUN pip install fastapi uvicorn
RUN pip install python-multipart
RUN pip install strawberry-graphql[fastapi] httpx

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
