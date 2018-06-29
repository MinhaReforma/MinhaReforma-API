from app import db

class Profissional(db.Model):
    __tablename__ = "profissional"

    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer)
    #id_areaAtuacao = db.Column(db.Integer)

    def __init__(self, id_pessoa):#, id_areaAtuacao):
        self.id_pessoa = id_pessoa
        #self.id_areaAtuacao = id_areaAtuacao

    def __repr__(self):
        return "<Profissional %r>" % self.id_pessoa
