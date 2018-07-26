from app.Facade import SQLAlchemy, BaseQuery, db, ModelReforma, ModelProfissional, ModelCliente, ModelConversa, ModelHabilidade, ModelReformaProfissional

Reforma = ModelReforma.Reforma
Profissional = ModelProfissional.Profissional
Cliente = ModelCliente.Cliente
Conversa = ModelConversa.Conversa
Habilidade = ModelHabilidade.Habilidade
ReformaProfissional = ModelReformaProfissional.ReformaProfissional

class ControllerReforma():

    def inserirReforma(self,id_cliente, datainicio, nome, descricao, status):

        result = self.validarIntegridade(id_cliente, datainicio, nome, descricao, status)
        if result['sucesso'] is False:
            return result

        i = Reforma(id_cliente,datainicio,nome,descricao,status)#,id_status,id_profissional,preco)
        db.session.add(i)   
        db.session.commit()

        return {'sucesso':True,'mensagem':'reforma cadastrada com sucesso.','id_cliente':i.id_cliente,'datainicio':i.datainicio,'nome':i.nome,'descricao':i.descricao,'status':i.status}

    def removerReforma(self,id):
        d = Reforma.query.get(id)
        if d == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}

        db.session.delete(d)
        db.session.commit()

        return {'sucesso':True, 'mensagem':'reforma removida com sucesso.'}

    def retornarReforma(self,id):
        g = Reforma.query.get(id)
        if g == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}
        
        precoTotal = 0
        lista = list()
        listaProfAcc = []
        for profic in g.profissionais:
            listhab = list()
            prof = Profissional.query.get(profic.id)
            for habil in prof.habilidades:
                hab = Habilidade.query.get(habil.id)
                listhab.append(hab.habilidade)
            
            #Lista para informar quais profissionais pelo id estão aceitos na reforma.
            detalhesProf = self.pegarDetalhesProfissionalReforma(prof.id, id)
            preco = detalhesProf[0]
            if detalhesProf[1] != None:
                listaProfAcc.append(detalhesProf[1])
            
            #adiciona o profissional a lista de profissionais.
            lista.append({'id':prof.id,'cpf':prof.pessoa.cpf,'nome':prof.pessoa.nome,'telefone':prof.pessoa.usuario.telefone, 'profissao': prof.profissao , 'habilidades':listhab, 'preco': preco})
            
            precoTotal += preco

        return {'sucesso':True, 'mensagem':'reforma retornada com sucesso.','id':g.id,'cliente':{'id':g.cliente.id,'cpf':g.cliente.pessoa.cpf,'nome':g.cliente.pessoa.nome,'telefone':g.cliente.pessoa.usuario.telefone},'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao, 'listaProfissionais':lista, 'status':g.status, 'precoTotal': precoTotal, 'listaProfissionaisAceitos': listaProfAcc}

    def retornarTodasReformas(self,status):
        g = Reforma.query.filter_by(status=status).all()
        if g == []:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):
            listaprof = list()
            for profis in g[i].profissionais:
                listhab = list()
                prof = Profissional.query.get(profis.id)
                listaprof.append({'id':prof.id,'cpf':prof.pessoa.cpf,'nome':prof.pessoa.nome,'telefone':prof.pessoa.usuario.telefone})
            lista.append({'id':g[i].id,'cliente':{'id':g[i].cliente.id,'cpf':g[i].cliente.pessoa.cpf,'nome':g[i].cliente.pessoa.nome,'telefone':g[i].cliente.pessoa.usuario.telefone},'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof, 'status':g[i].status})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todas as reformas retornadas com sucesso.','reformas':lista}
    
    def retornarTodasReformasCliente(self, id_cliente):
        g = Reforma.query.filter_by(id_cliente=id_cliente).all()
        if g == []:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):
            listaprof= list()
            for profis in g[i].profissionais:
                listhab = list()
                prof = Profissional.query.get(profis.id)
                listaprof.append({'id':prof.id,'cpf':prof.pessoa.cpf,'nome':prof.pessoa.nome,'telefone':prof.pessoa.usuario.telefone})
            lista.append({'id':g[i].id,'cliente':{'id':g[i].cliente.id,'cpf':g[i].cliente.pessoa.cpf,'nome':g[i].cliente.pessoa.nome,'telefone':g[i].cliente.pessoa.usuario.telefone},'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof, 'status':g[i].status})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todas as reformas retornadas com sucesso.','reformas':lista}

    def retornarTodasReformasProfissional(self, id_profissional):
        f = Profissional.query.filter_by(id=id_profissional).first()
        if f == None:
            return {'sucesso':False, 'mensagem':'profissional não existente.'}
        g = f.reformas
        if g == []:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):
            listaprof= list()
            for profis in g[i].profissionais:
                listhab = list()
                prof = Profissional.query.get(profis.id)
                listaprof.append({'id':prof.id,'cpf':prof.pessoa.cpf,'nome':prof.pessoa.nome,'telefone':prof.pessoa.usuario.telefone})
            lista.append({'id':g[i].id,'cliente':{'id':g[i].cliente.id,'cpf':g[i].cliente.pessoa.cpf,'nome':g[i].cliente.pessoa.nome,'telefone':g[i].cliente.pessoa.usuario.telefone},'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof, 'status':g[i].status})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todas as reformas retornadas com sucesso.','reformas':lista}
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao,status):#, id_status,id_profissional,preco)   
        result = self.validarIntegridade(id_cliente,datainicio,nome,descricao,status)
        if result['sucesso'] is False:
            return result

        u = Reforma.query.get(id)
        if u == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}

        u.id_cliente = id_cliente
        u.datainicio = datainicio
        u.nome = nome
        u.descricao = descricao
        u.status = status
        #u.id_status = id_status
        #u.id_profissional = id_profissional
        #u.preco = preco
        db.session.commit()

        return {'sucesso':True,'mensagem':'reforma atualizada com sucesso.','id':u.id,'id_cliente':u.id_cliente ,'datainicio':u.datainicio, 'nome':u.nome, 'descricao':u.descricao, 'status':u.status}
    
    def validarIntegridade(self,id_cliente, datainicio, nome, descricao, status):
        if id_cliente == None:
            return {'sucesso':False, 'mensagem':'id_cliente em branco.'}
        elif datainicio == None:
            return {'sucesso':False, 'mensagem':'datainicio em branco.'}
        elif nome == None or nome.strip() == "":
            return {'sucesso':False, 'mensagem':'nome em branco.'}
        elif descricao == None or descricao.strip() == "":
            return {'sucesso':False, 'mensagem':'descricao em branco.'}
        elif status == None or status.strip() == "":
            return {'sucesso':False, 'mensagem':'status em branco.'}
        return {'sucesso':True}

    def pegarDetalhesProfissionalReforma(self, idP, idR):
        p = ReformaProfissional.query.filter(ReformaProfissional.id_profissional == idP, ReformaProfissional.id_reforma == idR).first()
        if p == None:
            return 0
        return p.preco if p.preco != None else 0, p.id if p.status == "aceito" else None
    
