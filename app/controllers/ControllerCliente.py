from app.Facade import SQLAlchemy, BaseQuery, db, ModelCliente, ModelPessoa, ModelUsuario, ModelProfissional

Cliente = ModelCliente.Cliente
Pessoa = ModelPessoa.Pessoa
Usuario = ModelUsuario.Usuario
Profissional = ModelProfissional.Profissional

class ControllerCliente():
    def inserirCliente(self,cpf,nome,telefone,senha):

        result = self.validarIntegridade(cpf,nome,telefone,senha)
        if result['sucesso'] is False:
            return result
        
        h = Usuario.query.filter(Usuario.telefone == telefone).first()
        i = Pessoa.query.filter(Pessoa.cpf == cpf).first()

        if h == None:
            if i == None:
                h = Usuario(telefone, senha)
                db.session.add(h)
                i = Pessoa.query.filter(Pessoa.cpf == cpf).first()# meramente uma busca para atualizar os dados do banco.(não tem uso real)
                i = Pessoa(cpf,nome,h.id)
                db.session.add(i)
                j = Cliente.query.filter(Cliente.id_pessoa == i.id).first()
                j = Cliente(i.id)
                db.session.add(j)
            else:
                return {'sucesso':False, 'mensagem':'cpf em uso.'}
        else:
            if i == None:
                return {'sucesso':False, 'mensagem':'telefone em uso.'}
            else:
                j = Cliente.query.filter(Cliente.id_pessoa == i.id).first()
                if j == None:
                    h = Usuario(telefone, senha)
                    db.session.add(h)
                    i = Pessoa.query.filter(Pessoa.cpf == cpf).first()# meramente uma busca para atualizar os dados do banco.(não tem uso real)
                    i = Pessoa(cpf,nome,h.id)
                    db.session.add(i)
                    j = Cliente.query.filter(Cliente.id_pessoa == i.id).first()
                    j = Cliente(i.id)
                    db.session.add(j)
                else:
                    return {'sucesso':False, 'mensagem':'cliente existente.'}
        db.session.commit()

        return {'sucesso':True, 'mensagem':'cliente cadastrado com sucesso.','id':j.id,'cpf':i.cpf,'telefone':h.telefone, 'nome':nome}

    def removerCliente(self,id):
        d = Cliente.query.get(id)
        if d == None:
            return {'sucesso':False, 'mensagem':'cliente não existe.'}

        e = Pessoa.query.get(d.id_pessoa)
        f = Usuario.query.get(e.id_usuario)
        p = Profissional.query.filter_by(id_pessoa=id).first()

        if p == None:
            db.session.delete(e)
            db.session.delete(f)

        db.session.delete(d)
        db.session.commit()
        return {'sucesso':True, 'mensagem':'cliente removido com sucesso.'}

    def retornarCliente(self,id):
        g = Cliente.query.get(id)
        if g == None:
            return {'sucesso':False, 'mensagem':'cliente não existe.'}
        h = Pessoa.query.get(str(g.id_pessoa))
        i = Usuario.query.get(h.id_usuario)

        return {'sucesso':True,'mensagem':'cliente retornado com sucesso.','id':g.id,'cpf':h.cpf,'nome':h.nome,'telefone':i.telefone}

    def retornarTodosClientes(self):
        g = Cliente.query.all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há clientes.'}

        lista = list()
        for i in range(len(g)):
            p = Pessoa.query.get(g[i].id_pessoa)
            u = Usuario.query.get(p.id_usuario)
            lista.append({'id':str(g[i].id),'cpf':p.cpf,'nome':p.nome,'telefone':u.telefone})

        return {'sucesso':True,'mensagem':'todos os clientes retornados com sucesso.','clientes':lista}

    def atualizarCliente(self,id,cpf,nome,telefone,senha):
        result = self.validarIntegridade(cpf,nome,telefone,senha)
        if result['sucesso'] is False:
            return result
        u = Cliente.query.get(id)
        if u == None:
            return {'sucesso':False, 'mensagem':'cliente não existe.'}

        v = Pessoa.query.get(u.id_pessoa)
        x = Usuario.query.get(v.id_usuario)

        v.cpf = cpf
        v.nome = nome
        x.telefone = telefone
        x.senha = senha
        db.session.commit()

        return {'sucesso':True,'mensagem':'cliente atualizado com sucesso.','id':u.id,'cpf':v.cpf,'telefone':x.telefone, 'nome':nome}
    
    def validarIntegridade(self,cpf,nome,telefone,senha):
        if cpf == None or cpf.strip() == "":
            return {'sucesso':False, 'mensagem':'cpf em branco.'}
        elif nome == None or nome.strip() == "":
            return {'sucesso':False, 'mensagem':'nome em branco.'}
        elif telefone == None or telefone.strip() == "":
            return {'sucesso':False, 'mensagem':'telefone em branco.'}
        elif senha == None or senha.strip() == "":
            return {'sucesso':False, 'mensagem':'senha em branco.'}
        return {'sucesso':True}