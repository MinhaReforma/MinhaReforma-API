from app import db

class Reforma(db.Model):
    __tablename__ = "reforma"

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    datainicio = db.Column(db.DateTime)
    nome = db.Column(db.String)
    descricao = db.Column(db.String)
    #listaFotos
    listaProfissionais = db.Column(db.String)
    id_status = db.Column(db.Integer)
    id_profissional = db.Column(db.Integer)
    preco = db.Column(db.Float)
 
    def __init__(self, id_cliente, datainicio, nome, descricao, listaProfissionais, id_status, id_profissional, preco):
        self.id_cliente = id_cliente
        self.datainicio = datainicio
        self.nome = nome
        self.descricao = descricao
        self.listaProfissionais = listaProfissionais
        self.id_status = id_status
        self.id_profissional = id_profissional
        self.preco = preco

    def __repr__(self):
        return "<Reforma %r>" % self.id_cliente
