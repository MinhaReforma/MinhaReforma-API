from flask import jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db

from app.models.ModelUsuario import Usuario
#----------------------------Usuario--------------------------------

def inserirUsuario(telefone,senha):
    i = Usuario(telefone,senha)
    db.session.add(i)   
    db.session.commit()
    return jsonify({'sucesso':True,'id':i.id,'telefone':i.telefone,'senha':i.senha}), 201

def removerUsuario(id):
    try:
        d = Usuario.query.get(id)
        db.session.delete(d)
        db.session.commit()
        return jsonify({'sucesso':True,'id':d.id,'telefone':d.telefone,'senha':d.senha}), 202
    except:
        return jsonify({'sucesso':False,'tipo':'usuário não encontrado'}),404

def retornarTodosUsuarios():
    g = Usuario.query.all()
    lista = list()
    for i in range(len(g)):
        lista.append({'id':str(g[i].id),'telefone':g[i].telefone,'senha':g[i].senha}), 200
    return jsonify(lista)

def retornarUsuario(id):
    try:
        g = Usuario.query.get(id)
        return jsonify({'sucesso':True,'id':g.id,'telefone':g.telefone,'senha':g.senha}), 200
    except:
        return jsonify({'sucesso':False,'tipo':'usuário não encontrado'}),404

def atualizarUsuario(id,telefone,senha):
    try:
        u = Usuario.query.get(id)
        u.telefone = telefone
        u.senha = senha
        db.session.commit()
        return jsonify({'sucesso':True,'id':u.id,'telefone':u.telefone,'senha':u.senha}), 200
    except:
        return jsonify({'sucesso':False,'tipo':'usuário não encontrado'}),404

#--------------------------------LOGIN USUARIO-----------------------------------------------
def login(telefone,senha):
    g = Usuario.query.filter(Usuario.telefone == telefone).first()

    if g.senha == senha:
        return jsonify({'sucesso':True, 'id':g.id ,'telefone':telefone, 'senha':senha})

    return jsonify({'sucesso':False, 'tipo':'telefone ou senha invalidos'}), 400
    