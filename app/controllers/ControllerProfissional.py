from app.Facade import SQLAlchemy, BaseQuery, db, ModelProfissional, ModelPessoa, ModelUsuario, ModelHabilidade, ModelProfissionalHabilidade
#from flask_sqlalchemy import SQLAlchemy, BaseQuery
#from app import db

#from app.models.ModelProfissional import Profissional

Profissional = ModelProfissional.Profissional
Pessoa = ModelPessoa.Pessoa
Usuario = ModelUsuario.Usuario
Habilidade = ModelHabilidade.Habilidade
ProfissionalHabilidade = ModelProfissionalHabilidade.ProfissionalHabilidade

class ControllerProfissional():
    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades):
        try:
            h = Usuario(telefone, senha)
            db.session.add(h)
            db.session.commit()
            i = Pessoa(cpf,nome,h.id)
            db.session.add(i)
            db.session.commit()
            j = Profissional(i.id)
            db.session.add(j)
            db.session.commit()
            for hab in habilidades:
                tudo = Habilidade.query.all()
                sidekick = str()
                for m in tudo:
                    sidekick = m
                    if hab == m.habilidade:
                        break
                if hab != sidekick:
                    k = Habilidade(hab)
                    db.session.add(k)
                    db.session.commit()
                    l = ProfissionalHabilidade(j.id, k.id)
                    db.session.add(l)
                    db.session.commit()
            return True
        except:
            return False

    def removerProfissional(self,id):
        try:
            d = Profissional.query.get(id)
            e = Pessoa.query.get(d.id_pessoa)
            f = Usuario.query.get(e.id_usuario)
            db.session.delete(d)
            ProfissionalHabilidade.query.filter_by(id_profissional=id).delete()
            db.session.commit()
            return True
        except:
            return False

    def retornarProfissional(self,id):
        try:
            g = Profissional.query.get(id)
            h = Pessoa.query.get(str(g.id_pessoa))
            i = Usuario.query.get(h.id_usuario)
            prof = ProfissionalHabilidade.query.filter_by(id_profissional=id)
            lista = list()
            for w in prof:
                hab = Habilidade.query.get(w.id_habilidade)
                lista.append(hab.habilidade)
            return {'id':g.id,'cpf':h.cpf,'nome':h.nome,'telefone':i.telefone, 'senha':i.senha,'habilidades':lista}
        except:
            return False

    def retornarTodosProfissionais(self):
        #try:
        g = Profissional.query.all()
        lista = list()
        listhab = list()
        for i in range(len(g)):
            p = Pessoa.query.get(g[i].id_pessoa)
            u = Usuario.query.get(p.id_usuario)
            prof = ProfissionalHabilidade.query.filter_by(id_profissional=g[i].id)
            for w in prof:
                hab = Habilidade.query.get(w.id_habilidade)
                listhab.append(hab.habilidade)
            lista.append({'id':str(g[i].id),'cpf':p.cpf,'nome':p.nome,'telefone':u.telefone,'senha':u.senha,'habilidades':listhab})
        return lista
        #except:
         #   return False

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades):
        #try:
        u = Profissional.query.get(id)
        v = Pessoa.query.get(u.id_pessoa)
        x = Usuario.query.get(v.id_usuario)
        prof = ProfissionalHabilidade.query.filter_by(id_profissional=id)
        v.cpf = cpf
        v.nome = nome
        x.telefone = telefone
        x.senha = senha

        ProfissionalHabilidade.query.filter_by(id_profissional=id).delete()
        for hab in habilidades:
            tudo = Habilidade.query.all()
            for um in tudo:
                if hab == um.habilidade:
                    break
            if hab != um:
                k = Habilidade(hab)
                db.session.add(k)
                db.session.commit()
                l = ProfissionalHabilidade(id, k.id)
                db.session.add(l)
                db.session.commit()

        db.session.commit()
        return True
        #except:
        #    return False