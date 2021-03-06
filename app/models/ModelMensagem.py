from app import db
#from sqlalchemy.orm import backref

class Mensagem(db.Model):
    __tablename__ = "mensagem"

    id = db.Column(db.Integer, primary_key=True)
    id_conversa = db.Column(db.Integer, db.ForeignKey('conversa.id', onupdate='CASCADE', ondelete='CASCADE') , nullable=False)
    perfil = db.Column(db.String, nullable=False)
    data = db.Column(db.Integer, nullable=False)
    mensagem = db.Column(db.String, nullable=False)
    preco = db.Column(db.Float)
    nivelPreco = db.Column(db.Integer)

    conversa = db.relationship('Conversa', backref= db.backref('mensagens', cascade="all, delete"))

    def __init__(self, id_conversa, perfil, data, mensagem, preco, nivelPreco):
        self.id_conversa = id_conversa
        self.perfil = perfil
        self.data = data
        self.mensagem = mensagem
        self.preco = preco
        self.nivelPreco = nivelPreco

    def __repr__(self):
        return "<Mensagem %r>" % self.mensagem
