from app.Facade import SQLAlchemy, BaseQuery, db, ModelReforma, ModelReformaProfissional, ModelProfissional

Reforma = ModelReforma.Reforma
ReformaProfissional = ModelReformaProfissional.ReformaProfissional
Profissional = ModelProfissional.Profissional

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
        ReformaProfissional.query.filter_by(id_reforma=id).delete()
        db.session.commit()

        return {'sucesso':True, 'mensagem':'reforma removida com sucesso.'}

    def retornarReforma(self,id):
        g = Reforma.query.get(id)
        if g == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}
            
        h = ReformaProfissional.query.filter_by(id_reforma=id).all()
        lista = list()
        for profic in h:
            prof = Profissional.query.get(profic.id_profissional)
            lista.append(prof.id)            
        return {'sucesso':True, 'mensagem':'reforma retornada com sucesso.','id':g.id,'id_cliente':g.id_cliente,'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao, 'listaProfissionais':lista}

    def retornarTodasReformas(self):
        g = Reforma.query.all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há reformas.'}

        lista = list()
        listaprof = list()
        for i in range(len(g)):
            refprof = ReformaProfissional.query.filter_by(id_reforma=g[i].id_reforma)

            for profis in refprof:
                prof = Profissional.query.get(profis.id_profissional)
                listaprof.append(prof.id)
            lista.append({'id':g[i].id,'id_cliente':g[i].id_cliente,'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao, 'listaProfissionais':listaprof})#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco})

        return {'sucesso':True,'mensagem':'todos as reformas retornadas com sucesso.','reformas':lista}
                
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
        i = ReformaProfissional(id_reforma,id_profissional)
        db.session.add(i)   
        db.session.commit()
        return {'sucesso':True,'mensagem':'profissional adicionado com sucesso.','id_reforma':i.id_reforma,'id_profissional':i.id_profissional}

    # def retornarReformaProfissional(self,id):
    #     g = Reforma.query.get(id)
    #     if g == None:
    #         return {'sucesso':False, 'mensagem':'reforma não existe.'}
            
    #     h = ReformaProfissional.query.filter_by(id_reforma=id).all()
    #     lista = list()
    #     for profic in h:
    #         prof = Profissional.query.get(profic.id_profissional)
    #         lista.append(prof.id)            
    #     return {'sucesso':True, 'mensagem':'reforma retornada com sucesso.','id':g.id,'id_cliente':g.id_cliente,'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao, 'listaProfissionais':lista}