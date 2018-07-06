from app.Facade import SQLAlchemy, BaseQuery, db, ModelUsuario, ModelPessoa, ModelCliente, ModelProfissional

Usuario = ModelUsuario.Usuario
Pessoa = ModelPessoa.Pessoa

class ControllerLogin():
    def login(self,telefone,senha,tipoPessoa):
        result = self.validarIntegridade(telefone,senha, tipoPessoa)
        
        if result['sucesso'] is False:
            return result
         
        g = Usuario.query.filter(Usuario.telefone == telefone).first()
        
        return self.validarSenha(g, senha, tipoPessoa)

    def validarIntegridade(self, telefone, senha, tipoPessoa):
        if telefone == None or senha == None:
            return {'sucesso':False,'mensagem':'telefone ou senha em branco.'}
        #elif type(telefone) is not int:
         #   return {'sucesso':False,'mensagem':'telefone não é inteiro'}
        if tipoPessoa == None:
            return {'sucesso':False, 'mensagem':'tipoPessoa em branco'}
        elif tipoPessoa == 'cliente' or tipoPessoa == 'profissional':
            pass

        return {'sucesso':True}
    
    def validarSenha(self, valor, senha, tipoPessoa):
        if valor == None:
            pass
        elif valor.senha == senha:
            result = self.recuperarIds(valor,tipoPessoa)
            return {'sucesso':True,'mensagem':'logado com sucesso','id_usuario':valor.id, 'id_pessoa':result['idP'],'id_perfil':result['idR'] ,'telefone':valor.telefone, 'senha':valor.senha}
        return {'sucesso':False,'mensagem':'telefone ou senha inválido.'}
    
    def recuperarIds(self,valor, tipoPessoa):
        p = Pessoa.query.filter(Pessoa.id_usuario == valor.id).first()
        if tipoPessoa == 'cliente':
            Cliente = ModelCliente.Cliente
            r = Cliente.query.filter(Cliente.id_pessoa == p.id).first()
        elif tipoPessoa == 'profissional':
            Profissional = ModelProfissional.Profissional
            r = Profissional.query.filter(Profissional.id_pessoa == p.id).first()
        return {'idP':p.id,'idR':r.id}