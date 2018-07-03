from app.Facade import SQLAlchemy, BaseQuery, db, ModelUsuario
# from flask_sqlalchemy import SQLAlchemy, BaseQuery
# from app import db

# from app.models.ModelUsuario import Usuario

Usuario = ModelUsuario.Usuario

class ControllerLogin():
    def login(telefone,senha):
        g = Usuario.query.filter(Usuario.telefone == telefone).first()

        if g.senha == senha:
            return {'id':g.id ,'telefone':telefone, 'senha':senha}
        return False