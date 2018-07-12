from app import db

class Mensagem(db.Model):
    __tablename__ = "mensagem"

    id = db.Column(db.Integer, primary_key=True)
    id_conversa = db.Column(db.Integer, db.ForeignKey('conversa.id') , nullable=False)
    perfil = db.Column(db.String, nullable=False)
    data = db.Column(db.Integer, nullable=False)
    mensagem = db.Column(db.String, nullable=False)

    def __init__(self, id_conversa, perfil, data, mensagem):
        self.id_conversa = id_conversa
        self.perfil = perfil
        self.data = data
        self.mensagem = mensagem

    def __repr__(self):
        return "<Mensagem %r>" % self.mensagem
