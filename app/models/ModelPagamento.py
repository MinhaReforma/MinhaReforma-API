from app import db
from sqlalchemy.orm import backref


class Pagamento(db.Model):
    __tablename__ = "pagamento"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Integer, nullable=False)
    id_reforma = db.Column(db.Integer, db.ForeignKey('reforma.id', ondelete='CASCADE'), nullable=False)

    reforma = db.relationship('Reforma', backref=backref('pagamentos', passive_deletes=True))

    def __init__(self, data, id_reforma):
        self.data = data
        self.id_reforma = id_reforma

    def __repr__(self):
        return "<Pagamento %r>" % self.id_reforma 
