from app.Facade import SQLAlchemy, BaseQuery, db, ModelProfissional, ModelPessoa, ModelUsuario, ModelHabilidade, ModelCliente

Profissional = ModelProfissional.Profissional
Pessoa = ModelPessoa.Pessoa
Usuario = ModelUsuario.Usuario
Habilidade = ModelHabilidade.Habilidade
Cliente = ModelCliente.Cliente

class ControllerProfissional():

    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades):

        result = self.validarIntegridade(cpf,nome,telefone,senha,habilidades)
        if result['sucesso'] is False:
            return result
        
        h = Usuario.query.filter(Usuario.telefone == telefone).first()
        if h == None:
            h = Usuario(telefone, senha)
            db.session.add(h)
            #db.session.commit()
        
        i = Pessoa.query.filter(Pessoa.cpf == cpf).first()
        if i == None:
            i = Pessoa(cpf,nome,h.id)
            db.session.add(i)
            #db.session.commit()
        
        j = Profissional.query.filter(Profissional.id_pessoa == i.id).first()
        if j == None:
            j = Profissional(i.id)
            db.session.add(j)
            #db.session.commit()
        else:
            return {'sucesso':False, 'mensagem':'profissional existente.'}

        for hab in habilidades:
            tudo = Habilidade.query.all()

            sidekick = str()
            for um in tudo: #Verifica se habilidade existe na tabela de Habilidade
                if hab == um.habilidade:
                    sidekick = um.habilidade
                    break

            if hab != sidekick:# se não existir, adiciona na tabela
                k = Habilidade(hab)
                db.session.add(k)
                db.session.commit()
            else:
                k = hab
                
            j.habilidades.append(k)
            db.session.commit()

        db.session.commit()

        return {'sucesso':True,'mensagem':'profissional cadastrado com sucesso.','id':j.id,'cpf':i.cpf,'telefone':h.telefone,'habilidades':habilidades}

    def removerProfissional(self,id):
        d = Profissional.query.get(id)
        if d == None:
            return {'sucesso':False, 'mensagem':'profissional não existe.'}

        e = Pessoa.query.get(d.id_pessoa)
        f = Usuario.query.get(e.id_usuario)
        c = Cliente.query.filter_by(id_pessoa=e.id).first()

        if c == None:
            db.session.delete(e)
            #db.session.commit()
            db.session.delete(f)
            #db.session.commit()
        
        db.session.delete(d)
        db.session.commit()

        return {'sucesso':True, 'mensagem':'profissional removido com sucesso.'}

    def retornarProfissional(self,id):
        g = Profissional.query.get(id)
        if g == None:
            return {'sucesso':False, 'mensagem':'profissional não existe.'}
        h = Pessoa.query.get(str(g.id_pessoa))
        i = Usuario.query.get(h.id_usuario)

        lista = list()

        for habil in g.habilidades:
            hab = Habilidade.query.get(habil.id)
            lista.append(hab.habilidade)
            
        return {'sucesso':True,'mensagem':'profissional retornado com sucesso.','id':g.id,'cpf':h.cpf,'nome':h.nome,'telefone':i.telefone, 'habilidades':lista}

    def retornarTodosProfissionais(self):
        g = Profissional.query.all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há profissionais.'}

        lista = list()
        listhab = list()

        for i in range(len(g)):
            p = Pessoa.query.get(g[i].id_pessoa)
            u = Usuario.query.get(p.id_usuario)

            for habil in g[i].habilidades:
                hab = Habilidade.query.get(habil.id)
                listhab.append(hab.habilidade)
            lista.append({'id':g[i].id,'cpf':p.cpf,'nome':p.nome,'telefone':u.telefone,'habilidades':listhab})
        return {'sucesso':True,'mensagem':'todos os profissionais retornados com sucesso.','profissionais':lista}

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades):
        result = self.validarIntegridade(cpf,nome,telefone,senha,habilidades)
        if result['sucesso'] is False:
            return result
        u = Profissional.query.get(id)
        if u == None:
            return {'sucesso':False, 'mensagem':'profissional não existe.'}

        v = Pessoa.query.get(u.id_pessoa)
        x = Usuario.query.get(v.id_usuario)

        v.cpf = cpf
        v.nome = nome
        x.telefone = telefone
        x.senha = senha

        #ProfissionalHabilidade.query.filter_by(id_profissional=id).delete()
        u.habilidades.clear()
        for hab in habilidades:
            tudo = Habilidade.query.all()
            
            sidekick=str()
            for um in tudo:
                if hab == um.habilidade:
                    sidekick = um.habilidade
                    break

            if hab != sidekick:
                k = Habilidade(hab)
                db.session.add(k)
                db.session.commit()
            else:
                k = hab

            u.habilidades.append(k)
            db.session.commit()

        db.session.commit()
        
        return {'sucesso':True,'mensagem':'profissional atualizado com sucesso.','id':u.id,'cpf':v.cpf,'telefone':x.telefone,'habilidades':habilidades}
    
    def validarIntegridade(self,cpf,nome,telefone,senha,habilidades):
        if cpf is None or cpf.strip() == "":
            return {'sucesso':False, 'mensagem':'cpf em branco.'}
        elif nome is None or nome.strip() == "":
            return {'sucesso':False, 'mensagem':'nome em branco.'}
        elif telefone is None or telefone.strip() == "":
            return {'sucesso':False, 'mensagem':'telefone em branco.'}
        elif senha is None or senha.strip() == "":
            return {'sucesso':False, 'mensagem':'senha em branco.'}
        elif habilidades == list() or habilidades == None:
            return {'sucesso':False, 'mensagem':'habilidades em branco.'}
        return {'sucesso':True}
        