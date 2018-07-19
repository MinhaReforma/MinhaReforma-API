from app.Facade import SQLAlchemy, BaseQuery, db, ModelProfissional, ModelPessoa, ModelUsuario, ModelHabilidade, ModelCliente
import hashlib

Profissional = ModelProfissional.Profissional
Pessoa = ModelPessoa.Pessoa
Usuario = ModelUsuario.Usuario
Habilidade = ModelHabilidade.Habilidade
Cliente = ModelCliente.Cliente

class ControllerProfissional():

    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades, profissao):

        result = self.validarIntegridade(cpf,nome,telefone,senha,habilidades, profissao)
        if result['sucesso'] is False:
            return result
        
        h = Usuario.query.filter(Usuario.telefone == telefone).first()
        i = Pessoa.query.filter(Pessoa.cpf == cpf).first()

        m = hashlib.sha256()
        m.update(senha.encode('utf8'))
        m.digest()
        senhaHash = m.hexdigest()
        
        if h == None:
            if i == None:
                h = Usuario(telefone, senhaHash)
                db.session.add(h)
                i = Pessoa.query.filter(Pessoa.cpf == cpf).first()# meramente uma busca para atualizar os dados do banco.(não tem uso real)
                i = Pessoa(cpf,nome,h.id)
                db.session.add(i)
                j = Profissional.query.filter(Profissional.id_pessoa == i.id).first()
                j = Profissional(i.id,profissao)
                db.session.add(j)
            else:
                return {'sucesso':False, 'mensagem':'cpf em uso.'}
        else:
            if i == None:
                return {'sucesso':False, 'mensagem':'telefone em uso.'}
            else:
                j = Profissional.query.filter(Profissional.id_pessoa == i.id).first()
                if j == None:
                    h = Usuario(telefone, senhaHash)
                    db.session.add(h)
                    i = Pessoa.query.filter(Pessoa.cpf == cpf).first() # meramente uma busca para atualizar os dados do banco.(não tem uso real)
                    i = Pessoa(cpf,nome,h.id)
                    db.session.add(i)
                    j = Profissional.query.filter(Profissional.id_pessoa == i.id).first()
                    j = Profissional(i.id,profissao)
                    db.session.add(j)
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
            else:
                k = Habilidade.query.filter_by(habilidade=hab).first()
   
            j.habilidades.append(k)

        db.session.commit()

        return {'sucesso':True,'mensagem':'profissional cadastrado com sucesso.','id':j.id,'cpf':i.cpf,'telefone':h.telefone, 'profissao':j.profissao, 'habilidades':habilidades}

    def removerProfissional(self,id):
        d = Profissional.query.get(id)
        if d == None:
            return {'sucesso':False, 'mensagem':'profissional não existe.'}

        e = Pessoa.query.get(d.id_pessoa)
        f = Usuario.query.get(e.id_usuario)
        c = Cliente.query.filter_by(id_pessoa=e.id).first()

        if c == None:
            db.session.delete(f)
        
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
            
        return {'sucesso':True,'mensagem':'profissional retornado com sucesso.','id':g.id,'cpf':h.cpf,'nome':h.nome,'telefone':i.telefone, 'profissao':g.profissao, 'habilidades':lista}

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
            lista.append({'id':g[i].id,'cpf':p.cpf,'nome':p.nome,'telefone':u.telefone, 'profissao':g[i].profissao,'habilidades':listhab})
        return {'sucesso':True,'mensagem':'todos os profissionais retornados com sucesso.','profissionais':lista}

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades, profissao):
        result = self.validarIntegridade(cpf,nome,telefone,senha,habilidades, profissao)
        if result['sucesso'] is False:
            return result
        u = Profissional.query.get(id)
        if u == None:
            return {'sucesso':False, 'mensagem':'profissional não existe.'}

        v = Pessoa.query.get(u.id_pessoa)
        x = Usuario.query.get(v.id_usuario)

        u.profissao = profissao
        v.cpf = cpf
        v.nome = nome
        x.telefone = telefone
        x.senha = senha

        u.habilidades.clear()
        for hab in habilidades:
            tudo = Habilidade.query.all()
            
            sidekick = str()
            for um in tudo:
                if hab == um.habilidade:
                    sidekick = um.habilidade
                    break
            
            if hab != sidekick:
                k = Habilidade(hab)
                db.session.add(k)
            else:
                k = Habilidade.query.filter_by(habilidade=hab).first()
            
            u.habilidades.append(k)

        db.session.commit()
        
        return {'sucesso':True,'mensagem':'profissional atualizado com sucesso.','id':u.id,'cpf':v.cpf,'telefone':x.telefone,'habilidades':habilidades}
    
    def validarIntegridade(self,cpf,nome,telefone,senha,habilidades, profissao):
        if cpf == None or cpf.strip() == "":
            return {'sucesso':False, 'mensagem':'cpf em branco.'}
        elif nome == None or nome.strip() == "":
            return {'sucesso':False, 'mensagem':'nome em branco.'}
        elif telefone == None or telefone.strip() == "":
            return {'sucesso':False, 'mensagem':'telefone em branco.'}
        elif senha == None or senha.strip() == "":
            return {'sucesso':False, 'mensagem':'senha em branco.'}
        elif habilidades == list() or habilidades == None:
            return {'sucesso':False, 'mensagem':'habilidades em branco.'}
        elif profissao == None or profissao.strip() == "":
            return {'sucesso':False, 'mensagem':'profissao em branco.'}
        return {'sucesso':True}
        