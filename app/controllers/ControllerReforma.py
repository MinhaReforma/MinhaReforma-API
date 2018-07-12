from app.Facade import SQLAlchemy, BaseQuery, db, ModelReforma, ModelProfissional, ModelCliente, ModelConversa

Reforma = ModelReforma.Reforma
Profissional = ModelProfissional.Profissional
Cliente = ModelCliente.Cliente
Conversa = ModelConversa.Conversa

class ControllerReforma():

    def inserirReforma(self,id_cliente, datainicio, nome, descricao):

        result = self.validarIntegridade(id_cliente, datainicio, nome, descricao)
        if result['sucesso'] is False:
            return result

        i = Reforma(id_cliente,datainicio,nome,descricao)#,id_status,id_profissional,preco)
        db.session.add(i)   
        db.session.commit()

        return {'sucesso':True,'mensagem':'reforma cadastrada com sucesso.','id_cliente':i.id_cliente,'datainicio':i.datainicio,'nome':i.nome,'descricao':i.descricao}

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
            
        lista = list()
        for profic in h:
            listhab = list()
            prof = Profissional.query.get(profic.id_profissional)
            for habil in prof.habilidades:
                hab = Habilidade.query.get(habil.id_habilidade)
                listhab.append(hab.habilidade)
            lista.append({'id':prof.id,'cpf':prof.cpf,'nome':prof.nome,'telefone':prof.telefone, 'habilidade':listhab})            
        return {'sucesso':True, 'mensagem':'reforma retornada com sucesso.','id':g.id,'cliente':{'id':g.cliente.id,'cpf':g.cliente.cpf,'nome':g.cliente.nome,'telefone':g.cliente.telefone},'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao, 'listaProfissionais':lista}

    def retornarTodasReformas(self):
        g = Reforma.query.all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):

            for profis in g[i].profissionais:
                listhab = list()
                prof = Profissional.query.get(profis.id)
                for habil in prof.habilidades:
                    hab = Habilidade.query.get(habil.id_habilidade)
                    listhab.append(hab.habilidade)
                listaprof.append({'id':prof.id,'cpf':prof.cpf,'nome':h.nome,'telefone':i.telefone, 'habilidades':listhab})
            lista.append({'id':g[i].id,'cliente':{'id':g.cliente.id,'cpf':g.cliente.cpf,'nome':g.cliente.nome,'telefone':g.cliente.telefone},'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todas as reformas retornadas com sucesso.','reformas':lista}
    
    def retornarTodasReformasCliente(self, id_cliente):
        g = Reforma.query.filter_by(id_cliente==id_cliente).all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):

            for profis in g[i].profissionais:
                listhab = list()
                prof = Profissional.query.get(profis.id)
                for habil in prof.habilidades:
                    hab = Habilidade.query.get(habil.id_habilidade)
                    listhab.append(hab.habilidade)
                listaprof.append({'id':prof.id,'cpf':prof.cpf,'nome':h.nome,'telefone':i.telefone, 'habilidades':listhab})
            lista.append({'id':g[i].id,'cliente':{'id':g.cliente.id,'cpf':g.cliente.cpf,'nome':g.cliente.nome,'telefone':g.cliente.telefone},'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todas as reformas retornadas com sucesso.','reformas':lista}

    def retornarTodasReformasProfissional(self, id_profissional):
        f = Profissional.query.filter_by(id==id_profissional).first()
        g = f.reformas
        if g == None:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):

            for profis in g[i].profissionais:
                listhab = list()
                prof = Profissional.query.get(profis.id)
                for habil in prof.habilidades:
                    hab = Habilidade.query.get(habil.id_habilidade)
                    listhab.append(hab.habilidade)
                listaprof.append({'id':prof.id,'cpf':prof.cpf,'nome':h.nome,'telefone':i.telefone, 'habilidades':listhab})
            lista.append({'id':g[i].id,'cliente':{'id':g.cliente.id,'cpf':g.cliente.cpf,'nome':g.cliente.nome,'telefone':g.cliente.telefone},'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todas as reformas retornadas com sucesso.','reformas':lista}
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao):#, id_status,id_profissional,preco)   
        result = self.validarIntegridade(id,id_cliente,datainicio,nome,descricao)
        if result['sucesso'] is False:
            return result

        u = Reforma.query.get(id)
        if u == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}

        u.id_cliente = id_cliente
        u.datainicio = datainicio
        u.nome = nome
        u.descricao = descricao
        #u.id_status = id_status
        #u.id_profissional = id_profissional
        #u.preco = preco
        db.session.commit()

        return {'sucesso':True,'mensagem':'reforma atualizada com sucesso.','id':u.id,'id_cliente':u.id_cliente ,'datainicio':u.datainicio, 'nome':u.nome, 'descricao':u.descricao}
    
    def validarIntegridade(self,id_cliente, datainicio, nome, descricao):
        if id_cliente is None:
            return {'sucesso':False, 'mensagem':'id_cliente em branco.'}
        elif datainicio is None:
            return {'sucesso':False, 'mensagem':'datainicio em branco.'}
        elif nome is None:
            return {'sucesso':False, 'mensagem':'nome em branco.'}
        elif descricao is None:
            return {'sucesso':False, 'mensagem':'descricao em branco.'}
        return {'sucesso':True}

######################################################################### REFORMA PROFISSIONAL ########################################################################################################################

    def inserirReformaProfissional(self,id_reforma, id_profissional):

        ir = Reforma.query.get(id_reforma)
        ip = Profissional.query.get(id_profissional)

        if ip in ir.profissionais:
            return {'sucesso':True, 'mensagem':'profissional existente na reforma'}

        h = Conversa.query.filter(Conversa.id_reforma == ir, Conversa.id_profissional == ip).first()
        if h == None:
            h = Conversa(ir, ir.id_cliente, ip)
            db.session.add(h)
            db.session.commit()

        ir.profissionais.append(ip)
        db.session.add(ir)   
        db.session.commit()
        return {'sucesso':True,'mensagem':'profissional adicionado com sucesso.','id_reforma':ir.id,'id_profissional':ip.id}