from app import db

class ProfissionalHabilidade(db.Model):
    __tablename__ = "ProfissionalHabilidade"

    id_profissional = db.Column(db.Integer, primary_key=True)
    id_habilidade = db.Column(db.Integer)

    def __init__(self, id_profissional, id_habilidade):
        self.id_profissional = id_profissional
        self.id_habilidade = id_habilidade

    def __repr__(self):
        return "<ProfissionalHabilidade %r>" % self.id_profissional
