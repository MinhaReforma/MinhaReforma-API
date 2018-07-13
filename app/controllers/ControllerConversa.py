from app.Facade import SQLAlchemy, BaseQuery, db, ModelConversa, ModelMensagem

Conversa = ModelConversa.Conversa
Mensagem = ModelMensagem.Mensagem

class ControllerConversa():

    def retornarConversa(self,idr, idp):
        g = Conversa.query.filter(Conversa.id_reforma == idr, Conversa.id_profissional == idp).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'conversa não existe.'}
        
        lista = list()
        for mensa in g.mensagens:
            men = Mensagem.query.get(mensa.id)
            lista.append({'mensagem':men.mensagem, 'perfil':men.perfil, 'data':men.data, 'id':men.id})
    
        return {'sucesso':True,'mensagem':'conversa retornada com sucesso.','id':g.id,'id_reforma':g.id_reforma,'id_cliente':g.id_cliente, 'id_profissional':g.id_profissional, 'mensagens':lista}

    def retornarTodasConversas(self):
        g = Conversa.query.all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há conversas.'}

        lista = list()
        listamen= list()
        for i in range(len(g)):
            for mensa in g[i].mensagens:
                men = Mensagem.query.get(mensa.id)
                listamen.append({'mensagem':men.mensagem, 'perfil':men.perfil, 'data':men.data, 'id':men.id})
            lista.append({'id':g[i].id,'id_reforma':g[i].id_reforma,'id_cliente':g[i].id_cliente, 'id_profissional':g[i].id_profissional, 'mensagens':listamen})

        return {'sucesso':True,'mensagem':'todas as conversas retornados com sucesso.','conversas':lista}
    
#################################################### MENSAGEM ##############################################################

    def inserirMensagem(self, id_conversa, perfil, data, mensagem):

        g = Conversa.query.filter_by(id=id_conversa).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'conversa não existente.'}

        result = self.validarIntegridade(id_conversa, perfil, data, mensagem)
        if result['sucesso'] is False:
            return result

        h = Mensagem(id_conversa, perfil, data, mensagem)
        db.session.add(h)
        db.session.commit()

        return {'sucesso':True, 'mensagem':'Mensagem adicionada com sucesso', 'id':h.id, 'id_conversa':h.id_conversa, 'perfil':h.perfil, 'data':h.data, 'valor':h.mensagem}
    
    def validarIntegridade(self, id_conversa, perfil, data, mensagem):
        if id_conversa is None:
            return {'sucesso':False, 'mensagem':'id_conversa nulo.'}
        elif perfil is None:
            return {'sucesso':False, 'mensagem':'perfil nulo.'}
        elif data is None:
            return {'sucesso':False, 'mensagem':'data nulo.'}
        elif mensagem is None:
            return {'sucesso':False, 'mensagem':'mensagem nulo.'}
        
        return {'sucesso':True}