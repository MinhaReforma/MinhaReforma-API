from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/profissionais/<id>",methods=['GET'])
@app.route("/profissionais", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def profissional(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirProfissional(some_json['cpf'],some_json['nome'],some_json['telefone'],some_json['senha'],some_json['habilidades'], some_json['profissao'])
        if result['sucesso']:
            return jsonify(result), 201
        return jsonify(result), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        result = facade.removerProfissional(some_json['id'])
        if result['sucesso']:
            return jsonify(result), 202
        return jsonify(result), 400

    elif (request.method == 'GET'):
        if id == None:
            result = facade.retornarTodosProfissionais()
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
        else:
            result = facade.retornarProfissional(id)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        result = facade.atualizarProfissional(some_json['id'], some_json['cpf'], some_json['nome'], some_json['telefone'], some_json['senha'], some_json['habilidades'], some_json['profissao'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400