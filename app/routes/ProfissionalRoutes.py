from app.Facade import render_template, request, jsonify, app, Facade
#from flask import render_template, request, jsonify
#from app import app

#from app.controllers.ControllerProfissional import *

facade = Facade()
controller = facade.ControllerProfissional()

@app.route("/profissionais/<id>",methods=['GET'])
@app.route("/profissionais/", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/profissionais", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def profissional(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        if controller.inserirProfissional(some_json['cpf'],some_json['nome'],some_json['telefone'],some_json['senha'],some_json['habilidades']):
            return jsonify({'sucesso':True}), 201
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        if controller.removerProfissional(some_json['id']):
            return jsonify({'sucesso':True}), 202
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'GET'):
        if id == None:
            result = controller.retornarTodosProfissionais()
            if result:
                return jsonify({'sucesso':True,'profissionais':result}), 200
            else:
                return jsonify({'sucesso':False}),400
        else:
            result = controller.retornarProfissional(id)
            if result:
                return jsonify({'sucesso':True,'id':result['id'],'cpf':result['cpf'],'nome':result['nome'],'telefone':result['telefone'],'senha':result['senha'],'habilidades':result['habilidades']}), 200
            return jsonify({'sucesso':result}), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        if controller.atualizarProfissional(some_json['id'], some_json['cpf'], some_json['nome'], some_json['telefone'], some_json['senha'], some_json['habilidades']):
            return jsonify({'sucesso':True}), 200
        return jsonify({'sucesso':False}), 400