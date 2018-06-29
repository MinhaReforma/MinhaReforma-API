from app.Facade import SQLAlchemy, BaseQuery, db, ModelReforma
#from flask_sqlalchemy import SQLAlchemy, BaseQuery
#from app import db

#from app.models.ModelReforma import Reforma

Reforma = ModelReforma.Reforma

class ControllerReforma():

    def inserirReforma(self,id_cliente, datainicio, nome, descricao):
        try:
            i = Reforma(id_cliente,datainicio,nome,descricao)#,id_status,id_profissional,preco)
            db.session.add(i)   
            db.session.commit()
            return True
        except:
            return False

    def removerReforma(self,id):
        try:
            d = Reforma.query.get(id)
            db.session.delete(d)
            db.session.commit()
            return True
        except:
            return False

    def retornarReforma(self,id):
        try:
            g = Reforma.query.get(id)
            return {'id':g.id,'id_cliente':g.id_cliente,'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao}#,'id_status':g.id_status,'id_profissional':g.id_profissional,'preco':g.preco}
        except:
            return False
    def retornarTodasReformas(self):
        #try:
        g = Reforma.query.all()
        lista = list()
        for i in range(len(g)):
            lista.append({'id':str(g[i].id),'id_cliente':g[i].id_cliente,'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao}),200#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco}), 200
        return lista
        #except:
            #return False
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao):#, id_status,id_profissional,preco)   
        try:
            u = Reforma.query.get(id)
            u.id_cliente = id_cliente
            u.datainicio = datainicio
            u.nome = nome
            u.descricao = descricao
            #u.id_status = id_status
            #u.id_profissional = id_profissional
            #u.preco = preco
            db.session.commit()
            return True
        except:
            return False    
