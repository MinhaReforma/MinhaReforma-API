from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/avaliacao/<int:idor>/<int:ido>/<int:idr>/<tipo>", methods=['GET'])
@app.route("/avaliacao/<tipo>", defaults={'idor':None, 'ido':None, 'idr':None}, methods=['GET'])
@app.route("/avaliacao", defaults={'idor':None, 'ido':None, 'idr':None, 'tipo':None}, methods=['POST','DELETE','PUT'])
def avaliacao(idor,ido,idr,tipo):
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirAvaliacao(some_json['id_avaliador'],some_json['id_avaliado'],some_json['id_reforma'],some_json['mensagem'],some_json['nota'], some_json['tipo'])
        if result['sucesso']:
            return jsonify(result), 201
        return jsonify(result), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        result = facade.removerAvaliacao(some_json['id_avaliador'], some_json['id_avaliado'],some_json['id_reforma'], some_json['tipo'])
        if result['sucesso']:
            return jsonify(result), 202
        return jsonify(result), 400

    elif (request.method == 'GET'):
        if idor == None or ido == None or idr == None:
            result = facade.retornarTodasAvaliacoes(tipo)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400
        else:
            result = facade.retornarAvaliacao(idor,ido,idr,tipo)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        result = facade.atualizarCliente(some_json['id_avaliador'], some_json['id_avaliado'],some_json['id_reforma'], some_json['mensagem'], some_json['nota'], some_json['tipo'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400

@app.route("/avaliacao/<tipo>/<int:id>",methods=['GET'])
def avaliacaoCliente(tipo,id):
    if (request.method == 'GET'):
        if tipo == "cliente":
            result = facade.retornarTodasAvaliacoesCliente(id)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400

        elif tipo == "profissional":
            result = facade.retornarTodasAvaliacoesProfissional(id)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400
        
        else:
            return jsonify({'sucesso':False,'mensagem':'tipo inválido.'}), 400
