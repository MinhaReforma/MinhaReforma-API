from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/usuarios/<id>",methods=['GET'])
@app.route("/usuarios", defaults={'id': None}, methods=['POST','GET','DELETE','PUT'])
def usuario(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirUsuario(some_json['telefone'],some_json['senha'])
        if result['sucesso']:
            return jsonify(result), 201
        return jsonify(result), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        result = facade.removerUsuario(some_json['id'])
        if result['sucesso']:
            return jsonify(result), 202
        return jsonify(result), 400

    elif (request.method == 'GET'):
        if id == None:
            result = facade.retornarTodosUsuarios()
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
        else:
            result = facade.retornarUsuario(id)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        result = facade.atualizarUsuario(some_json['id'], some_json['telefone'], some_json['senha'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400
