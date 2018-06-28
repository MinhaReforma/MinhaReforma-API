from app import db

class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)

    def __init__(self, id_usuario):
        self.id_usuario = id_usuario

    def __repr__(self):
        return "<Cliente %r>" % self.id_usuario
