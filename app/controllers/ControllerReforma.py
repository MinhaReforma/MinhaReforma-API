from flask import jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db

from app.models.ModelReforma import Reforma

def inserirReforma(id_cliente, datainicio, nome, descricao):
    i = Reforma(id_cliente,datainicio,nome,descricao)#,id_status,id_profissional,preco)
    db.session.add(i)   
    db.session.commit()
    return jsonify({'sucesso':True,'id':i.id,'id_cliente':i.id_cliente,'datainicio':i.datainicio,'nome':i.nome,'descricao':i.descricao}) , 201#,'id_status':i.id_status,'id_profissional':i.id_profissional,'preco':i.preco}), 201

def removerReforma(id):
    try:
        d = Reforma.query.get(id)
        db.session.delete(d)
        db.session.commit()
        return jsonify({'sucesso':True,'id':d.id,'id_cliente':d.id_cliente,'datainicio':d.datainicio,'nome':d.nome,'descricao':d.descricao}),202#,'id_status':d.id_status,'id_profissional':d.id_profissional,'preco':d.preco}), 202
    except:
        return jsonify({'sucesso':True,'tipo':'reforma não encontrada'}),404

def retornarReforma(id):
    try:
        g = Reforma.query.get(id)
        return jsonify({'sucesso':True,'id':g.id,'id_cliente':g.id_cliente,'datainicio':g.datainicio,'nome':g.nome,'descricao':g.descricao}),200#,'id_status':g.id_status,'id_profissional':g.id_profissional,'preco':g.preco}), 200
    except:
        return jsonify({'sucesso':False,'tipo':'reforma não encontrada'}),404

def retornarTodasReformas():
    g = Reforma.query.all()
    lista = list()
    for i in range(len(g)):
        lista.append({'id':str(g[i].id),'id_cliente':g[i].id_cliente,'datainicio':g[i].datainicio,'nome':g[i].nome,'descricao':g[i].descricao}),200#,'id_status':g[i].id_status,'id_profissional':g[i].id_profissional,'preco':g[i].preco}), 200
    return jsonify(lista)
            
def atualizarReforma(id,id_cliente,datainicio,nome,descricao):#, id_status,id_profissional,preco)   
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
        return jsonify({'sucesso':True,'id':u.id,'id_cliente':u.id_cliente,'datainicio':u.datainicio,'nome':u.nome,'descricao':u.descricao}),200#,'id_status':u.id_status,'id_profissional':u.id_profissional,'preco':u.preco}), 200
    except:
        return jsonify({'sucesso':False, 'tipo':'reforma não encontrada'}),404    
