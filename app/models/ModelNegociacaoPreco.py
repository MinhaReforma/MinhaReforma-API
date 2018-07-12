from app import db
from sqlalchemy.orm import backref


class NegociacaoPreco(db.Model):
    __tablename__ = "negociacaopreco"

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id', ondelete='CASCADE'), nullable=False)
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissional.id', ondelete='CASCADE'), nullable=False)
    id_reforma = db.Column(db.Integer, db.ForeignKey('reforma.id', ondelete='CASCADE'), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    cliente = db.relationship('Cliente', backref=backref('negociacoes', passive_deletes=True))
    profissional = db.relationship('Profissional', backref=backref('negociacoes', passive_deletes=True))
    reforma = db.relationship('Reforma', backref=backref('negociacoes', passive_deletes=True))

    def __init__(self, id_cliente, id_profissional, preco, id_reforma):
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional
        self.preco = preco
        self.id_reforma = id_reforma

    def __repr__(self):
        return "<NegociacaoPreco %r>" % self.id_reforma
