from app import db
#from sqlalchemy.orm import backref


class Pessoa(db.Model):
    __tablename__ = "pessoa"

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', onupdate='CASCADE', ondelete='CASCADE'), unique=True, nullable=False)
    cpf = db.Column(db.String, unique=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    #id_carteira = db.Column(db.Integer)
    #foto = db.Column(db.String)

    usuario = db.relationship('Usuario', lazy='joined', uselist=False, backref=db.backref('pessoa', cascade="all, delete"))

    # cliente = db.relationship('Cliente', backref='pessoa', lazy='joined', uselist=False)
    # profissional = db.relationship('Profissional', backref='pessoa', lazy='joined', uselist=False)

    def __init__(self, cpf, nome, id_usuario):#, id_carteira, foto):
        self.cpf = cpf
        self.nome = nome
        self.id_usuario = id_usuario
        #self.id_carteira = id_carteira

    def __repr__(self):
        return "<Pessoa %r>" % self.nome
