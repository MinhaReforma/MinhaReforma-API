from app import db
from sqlalchemy.orm import backref

profhabilidades = db.Table("profissionalHabilidade",
    db.Column('id_profissional', db.Integer, db.ForeignKey('profissional.id', ondelete='CASCADE'), primary_key=True),
    db.Column('id_habilidade', db.Integer, db.ForeignKey('habilidade.id', ondelete='CASCADE'), primary_key=True)
)

class Habilidade(db.Model):
    __tablename__ = "habilidade"

    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.Column(db.String, nullable=False)

    profissionais = db.relationship('Profissional', secondary=profhabilidades, lazy='subquery', backref=backref('habilidades', passive_deletes=True))

    def __init__(self, habilidade):
        self.habilidade = habilidade

    def __repr__(self):
        return "<Habilidade %r>" % self.habilidade
