from app import db

class ReformaProfissional(db.Model):
    __tablename__ = "reformaProfissional"

    id_reforma = db.Column(db.Integer, db.ForeignKey('reforma.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissional.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    preco = db.Column(db.Float)

    reforma = db.relationship('Reforma', backref= db.backref('reformaprofissionais', cascade="all, delete"))
    profissional = db.relationship('Profissional', backref= db.backref('reformaprofissionais', cascade="all, delete"))

    def __init__(self, id_reforma, id_profissional, preco=None):
        self.id_reforma = id_reforma
        self.id_profissional = id_profissional
        self.preco = preco

    def __repr__(self):
        return "<ReformaProfissional %r>" % self.id_reforma
