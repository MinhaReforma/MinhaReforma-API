from app import db

class ProfissionalHabilidade(db.Model):
    __tablename__ = "profissionalHabilidade"

    id_profissional = db.Column(db.Integer)
    id_hbilidade = db.Column(db.Integer)

    def __init__(self, id_profissional, id_hbilidade):
        self.id_profissional = id_profissional
        self.id_hbilidade = id_hbilidade

    def __repr__(self):
        return "<ProfissionalHabilidade %r>" % self.id_profissional
