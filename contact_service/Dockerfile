FROM python:3.13.3-alpine

WORKDIR /app

COPY ./src /app/src

RUN pip install fastapi uvicorn

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]