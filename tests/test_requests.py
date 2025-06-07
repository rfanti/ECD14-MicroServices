import requests

# Criar contato
res = requests.post('http://localhost:5000/contatos', json={
    "nome": "João da Silva",
    "categoria": "pessoal",
    "telefones": [
        {"numero": "51988887777", "tipo": "móvel"},
        {"numero": "5133332222", "tipo": "fixo"}
    ]
})
print("Criado:", res.json())

# Listar contatos
res = requests.get('http://localhost:5000/contatos')
print("Todos:", res.json())

# Consultar contato específico
res = requests.get('http://localhost:5000/contatos/1')
print("Contato 1:", res.json())
