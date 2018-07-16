from app.Facade import SQLAlchemy, BaseQuery, ModelUsuario

Usuario = ModelUsuario.Usuario

class ControllerUsuario():

    def inserirUsuario(self,telefone,senha):

        result = self.validarIntegridade(telefone,senha)
        if result['sucesso'] is False:
            return result

        i = Usuario(telefone,senha)
        db.session.add(i)   
        db.session.commit()
        return {'sucesso':True, 'mensagem':'usuário inserido.','telefone':i.telefone}

    def removerUsuario(self,id):
        d = Usuario.query.get(id)

        if d == None:
            return {'sucesso':False, 'mensagem':'usuário não existe.'}

        db.session.delete(d)
        db.session.commit()
        return {'sucesso':True, 'mensagem':'usuário removido com sucesso.'}


    def retornarTodosUsuarios(self):
        g = Usuario.query.all()

        if g == None:
            return {'sucesso':False, 'mensagem':'não há usuários.'}

        lista = list()
        for i in range(len(g)):
            lista.append({'id':g[i].id,'telefone':g[i].telefone})

        return {'sucesso':True,'mensagem':'todos os usuarios retornados com sucesso.','usuarios':lista}

    def retornarUsuario(self,id):
        g = Usuario.query.get(id)
        if g == None:
            return {'sucesso':False, 'mensagem':'usuário não existe.'}

        return {'sucesso':True,'mensagem':'usuário retornado com sucesso.','id':g.id,'telefone':g.telefone}

    def atualizarUsuario(self,id,telefone,senha):

        result = self.validarIntegridade(telefone,senha)
        if result['sucesso'] is False:
            return result

        u = Usuario.query.get(id)
        if u == None:
            return {'sucesso':False, 'mensagem':'usuário não existe.'}

        u.telefone = telefone
        u.senha = senha
        db.session.commit()

        return {'sucesso':True,'mensagem':'usuário atualizado com sucesso.','id':u.id,'telefone':u.telefone}
    
    def validarIntegridade(self,telefone,senha):
        if telefone == None or telefone.strip() == "":
            return {'sucesso':False, 'mensagem':'telefone em branco.'}
        elif senha == None or senha.strip() == "":
            return {'sucesso':False, 'mensagem':'senha em branco.'}
        return {'sucesso':True}