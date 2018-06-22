from app import db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String, unique=True)
    nome = db.Column(db.String)
    id_usuario = db.Column(db.String)
    #id_carteira = db.Column(db.String)
    #foto = db.Column(db.String)

    def __init__(self, cpf, nome, id_usuario):#, id_carteira, foto):
        self.cpf = cpf
        self.nome = nome
        self.id_usuario = id_usuario
        #self.id_carteira = id_carteira
        #self.foto = foto

    def __repr__(self):
        return "<Cliente %r>" % self.nome
