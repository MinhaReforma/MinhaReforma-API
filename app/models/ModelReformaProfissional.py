from app import db

class ReformaProfissional(db.Model):
    __tablename__ = "reformaProfissional"

    id_reforma = db.Column(db.Integer, primary_key=True)
    id_profissional = db.Column(db.Integer, primary_key=True)

    def __init__(self, id_reforma, id_profissional):
        self.id_reforma = id_reforma
        self.id_profissional = id_profissional

    def __repr__(self):
        return "<ReformaProfissional %r>" % self.id_reforma
