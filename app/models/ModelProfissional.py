from app import db

profhabilidades = db.Table("profissionalHabilidade",
    db.Column('id_profissional', db.Integer, db.ForeignKey('profissional.id'), primary_key=True),
    db.Column('id_habilidade', db.Integer, db.ForeignKey('habilidade.id'), primary_key=True)
)

class Profissional(db.Model):
    __tablename__ = "profissional"

    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id'), unique=True, nullable=False)
    habilidades = db.relationship('Habilidade', secondary=profhabilidades, lazy='subquery', backref='profissional')
    negociacoes = db.relationship('NegociacaoPreco', backref='profissional')
    conversas = db.relationship('Conversa',backref='profissional')
    #id_areaAtuacao = db.Column(db.Integer)

    def __init__(self, id_pessoa):#, id_areaAtuacao):
        self.id_pessoa = id_pessoa
        #self.id_areaAtuacao = id_areaAtuacao

    def __repr__(self):
        return "<Profissional %r>" % self.id_pessoa
