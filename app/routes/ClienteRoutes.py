from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/clientes/<id>",methods=['GET'])
@app.route("/clientes/", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/clientes", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def cliente(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirProfissional(some_json['cpf'],some_json['nome'],some_json['telefone'],some_json['senha'])
        if result['sucesso']:
            return jsonify(result), 201
        return jsonify(result), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        result = facade.removerCliente(some_json['id'])
        if result['sucesso']:
            return jsonify(result), 202
        return jsonify(result), 400

    elif (request.method == 'GET'):
        if id == None:
            result = facade.retornarTodosClientes()
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
        else:
            result = facade.retornarCliente(id)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        result = facade.atualizarProfissional(some_json['id'], some_json['cpf'], some_json['nome'], some_json['telefone'], some_json['senha'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400