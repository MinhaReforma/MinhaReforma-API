from app import db

class Conversa(db.Model):
    __tablename__ = "conversa"

    id_reforma = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, nullable=False)
    id_profissional = db.Column(db.Integer, nullable=False)

    def __init__(self, id_reforma, id_cliente, id_profissional, conversa):
        self.id_reforma = id_reforma
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional

    def __repr__(self):
        return "<Conversa %r>" % self.id_reforma
