from app import db

class Pagamento(db.Model):
    __tablename__ = "pagamento"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    id_reforma = db.Column(db.Integer)

    def __init__(self, data, id_reforma):
        self.data = data
        self.id_reforma = id_reforma

    def __repr__(self):
        return "<Pagamento %r>" % self.id_reforma 
