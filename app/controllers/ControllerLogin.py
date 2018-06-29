from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db

from app.models.ModelUsuario import Usuario

def login(telefone,senha):
    try:
        g = Usuario.query.filter(Usuario.telefone == telefone).first()

        if g.senha == senha:
            return {'id':g.id ,'telefone':telefone, 'senha':senha}
        return False
    except:
        return False