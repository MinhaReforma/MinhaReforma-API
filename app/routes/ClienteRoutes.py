from app.Facade import render_template, request, jsonify, app, Facade
#from flask import render_template, request, jsonify
#from app import app

#from app.controllers.ControllerCliente import *

facade = Facade()
controller = facade.ControllerCliente()

@app.route("/clientes/<id>",methods=['GET'])
@app.route("/clientes/", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/clientes", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def cliente(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        if controller.inserirCliente(some_json['cpf'],some_json['nome'],some_json['telefone'],some_json['senha']):
            return jsonify({'sucesso':True}), 201
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        if controller.removerCliente(some_json['id']):
            return jsonify({'sucesso':True}), 202
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'GET'):
        if id == None:
            result = controller.retornarTodosClientes()
            if result:
                return jsonify({'sucesso':True,'clientes':result}), 200
            else:
                return jsonify({'sucesso':False}),400
        else:
            result = controller.retornarCliente(id)
            if result:
                return jsonify({'sucesso':True,'id':result['id'],'cpf':result['cpf'],'nome':result['nome'],'telefone':result['telefone'],'senha':result['senha']}), 200
            return jsonify({'sucesso':result}), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        if controller.atualizarCliente(some_json['id'], some_json['cpf'], some_json['nome'], some_json['telefone'], some_json['senha']):
            return jsonify({'sucesso':True}), 200
        return jsonify({'sucesso':False}), 400