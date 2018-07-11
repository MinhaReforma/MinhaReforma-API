from app import db

class Mensagem(db.Model):
    __tablename__ = "mensagem"

    id = db.Column(db.Integer, primary_key=True)
    id_conversa = db.Column(db.Integer, nullable=False)
    Data = db.Column(db.DateTime, nullable=False)
    mensagem = db.Column(db.String, nullable=False)

    def __init__(self, id_conversa, Data, mensagem):
        self.id_conversa = id_conversa
        self.Data = Data
        self.mensagem = mensagem

    def __repr__(self):
        return "<Mensagem %r>" % self.mensagem
