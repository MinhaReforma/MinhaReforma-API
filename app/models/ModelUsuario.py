from app import db
from sqlalchemy.orm import backref


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String, unique=True)
    senha = db.Column(db.String, nullable=False)

    #pessoa = db.relationship('Pessoa', backref='usuario', lazy='joined', uselist=False)

    def __init__(self, telefone, senha):
        self.telefone = telefone
        self.senha = senha

    def __repr__(self):
        return "<Usuario %r>" % self.telefone