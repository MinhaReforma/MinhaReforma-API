from app import db

profhabilidades = db.Table("profissionalHabilidade",
    db.Column('id_profissional', db.Integer, db.ForeignKey('profissional.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
    db.Column('id_habilidade', db.Integer, db.ForeignKey('habilidade.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
)

class Habilidade(db.Model):
    __tablename__ = "habilidade"

    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.Column(db.String, nullable=False)

    profissionais = db.relationship('Profissional', secondary=profhabilidades, lazy='subquery', backref='habilidades')

    def __init__(self, habilidade):
        self.habilidade = habilidade

    def __repr__(self):
        return "<Habilidade %r>" % self.habilidade
