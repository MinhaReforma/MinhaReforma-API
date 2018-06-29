from app.Facade import SQLAlchemy, BaseQuery, ModelUsuario
#from flask_sqlalchemy import SQLAlchemy, BaseQuery
#from app import db

#from app.models.ModelUsuario import Usuario

Usuario = ModelUsuario.Usuario

class ControllerUsuario():

    def inserirUsuario(self,telefone,senha):
        try:
            i = Usuario(telefone,senha)
            db.session.add(i)   
            db.session.commit()
            return True
        except:
            return False

    def removerUsuario(self,id):
        try:
            d = Usuario.query.get(id)
            db.session.delete(d)
            db.session.commit()
            return True
        except:
            return False

    def retornarTodosUsuarios(self):
        try:
            g = Usuario.query.all()
            lista = list()
            for i in range(len(g)):
                lista.append({'id':str(g[i].id),'telefone':g[i].telefone,'senha':g[i].senha})
            return lista
        except:
            return False

    def retornarUsuario(self,id):
        try:
            g = Usuario.query.get(id)
            result = {'id':g.id,'telefone':g.telefone,'senha':g.senha}
            if result:
                return result
            return False
        except:
            return False

    def atualizarUsuario(self,id,telefone,senha):
        try:
            u = Usuario.query.get(id)
            u.telefone = telefone
            u.senha = senha
            db.session.commit()
            return True
        except:
            return False
