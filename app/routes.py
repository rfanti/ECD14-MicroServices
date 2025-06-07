from flask import Blueprint, request, jsonify
from .models import db, Contact, Phone
from .schemas import ContactSchema
from .models import PhoneType, ContactCategory

bp = Blueprint('api', __name__)
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

@bp.route('/contatos', methods=['POST'])
def criar_contato():
    data = request.get_json()
    contato = Contact(nome=data['nome'], categoria=data['categoria'])
    for tel in data['telefones']:
        contato.telefones.append(Phone(numero=tel['numero'], tipo=tel['tipo']))
    db.session.add(contato)
    db.session.commit()
    return contact_schema.jsonify(contato), 201

@bp.route('/contatos/<int:id>', methods=['GET'])
def obter_contato(id):
    contato = Contact.query.get_or_404(id)
    return contact_schema.jsonify(contato)

@bp.route('/contatos', methods=['GET'])
def listar_contatos():
    contatos = Contact.query.all()
    return contacts_schema.jsonify(contatos)
