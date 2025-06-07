FROM python:3.13.3-alpine

WORKDIR /app

COPY ./src /app

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]