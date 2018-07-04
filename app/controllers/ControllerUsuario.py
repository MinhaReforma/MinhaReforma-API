from app.Facade import SQLAlchemy, BaseQuery, ModelUsuario

Usuario = ModelUsuario.Usuario

class ControllerUsuario():

    def inserirUsuario(self,telefone,senha):
        i = Usuario(telefone,senha)
        db.session.add(i)   
        db.session.commit()
        return True

    def removerUsuario(self,id):
        d = Usuario.query.get(id)
        db.session.delete(d)
        db.session.commit()
        return True

    def retornarTodosUsuarios(self):
        g = Usuario.query.all()
        lista = list()
        for i in range(len(g)):
            lista.append({'id':str(g[i].id),'telefone':g[i].telefone,'senha':g[i].senha})
        return lista

    def retornarUsuario(self,id):
        g = Usuario.query.get(id)
        result = {'id':g.id,'telefone':g.telefone,'senha':g.senha}
        if result:
            return result
        return False

    def atualizarUsuario(self,id,telefone,senha):
        u = Usuario.query.get(id)
        u.telefone = telefone
        u.senha = senha
        db.session.commit()
        return True
