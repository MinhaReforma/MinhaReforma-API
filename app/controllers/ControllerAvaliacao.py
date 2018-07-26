from app.Facade import SQLAlchemy, BaseQuery, db, ModelAvaliacao, ModelUsuario

Avaliacao = ModelAvaliacao.Avaliacao
Usuario = ModelUsuario.Usuario

class ControllerAvaliacao():
    def inserirAvaliacao(self,id_avaliador,id_avaliado,mensagem,nota, tipo):

        result = self.validarIntegridade(id_avaliador,id_avaliado,mensagem,nota,tipo)
        if result['sucesso'] is False:
            return result

        if tipo == 'cliente':
            f = Cliente.query.filter_by(id=id_avaliador).first()
            g = Profissional.query.filter_by(id=id_avaliado).first()
            try:
                f = f.pessoa.usuario
            except:
                return {'sucesso':False, 'mensagem':'cliente não possui usuário.'}
            try:
                g = g.pessoa.usuario
            except:
                return {'sucesso':False, 'mensagem':'profissional não possui usuário.'}
                
        elif tipo == 'profissional':
            f = Profissional.query.filter_by(id=id_avaliador).first()
            g = Cliente.query.filter_by(id=id_avaliado).first()
            try:
                f = f.pessoa.usuario
            except:
                return {'sucesso':False, 'mensagem':'profissional não possui usuário.'}
            try:
                g = g.pessoa.usuario
            except:
                return {'sucesso':False, 'mensagem':'cliente não possui usuário.'}
        else:
            return {'sucesso':False, 'mensagem':'tipo não válido.'}
        
        h = Avaliacao.query.filter(Avaliacao.id_avaliador == f.id, Avaliacao.id_avaliado == g.id, Avaliacao.tipo == tipo).first()
        if h != None:
            return {'sucesso':False, 'mensagem':'avaliação existente.'}
        
        h = Avaliacao(f.id, g.id, tipo, mensagem, nota)
        db.session.add(h)
        db.session.commit()

        return {'sucesso':True, 'mensagem':'avaliação cadastrada com sucesso.', 'id_avaliador':h.id_avaliador, 'id_avaliado':h.id_avaliado, 'mensagem':h.mensagem, 'nota':h.nota, 'tipo':h.tipo}

    def removerAvaliacao(self,id_avaliador,id_avaliado, tipo):
        d = Avaliacao.query.filter(Avaliacao.id_avaliador == id_avaliador, Avaliacao.id_avaliado == id_avaliado, Avaliacao.tipo == tipo).first()
        if d == None:
            return {'sucesso':False, 'mensagem':'avaliação não existe.'}

        db.session.delete(d)
        db.session.commit()
        return {'sucesso':True, 'mensagem':'avaliação removida com sucesso.'}

    def retornarAvaliacao(self,id_avaliador,id_avaliado, tipo):
        g = Avaliacao.query.filter(Avaliacao.id_avaliador == id_avaliador, Avaliacao.id_avaliado == id_avaliado, Avaliacao.tipo == tipo).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'Avaliação não existe.'}

        return {'sucesso':True,'mensagem':'avaliação retornada com sucesso.','id_avaliador':g.id_avaliador, 'id_avaliado':g.id_avaliado, 'mensagem':g.mensagem, 'nota':g.nota, 'tipo':g.tipo}

    def retornarTodasAvaliacoes(self, tipo):
        g = Avaliacao.query.filter(Avaliacao.tipo == tipo).all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há avaliações.'}

        lista = list()
        for i in range(len(g)):
            lista.append({'id_avaliador':g[i].id_avaliador, 'id_avaliado':g[i].id_avaliado, 'mensagem':g[i].mensagem, 'nota':g[i].nota, 'tipo':g[i].tipo})

        return {'sucesso':True,'mensagem':'todas as avaliações retornadas com sucesso.','avaliações':lista}

    def atualizarAvaliacao(self,id_avaliador,id_avaliado,mensagem,nota, tipo):
        result = self.validarIntegridade(id_avaliador,id_avaliado,mensagem,nota, tipo)
        if result['sucesso'] is False:
            return result
        u = Avaliacao.query.filter(Avaliacao.id_avaliador == id_avaliador, Avaliacao.id_avaliado == id_avaliado, Avaliacao.tipo == tipo).first()
        if u == None:
            return {'sucesso':False, 'mensagem':'avaliação não existe.'}
        
        f = Usuario.query.filter_by(id=id_avaliador).first()
        g = Usuario.query.filter_by(id=id_avaliado).first()

        if tipo == 'cliente':
            try:
                f = f.pessoa.cliente
            except:
                return {'sucesso':False, 'mensagem':'Usuário não possui cliente.'}
            try:
                g = g.pessoa.profissional
            except:
                return {'sucesso':False, 'mensagem':'Usuário não possui profissional.'}
                
        elif tipo == 'profissional':
            try:
                f = f.pessoa.profissional
            except:
                return {'sucesso':False, 'mensagem':'Usuário não possui profissional.'}
            try:
                g = g.pessoa.cliente
            except:
                return {'sucesso':False, 'mensagem':'Usuário não possui cliente.'}
        else:
            return {'sucesso':False, 'mensagem':'tipo não válido.'}

        u.mensagem = mensagem
        u.nota = nota
        db.session.commit()

        return {'sucesso':True,'mensagem':'avaliação atualizada com sucesso.','id_avaliador':h.id_avaliador, 'id_avaliado':h.id_avaliado, 'mensagem':h.mensagem, 'nota':h.nota, 'tipo':h.tipo}
    
    def validarIntegridade(self,id_avaliador,id_avaliado,mensagem,nota, tipo):
        if id_avaliador == None:
            return {'sucesso':False, 'mensagem':'id_avaliador em branco.'}
        elif id_avaliado == None:
            return {'sucesso':False, 'mensagem':'id_avaliado em branco.'}
        elif mensagem == None or mensagem.strip() == "":
            return {'sucesso':False, 'mensagem':'mensagem em branco.'}
        elif nota == None:
            return {'sucesso':False, 'mensagem':'nota em branco.'}
        elif tipo == None or tipo.strip() == "":
            return {'sucesso':False, 'mensagem':'tipo em branco.'}
        return {'sucesso':True}