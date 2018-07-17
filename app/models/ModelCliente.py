from app import db
#from sqlalchemy.orm import backref


class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id', onupdate='CASCADE', ondelete='CASCADE'), unique=True, nullable=False)

    pessoa = db.relationship('Pessoa', backref=db.backref('cliente', cascade="all, delete"), lazy='joined', uselist=False)

    # reformas = db.relationship('Reforma', backref='cliente', lazy='joined')
    # negociacoes = db.relationship('NegociacaoPreco', backref='cliente')
    # conversas = db.relationship('Conversa', backref='cliente')

    def __init__(self, id_pessoa):
        self.id_pessoa = id_pessoa

    def __repr__(self):
        return "<Cliente %r>" % self.id_pessoa
