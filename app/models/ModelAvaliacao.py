from app import db

class Avaliacao(db.Model):
    __tablename__ = "avaliacao"

    id_avaliador = db.Column(db.Integer, db.ForeignKey('usuario.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    id_avaliado = db.Column(db.Integer, db.ForeignKey('usuario.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    id_reforma = db.Column(db.Integer, db.ForeignKey('reforma.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    mensagem = db.Column(db.String)
    nota = db.Column(db.Float)
    tipo = db.Column(db.String)

    usuario_avaliador = db.relationship('Usuario', foreign_keys=[id_avaliador], backref= db.backref('avaliacao', cascade="all, delete"))
    usuario_avaliado = db.relationship('Usuario', foreign_keys=[id_avaliado])
    reforma = db.relationship('Reforma')

    def __init__(self, id_avaliador, id_avaliado, id_reforma, tipo, mensagem=None ,nota=None):
        self.id_avaliador = id_avaliador
        self.id_avaliado = id_avaliado
        self.id_reforma = id_reforma
        self.mensagem = mensagem
        self.nota = nota
        self.tipo = tipo

    def __repr__(self):
        return "<Avaliacao %r>" % self.id_avaliador