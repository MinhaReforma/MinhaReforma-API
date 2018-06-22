from flask import jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db

from app.models.ModelCliente import Cliente

def inserirCliente(cpf,nome,id_usuario):
    try:
        i = Cliente(cpf,nome,id_usuario)
        db.session.add(i)   
        db.session.commit()
        return jsonify({'sucesso':True,'id':i.id,'cpf':i.cpf,'nome':i.nome,'id_usuario':i.id_usuario}), 201
    except:
        return jsonify({'sucesso':False,'tipo':'Cliente não encontrado'}),404

def removerCliente(id):
    try:
        d = Cliente.query.get(id)
        db.session.delete(d)
        db.session.commit()
        return jsonify({'sucesso':True,'id':d.id,'cpf':d.cpf,'nome':d.nome,'id_usuario':d.id_usuario}), 202
    except:
        return jsonify({'sucesso':False,'tipo':'Cliente não encontrado'}),404

def retornarCliente(id):
    try:
        g = Cliente.query.get(id)
        return jsonify({'sucesso':True,'id':g.id,'cpf':g.cpf,'nome':g.nome,'id_usuario':g.id_usuario}), 200
    except:
        return jsonify({'sucesso':False,'tipo':'Cliente não encontrado'}),404

def retornarTodosClientes():
    g = Cliente.query.all()
    lista = list()
    for i in range(len(g)):
        lista.append({'id':str(g[i].id),'cpf':g[i].cpf,'nome':g[i].nome,'id_usuario':g[i].id_usuario}), 200
    return jsonify(lista)

def atualizarCliente(id,cpf,nome,id_usuario):
    try:
        u = Cliente.query.get(id)
        u.cpf = cpf
        u.nome = nome
        u.id_usuario = id_usuario
        db.session.commit()
        return jsonify({'sucesso':True,'id':u.id,'cpf':u.cpf,'nome':u.nome,'id_usuario':u.id_usuario}), 200
    except:
        return jsonify({'sucesso':False,'tipo':'Cliente não encontrado'}),404