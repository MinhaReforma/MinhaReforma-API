from app.Facade import SQLAlchemy, BaseQuery, db, ModelProfissional, ModelPessoa, ModelUsuario
#from flask_sqlalchemy import SQLAlchemy, BaseQuery
#from app import db

#from app.models.ModelProfissional import Profissional

Profissional = ModelProfissional.Profissional
Pessoa = ModelPessoa.Pessoa
Usuario = ModelUsuario.Usuario

class ControllerProfissional():
    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades):
        try:
            h = Usuario(telefone, senha)
            db.session.add(h)
            db.session.commit()
            i = Pessoa(cpf,nome,h.id)
            db.session.add(i)
            db.session.commit()
            j = Profissional(i.id, habilidades)
            db.session.add(j)   
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
            db.session.commit()
            return True
        except:
            return False

    def retornarProfissional(self,id):
        try:
            g = Profissional.query.get(id)
            h = Pessoa.query.get(str(g.id_pessoa))
            i = Usuario.query.get(h.id_usuario)
            return {'id':g.id,'cpf':h.cpf,'nome':h.nome,'telefone':i.telefone, 'senha':i.senha,'habilidades':g.listaHabilidades}
        except:
            return False

    def retornarTodosProfissionais(self):
        try:
            g = Profissional.query.all()
            lista = list()
            for i in range(len(g)):
                p = Pessoa.query.get(g[i].id_pessoa)
                u = Usuario.query.get(p.id_usuario)
                lista.append({'id':str(g[i].id),'cpf':p.cpf,'nome':p.nome,'telefone':u.telefone,'senha':u.senha,'habilidades':g[i].listaHabilidades})
            return lista
        except:
            return False

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades):
        try:
            u = Profissional.query.get(id)
            v = Pessoa.query.get(u.id_pessoa)
            x = Usuario.query.get(v.id_usuario)
            v.cpf = cpf
            v.nome = nome
            x.telefone = telefone
            x.senha = senha
            u.listaHabilidades = habilidades
            db.session.commit()
            return True
        except:
            return False