from app import db
#from sqlalchemy.orm import backref

class Conversa(db.Model):
    __tablename__ = "conversa"

    id = db.Column(db.Integer, primary_key=True)
    id_reforma = db.Column(db.Integer, db.ForeignKey('reforma.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissional.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    reforma = db.relationship('Reforma', backref= db.backref('conversas', cascade="all, delete"))
    cliente = db.relationship('Cliente', backref= db.backref('conversas', cascade="all, delete"))
    profissional = db.relationship('Profissional', backref= db.backref('conversas', cascade="all, delete"))
    
    #mensagens = db.relationship('Mensagem', backref='conversa')

    def __init__(self, id_reforma, id_cliente, id_profissional):
        self.id_reforma = id_reforma
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional

    def __repr__(self):
        return "<Conversa %r>" % self.id_reforma
