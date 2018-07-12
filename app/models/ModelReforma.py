from app import db

refprofissionais = db.Table("reformaProfissional",
    db.Column('id_reforma', db.Integer, db.ForeignKey('reforma.id'), primary_key=True),
    db.Column('id_profissional', db.Integer, db.ForeignKey('profissional.id'), primary_key=True)
)

class Reforma(db.Model):
    __tablename__ = "reforma"

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    datainicio = db.Column(db.String)
    nome = db.Column(db.String, nullable=False)
    descricao = db.Column(db.String, nullable=False)
    profissionais = db.relationship('Profissional', secondary=refprofissionais, lazy='subquery', backref='reforma')
    pagamentos = db.relationship('Pagamento', backref='reforma')
    negociacoes = db.relationship('NegociacaoPreco', backref='reforma')
    conversas = db.relationship('Conversa', backref='reforma')
    #listaFotos
    #id_status = db.Column(db.Integer)
    #preco = db.Column(db.Float)
 
    def __init__(self, id_cliente, datainicio, nome, descricao):#, id_status, id_profissional, preco):
        self.id_cliente = id_cliente
        self.datainicio = datainicio
        self.nome = nome
        self.descricao = descricao
        #self.id_status = id_status
        #self.id_profissional = id_profissional
        #self.preco = preco

    def __repr__(self):
        return "<Reforma %r>" % self.id_cliente
