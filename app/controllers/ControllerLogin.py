from app.Facade import SQLAlchemy, BaseQuery, db, ModelUsuario

Usuario = ModelUsuario.Usuario

class ControllerLogin():
    def login(self,telefone,senha):
        g = Usuario.query.filter(Usuario.telefone == telefone).first()

        if g.senha == senha:
            return {'id':g.id ,'telefone':telefone, 'senha':senha}
        return False