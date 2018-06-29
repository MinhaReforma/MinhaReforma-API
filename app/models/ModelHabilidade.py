from app import db

class Habilidade(db.Model):
    __tablename__ = "habilidade"

    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.Column(db.String)

    def __init__(self, habilidade):
        self.habilidade = habilidade

    def __repr__(self):
        return "<Habilidade %r>" % self.habilidade
