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
        if telefone == None or senha == None or telefone.strip() == "" or senha.strip() == "":
            return {'sucesso':False,'mensagem':'telefone ou senha em branco.'}
        if tipoPessoa == None or tipoPessoa.strip() == "":
            return {'sucesso':False, 'mensagem':'tipoPessoa em branco'}
        elif tipoPessoa != 'cliente' and tipoPessoa != 'profissional':
            return {'sucesso':False, 'mensagem':'tipoPessoa deve ser cliente ou profissional'}

        return {'sucesso':True}
    
    def validarSenha(self, valor, senha, tipoPessoa):
        m = hashlib.sha256()
        m.update(senha)
        m.digest()
        senhaHash = m.hexdigest();
        if valor == None:
            pass
        elif valor.senha == senhaHash:
            result = self.recuperarIds(valor,tipoPessoa)
            if result['sucesso']:
                return {'sucesso':True,'mensagem':'logado com sucesso','id_usuario':valor.id, 'id_pessoa':result['idPes'],'id_perfil':result['idRes'] ,'telefone':valor.telefone}
            return result
        return {'sucesso':False,'mensagem':'telefone ou senha incorreto.'}
    
    def recuperarIds(self,valor, tipoPessoa):
        p = Pessoa.query.filter(Pessoa.id_usuario == valor.id).first()

        if tipoPessoa == 'cliente':
            Cliente = ModelCliente.Cliente
            r = Cliente.query.filter(Cliente.id_pessoa == p.id).first()
            result = self.validarPerfil(r)

        elif tipoPessoa == 'profissional':
            Profissional = ModelProfissional.Profissional
            r = Profissional.query.filter(Profissional.id_pessoa == p.id).first()
            result = self.validarPerfil(r)

        if result['sucesso']:
            return {'sucesso':True,'idPes':p.id,'idRes':r.id}

        return result
    
    def validarPerfil(self,perfil):
        if perfil == None:
            return {'sucesso':False, 'mensagem':'usuário não cadastrado.'}
        return {'sucesso':True}