from app.Facade import SQLAlchemy, BaseQuery, db, ModelConversa, ModelMensagem, ModelReformaProfissional

Conversa = ModelConversa.Conversa
Mensagem = ModelMensagem.Mensagem
ReformaProfissional = ModelReformaProfissional.ReformaProfissional

class ControllerConversa():

    def retornarConversa(self,idr, idp):
        g = Conversa.query.filter(Conversa.id_reforma == idr, Conversa.id_profissional == idp).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'conversa não existe.'}
        
        lista = list()
        for mensa in g.mensagens:
            lista.append({'mensagem':mensa.mensagem, 'perfil':mensa.perfil, 'data':mensa.data, 'id':mensa.id, 'preco': mensa.preco, 'nivelPreco':mensa.nivelPreco})
    
        return {'sucesso':True,'mensagem':'conversa retornada com sucesso.','id':g.id,'id_reforma':g.id_reforma,'id_cliente':g.id_cliente, 'id_profissional':g.id_profissional, 'preco':g.preco, 'mensagens':lista}

    def retornarTodasConversas(self):
        g = Conversa.query.all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há conversas.'}

        lista = list()
        listamen= list()
        for i in range(len(g)):
            for mensa in g[i].mensagens:
                listamen.append({'mensagem':mensa.mensagem, 'perfil':mensa.perfil, 'data':mensa.data, 'id':mensa.id, 'preco':mensa.preco, 'nivelPreco':mensa.nivelPreco})
            if g.preco == None:
                g.preco = 0
            lista.append({'id':g[i].id,'id_reforma':g[i].id_reforma,'id_cliente':g[i].id_cliente,'id_profissional':g[i].id_profissional,'preco':g[i].preco,'mensagens':listamen})

        return {'sucesso':True,'mensagem':'todas as conversas retornados com sucesso.','conversas':lista}
    
#################################################### MENSAGEM ##############################################################

    def inserirMensagem(self, id_conversa, perfil, data, mensagem, preco=0, nivelPreco=0):

        g = Conversa.query.filter_by(id=id_conversa).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'conversa não existente.'}

        result = self.validarIntegridade(id_conversa, perfil, data, mensagem)
        if result['sucesso'] is False:
            return result
        
        db.session.add(g)
        h = Mensagem(id_conversa, perfil, data, mensagem, preco, nivelPreco)
        db.session.add(h)
        db.session.commit()

        return {'sucesso':True, 'mensagem':'Mensagem adicionada com sucesso', 'id':h.id, 'id_conversa':h.id_conversa, 'perfil':h.perfil, 'data':h.data, 'valor':h.mensagem, 'preco':h.preco, 'nivelPreco':h.nivelPreco}
    
    def atualizarMensagem(self, id_mensagem, nivelPreco=0):

        g = Mensagem.query.filter_by(id=id_mensagem).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'mensagem não existente.'}
        
        h = Conversa.query.filter_by(id= g.id_conversa).first()

        for i in h.mensagens:
            i.nivelPreco = 0
            db.session.commit()

        g.nivelPreco = nivelPreco

        if nivelPreco == 2:
            i = ReformaProfissional.query.filter(ReformaProfissional.id_profissional == h.id_profissional, ReformaProfissional.id_reforma == h.id_profissional).first()
            i.preco = g.preco
        
        db.session.commit()

        return {'sucesso':True, 'mensagem':'Mensagem adicionada com sucesso', 'id':g.id, 'id_conversa':g.id_conversa, 'perfil':g.perfil, 'data':g.data, 'valor':g.mensagem, 'preco':g.preco, 'nivelPreco': g.nivelPreco}
    
    def validarIntegridade(self, id_conversa, perfil, data, mensagem):
        if id_conversa == None or id_conversa.strip() == "":
            return {'sucesso':False, 'mensagem':'id_conversa nulo.'}
        elif perfil == None or perfil.strip() == "":
            return {'sucesso':False, 'mensagem':'perfil nulo.'}
        elif data == None or data.strip() == "":
            return {'sucesso':False, 'mensagem':'data nulo.'}
        elif mensagem == None or mensagem.strip() == "":
            return {'sucesso':False, 'mensagem':'mensagem nulo.'}
        
        return {'sucesso':True}