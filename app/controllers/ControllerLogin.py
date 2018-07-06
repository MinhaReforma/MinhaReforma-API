from app.Facade import SQLAlchemy, BaseQuery, db, ModelUsuario

Usuario = ModelUsuario.Usuario

class ControllerLogin():
    def login(self,telefone,senha):

        result = self.validarIntegridade(telefone,senha)
        if result['sucesso'] is False:
            return result
         
        g = Usuario.query.filter(Usuario.telefone == telefone).first()
        
        return self.validarSenha(g, senha)

    def validarIntegridade(self, telefone, senha):
        if telefone == None or senha == None:
            return {'sucesso':False,'tipo':'telefone ou senha em branco.'}
        #elif type(telefone) is not int:
         #   return {'sucesso':False,'tipo':'telefone não é inteiro'}
        return {'sucesso':True}
    
    def validarSenha(self, valor, senha):
        if valor == None:
            pass
        elif valor.senha == senha:
            return {'sucesso':True,'id':valor.id ,'telefone':valor.telefone, 'senha':valor.senha}
        return {'sucesso':False,'tipo':'telefone ou senha inválido.'}