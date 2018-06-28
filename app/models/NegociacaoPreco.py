from app import db

class NegociacaoPreco(db.Model):
    __tablename__ = "negociacaopreco"

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    id_profissional = db.Column(db.Integer)
    preco = db.Column(db.Float)
    id_reforma = db.Column(db.Integer)

    def __init__(self, id_cliente, id_profissional, preco, id_reforma):
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional
        self.preco = preco
        self.id_reforma = id_reforma

    def __repr__(self):
        return "<NegociacaoPreco %r>" % self.id_reforma
