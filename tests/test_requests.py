import requests

# Criar contato
res = requests.post('http://localhost:5000/contatos', json={
    "nome": "João da Silva",
    "categoria": "pessoal",
    "telefones": [
        {"numero": "999999999", "tipo": "móvel"},
        {"numero": "333333333", "tipo": "fixo"}
    ]
})
print("Criar:", res.json())

# Listar contatos
res = requests.get('http://localhost:5000/contatos')
print("Listar:", res.json())

# Buscar por ID
res = requests.get('http://localhost:5000/contatos/1')
print("Buscar:", res.json())
