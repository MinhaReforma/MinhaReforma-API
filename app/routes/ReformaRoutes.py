from flask import render_template, request
from app import app

from app.controllers.ControllerReforma import *


@app.route("/reformas/<id>",methods=['GET'])
@app.route("/reformas/", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/reformas", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def reforma(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        return inserirReforma(some_json['id_cliente'],some_json['datainicio'],some_json['nome'],some_json['descricao'])#, some_json['id_status'],some_json['id_profissional'],some_json['preco'])

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        return removerReforma(some_json['id'])
        
    elif (request.method == 'GET'):
        if id == None:
            return retornarTodasReformas()
        else:
            return retornarReforma(id)
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        return atualizarReforma(some_json['id'],some_json['id_cliente'],some_json['datainicio'],some_json['nome'],some_json['descricao'])#, some_json['id_status'],some_json['id_profissional'],some_json['preco'])
