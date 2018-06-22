from flask import render_template, request
from app import app

from app.controllers.ControllerUsuario import *


@app.route("/usuarios/<id>",methods=['GET'])
@app.route("/usuarios/", defaults={'id': None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/usuarios", defaults={'id': None}, methods=['POST','GET','DELETE','PUT'])
def usuario(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        return inserirUsuario(some_json['telefone'],some_json['senha'])

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        return removerUsuario(some_json['id'])

    elif (request.method == 'GET'):
        if id == None:
            return retornarTodosUsuarios()
        else:
            return retornarUsuario(id)
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        return atualizarUsuario(some_json['id'], some_json['telefone'], some_json['senha'])

#--------------------------------LOGIN USUARIO-----------------------------------------------

@app.route("/usuarios/login/", methods=['POST'])
@app.route("/usuarios/login", methods=['POST'])
def loginUsuario():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return login(some_json['telefone'],some_json['senha'])
        g = Usuario.query.filter(Usuario.telefone == some_json['telefone']).first()
        if g is None:
            return jsonify({'sucesso':False, 'tipo':'telefone ou senha não encontrado'}), 404
        elif g.senha == some_json['senha']:
            return jsonify({'sucesso':True, 'id':g.id ,'telefone':some_json['telefone'], 'senha':some_json['senha']})
        else:
            return jsonify({'sucesso':False, 'tipo':'telefone ou senha não encontrado'}), 404
