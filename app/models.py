from flask_sqlalchemy import SQLAlchemy
from enum import Enum
import enum

db = SQLAlchemy()

class PhoneType(enum.Enum):
    MOVEL = 'móvel'
    FIXO = 'fixo'
    COMERCIAL = 'comercial'

class ContactCategory(enum.Enum):
    FAMILIAR = 'familiar'
    PESSOAL = 'pessoal'
    COMERCIAL = 'comercial'

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.Enum(ContactCategory), nullable=False)
    telefones = db.relationship('Phone', backref='contato', cascade="all, delete")

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.Enum(PhoneType), nullable=False)
    contato_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)