######################################################################### REFORMA PROFISSIONAL ########################################################################################################################

    def inserirReformaProfissional(self,id_reforma, id_profissional):

        reforma = Reforma.query.get(id_reforma)
        profissional = Profissional.query.get(id_profissional)

        if profissional in reforma.profissionais:
            return {'sucesso':False, 'mensagem':'profissional existente na reforma.'}

        h = Conversa.query.filter(Conversa.id_reforma == reforma.id, Conversa.id_profissional == profissional.id).first()
        if h == None:
            h = Conversa(reforma.id, reforma.id_cliente, profissional.id)
            db.session.add(h)
            db.session.commit()

        reforma.profissionais.append(profissional)
        db.session.add(reforma)   
        db.session.commit()
        return {'sucesso':True,'mensagem':'profissional adicionado com sucesso.','id_reforma':reforma.id,'id_profissional':profissional.id}
    
    def alterarReformaProfissional(self,id_reforma, id_profissional, status):

        reformaProfissional = ReformaProfissional.query.filter(ReformaProfissional.id_profissional == id_profissional,ReformaProfissional.id_reforma == id_reforma).first()

        if reformaProfissional == None:
            return {'sucesso':False, 'mensagem':'profissional não existe na reforma.'}

        reformaProfissional.status = status
        db.session.add(reformaProfissional)
        db.session.commit()
        return {'sucesso':True,'mensagem':'status da relação alterada com sucesso.','id_reforma':reformaProfissional.id_reforma,'id_profissional':reformaProfissional.id_profissional, 'status': reformaProfissional.status}
    
    def novoStatus(self, id_reforma, status):

        reforma = Reforma.query.get(id_reforma)
        reformaProfissional = ReformaProfissional.query.filter_by(id_reforma=id_reforma).all()

        if reforma == None:
            return {'sucesso':False, 'mensagem':'reforma inexistente.'}

        for relacao in reformaProfissional:
            if relacao.status != 'aceito':
                db.session.delete(relacao)
        
        reforma.status = status
        db.session.commit()
        return {'sucesso':True, 'mensagem':'status alterado com sucesso', 'id_reforma':reforma.id, 'status':reforma.status}