from app import db

class Pessoa(db.Model):
    __tablename__ = "pessoa"

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    cpf = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    #id_carteira = db.Column(db.Integer)
    #foto = db.Column(db.String)

    def __init__(self, cpf, nome, id_usuario):#, id_carteira, foto):
        self.cpf = cpf
        self.nome = nome
        self.id_usuario = id_usuario
        #self.id_carteira = id_carteira

    def __repr__(self):
        return "<Pessoa %r>" % self.nome
