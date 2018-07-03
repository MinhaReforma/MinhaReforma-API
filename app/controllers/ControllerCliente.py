from app.Facade import SQLAlchemy, BaseQuery, db, ModelCliente, ModelPessoa, ModelUsuario
#from flask_sqlalchemy import SQLAlchemy, BaseQuery
#from app import db

#from app.models.ModelCliente import Cliente

Cliente = ModelCliente.Cliente
Pessoa = ModelPessoa.Pessoa
Usuario = ModelUsuario.Usuario

class ControllerCliente():
    def inserirCliente(self,cpf,nome,telefone,senha):
        h = Usuario(telefone, senha)
        db.session.add(h)
        db.session.commit()
        i = Pessoa(cpf,nome,h.id)
        db.session.add(i)
        db.session.commit()
        j = Cliente(i.id)
        db.session.add(j)   
        db.session.commit()
        return True

    def removerCliente(self,id):
        d = Cliente.query.get(id)
        e = Pessoa.query.get(d.id_pessoa)
        f = Usuario.query.get(e.id_usuario)
        db.session.delete(d)
        db.session.commit()
        return True

    def retornarCliente(self,id):
        g = Cliente.query.get(id)
        h = Pessoa.query.get(str(g.id_pessoa))
        i = Usuario.query.get(h.id_usuario)
        return {'id':g.id,'cpf':h.cpf,'nome':h.nome,'telefone':i.telefone, 'senha':i.senha}

    def retornarTodosClientes(self):
        g = Cliente.query.all()
        lista = list()
        for i in range(len(g)):
            p = Pessoa.query.get(g[i].id_pessoa)
            u = Usuario.query.get(p.id_usuario)
            lista.append({'id':str(g[i].id),'cpf':p.cpf,'nome':p.nome,'telefone':u.telefone,'senha':u.senha})
        return lista

    def atualizarCliente(self,id,cpf,nome,telefone,senha):
        u = Cliente.query.get(id)
        v = Pessoa.query.get(u.id_pessoa)
        x = Usuario.query.get(v.id_usuario)
        v.cpf = cpf
        v.nome = nome
        x.telefone = telefone
        x.senha = senha
        db.session.commit()
        return True