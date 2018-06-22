from flask import render_template, request
from app import app

from app.controllers.ControllerCliente import *


@app.route("/clientes/<id>",methods=['GET'])
@app.route("/clientes/", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/clientes", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def cliente(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        return inserirCliente(some_json['cpf'],some_json['nome'],some_json['id_usuario'])

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        return removerCliente(some_json['id'])

    elif (request.method == 'GET'):
        if id == None:
            return retornarTodosClientes()
        else:
            return retornarCliente(id)
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        return atualizarCliente(some_json['id'], some_json['cpf'], some_json['nome'], some_json['id_usuario'])