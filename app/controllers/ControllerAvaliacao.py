from app.Facade import SQLAlchemy, BaseQuery, db, ModelAvaliacao, ModelUsuario, ModelCliente, ModelProfissional, ModelReforma

Avaliacao = ModelAvaliacao.Avaliacao
Cliente = ModelCliente.Cliente
Profissional = ModelProfissional.Profissional
Reforma = ModelReforma.Reforma
Usuario = ModelUsuario.Usuario

class ControllerAvaliacao():
    def inserirAvaliacao(self,id_avaliador,id_avaliado,id_reforma,mensagem,nota, tipo):

        result = self.validarIntegridade(id_avaliador,id_avaliado,id_reforma,mensagem,nota,tipo)
        if result['sucesso'] is False:
            return result
        
        e = Reforma.query.filter_by(id=id_reforma).first()
        if e == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}

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
        
        h = Avaliacao.query.filter(Avaliacao.id_avaliador == f.id, Avaliacao.id_avaliado == g.id, Avaliacao.id_reforma == e.id ,Avaliacao.tipo == tipo).first()
        if h != None:
            return {'sucesso':False, 'mensagem':'avaliação existente.'}
        
        h = Avaliacao(f.id, g.id, e.id, tipo, mensagem, nota)
        db.session.add(h)
        db.session.commit()

        return {'sucesso':True, 'mensagem':'avaliação cadastrada com sucesso.', 'id_avaliador':h.id_avaliador, 'id_avaliado':h.id_avaliado,'id_reforma':h.id_reforma ,'mensagem':h.mensagem, 'nota':h.nota, 'tipo':h.tipo}

    def removerAvaliacao(self,id_avaliador,id_avaliado, id_reforma, tipo):

        result = self.validarIntegridade(id_avaliador,id_avaliado,id_reforma,mensagem,nota,tipo)
        if result['sucesso'] is False:
            return result
        
        e = Reforma.query.filter_by(id=id_reforma).first()
        if e == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}

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

        d = Avaliacao.query.filter(Avaliacao.id_avaliador == f.id, Avaliacao.id_avaliado == g.id, Avaliacao.id_reforma == e.id ,Avaliacao.tipo == tipo).first()
        if d == None:
            return {'sucesso':False, 'mensagem':'avaliação não existe.'}

        db.session.delete(d)
        db.session.commit()
        return {'sucesso':True, 'mensagem':'avaliação removida com sucesso.'}

    def retornarAvaliacao(self,id_avaliador,id_avaliado, id_reforma,tipo):

        result = self.validarIntegridade(id_avaliador,id_avaliado,id_reforma,mensagem,nota,tipo)
        if result['sucesso'] is False:
            return result
        
        e = Reforma.query.filter_by(id=id_reforma).first()
        if e == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}

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
            
        g = Avaliacao.query.filter(Avaliacao.id_avaliador == f.id, Avaliacao.id_avaliado == g.id, Avaliacao.id_reforma == e.id ,Avaliacao.tipo == tipo).first()
        if g == None:
            return {'sucesso':False, 'mensagem':'Avaliação não existe.'}

        return {'sucesso':True,'mensagem':'avaliação retornada com sucesso.','id_avaliador':g.id_avaliador, 'id_avaliado':g.id_avaliado, 'id_reforma':g.id_reforma, 'mensagem':g.mensagem, 'nota':g.nota, 'tipo':g.tipo}

    def retornarTodasAvaliacoes(self, tipo):
        g = Avaliacao.query.filter(Avaliacao.tipo == tipo).all()
        if g == None:
            return {'sucesso':False, 'mensagem':'não há avaliações.'}

        lista = list()
        for i in range(len(g)):
            lista.append({'id_avaliador':g[i].id_avaliador, 'id_avaliado':g[i].id_avaliado, 'id_reforma':g[i].id_reforma, 'mensagem':g[i].mensagem, 'nota':g[i].nota, 'tipo':g[i].tipo})

        return {'sucesso':True,'mensagem':'todas as avaliações retornadas com sucesso.','avaliações':lista}

    def atualizarAvaliacao(self,id_avaliador,id_avaliado,id_reforma,mensagem,nota, tipo):
        result = self.validarIntegridade(id_avaliador,id_avaliado,id_reforma,mensagem,nota, tipo)
        if result['sucesso'] is False:
            return result
        
        e = Reforma.query.filter_by(id=id_reforma).first()
        if e == None:
            return {'sucesso':False, 'mensagem':'reforma não existe.'}
        
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

        u = Avaliacao.query.filter(Avaliacao.id_avaliador == f.id, Avaliacao.id_avaliado == g.id, Avaliacao.id_reforma == e.id ,Avaliacao.tipo == tipo).first()
        if u == None:
            return {'sucesso':False, 'mensagem':'avaliação não existe.'}

        u.mensagem = mensagem
        u.nota = nota
        db.session.commit()

        return {'sucesso':True,'mensagem':'avaliação atualizada com sucesso.','id_avaliador':h.id_avaliador, 'id_avaliado':h.id_avaliado, 'id_reforma':h.id_reforma,'mensagem':h.mensagem, 'nota':h.nota, 'tipo':h.tipo}
    
    def validarIntegridade(self,id_avaliador,id_avaliado,id_reforma,mensagem,nota, tipo):
        if id_avaliador == None:
            return {'sucesso':False, 'mensagem':'id_avaliador em branco.'}
        elif id_avaliado == None:
            return {'sucesso':False, 'mensagem':'id_avaliado em branco.'}
        elif id_reforma == None:
            return {'sucesso':False, 'mensagem':'id_reforma em branco.'}
        elif mensagem == None or mensagem.strip() == "":
            return {'sucesso':False, 'mensagem':'mensagem em branco.'}
        elif nota == None:
            return {'sucesso':False, 'mensagem':'nota em branco.'}
        elif tipo == None or tipo.strip() == "":
            return {'sucesso':False, 'mensagem':'tipo em branco.'}
        return {'sucesso':True}
    
    ###########################################################################################################################################

    def retornarTodasAvaliacoesCliente(self, id):
        f = Cliente.query.filter_by(id=id).first()
        if f == None:
            return {'sucesso':False, 'mensagem':'cliente não existe.'}
        g = Avaliacao.query.filter(Avaliacao.id_avaliado == f.pessoa.usuario.id, Avaliacao.tipo == "profissional").all()
        if g == []:
            return {'sucesso':False, 'mensagem':'não há avaliações.'}
        
        j = Usuario.query.filter_by(id=id_avaliador).first()

        lista = list()
        for i in g:
            h = Profissional.query.filter_by(id=j.pessoa.profissional.id).first()
            lista.append({'id_avaliador':i.id_avaliador, 'id_avaliado':i.id_avaliado, 'id_reforma':i.id_reforma, 'profissional':{'id':h.id,'cpf':h.pessoa.cpf,'nome':h.pessoa.nome,'telefone':h.pessoa.usuario.telefone} , 'mensagem':i.mensagem, 'nota':i.nota, 'tipo':i.tipo})
        
        return {'sucesso':True, 'mensagem':'todas as avaliações retornadas com sucesso.', 'avaliacoes':lista}
    
    def retornarTodasAvaliacoesProfissional(self, id):
        f = Profissional.query.filter_by(id=id).first()
        if f == None:
            return {'sucesso':False, 'mensagem':'profissional não existe'}
        g = Avaliacao.query.filter(Avaliacao.id_avaliado == f.pessoa.usuario.id, Avaliacao.tipo == "cliente").all()
        if g == []:
            return {'sucesso':False, 'mensagem':'não há avaliações.'}
        
        j = Usuario.query.filter_by(id=id_avaliador).first()

        lista = list()
        for i in g:
            h = Cliente.query.filter_by(id=j.pessoa.cliente.id).first()
            lista.append({'id_avaliador':i.id_avaliador, 'id_avaliado':i.id_avaliado, 'id_reforma':i.id_reforma, 'cliente':{'id':h.id,'cpf':h.pessoa.cpf,'nome':h.pessoa.nome,'telefone':h.pessoa.usuario.telefone},'mensagem':i.mensagem, 'nota':i.nota, 'tipo':i.tipo})
        
        return {'sucesso':True, 'mensagem':'todas as avaliações retornadas com sucesso.', 'avaliacoes':lista}
