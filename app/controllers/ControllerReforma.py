from app.Facade import SQLAlchemy, BaseQuery, db, ModelReforma, ModelReformaProfissional

Reforma = ModelReforma.Reforma
ReformaProfissional = ModelReformaProfissional.ReformaProfissional

class ControllerReforma():

    def inserirReforma(self,id_cliente, datainicio, nome, descricao):
        i = Reforma(id_cliente,datainicio,nome,descricao)#,id_status,id_profissional,preco)
        db.session.add(i)   
        db.session.commit()
        return True

    def removerReforma(self,id):
        d = Reforma.query.get(id)
        db.session.delete(d)
        db.session.commit()

    def retornarReforma(self,id):
        g = Reforma.query.get(id)
        h = ReformaProfissional.query.get(id)
        lista = list()
        for w in h:
            prof = ReformaProfissional.query.get(w.id_reforma)
            lista.append(prof.id_profissional)            
        return {'id':g.id,'id_cliente':g.id_cliente,'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao, 'listaProfissionais':lista}

    def retornarTodasReformas(self):
        g = Reforma.query.all()
        lista = list()
        for i in range(len(g)):
            lista.append({'id':str(g[i].id),'id_cliente':g[i].id_cliente,'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao}),200#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco}), 200
        return lista
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao):#, id_status,id_profissional,preco)   
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
                
    def inserirReformaProfissional(self,id_reforma, id_profissional):
        i = ReformaProfissional(id_reforma,id_profissional)
        print(i)
        db.session.add(i)   
        db.session.commit()
        return True
