from flask import Flask
from flask_restx import Api, Resource, fields
from enum import Enum

app = Flask(__name__)
api = Api(app, version='1.0', title='Agenda de Contatos API',
          description='API REST de Agenda de Contatos com Swagger',
          doc='/docs')  # Documentação Swagger em /docs

ns = api.namespace('contatos', description='Operações com contatos')


class TelefoneTipo(str, Enum):
    MOVEL = "móvel"
    FIXO = "fixo"
    COMERCIAL = "comercial"


class CategoriaContato(str, Enum):
    FAMILIAR = "familiar"
    PESSOAL = "pessoal"
    COMERCIAL = "comercial"


telefone_model = api.model('Telefone', {
    'numero': fields.String(required=True, description='Número de telefone'),
    'tipo': fields.String(required=True, enum=[t.value for t in TelefoneTipo])
})

contato_model = api.model('Contato', {
    'id': fields.Integer(readOnly=True, description='ID do contato'),
    'nome': fields.String(required=True, description='Nome do contato'),
    'categoria': fields.String(required=True, enum=[c.value for c in CategoriaContato]),
    'telefones': fields.List(fields.Nested(telefone_model), required=True)
})

contatos_db = []


@ns.route('')
class ContatoList(Resource):
    @ns.marshal_list_with(contato_model)
    def get(self):
        """Lista todos os contatos"""
        return contatos_db

    @ns.expect(contato_model)
    @ns.marshal_with(contato_model, code=201)
    def post(self):
        """Adiciona um novo contato"""
        data = api.payload
        novo = {
            'id': len(contatos_db) + 1,
            'nome': data['nome'],
            'categoria': data['categoria'],
            'telefones': data['telefones']
        }
        contatos_db.append(novo)
        return novo, 201


@ns.route('/<int:id>')
@ns.response(404, 'Contato não encontrado')
@ns.param('id', 'ID do contato')
class Contato(Resource):
    @ns.marshal_with(contato_model)
    def get(self, id):
        """Consulta um contato pelo ID"""
        contato = next((c for c in contatos_db if c['id'] == id), None)
        if contato:
            return contato
        api.abort(404, "Contato não encontrado")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
