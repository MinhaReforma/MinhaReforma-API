from app.Facade import render_template, request, jsonify, app, Facade #ControllerReforma, Facade

facade = Facade()

@app.route("/reformas/<int:id>",methods=['GET'])
@app.route("/reformas", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def reforma(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirReforma(some_json['id_cliente'],some_json['datainicio'],some_json['nome'],some_json['descricao'],some_json['status'])
        if result['sucesso']:
            return jsonify(result), 201
        return jsonify(result), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        result = facade.removerReforma(some_json['id'])
        if result['sucesso']:
            return jsonify(result), 202
        return jsonify(result), 400
        
    elif (request.method == 'GET'):
        if id == None:
            result = facade.retornarTodasNovasReformas()
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
        else:
            result = facade.retornarReforma(id)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        print(some_json)
        result = facade.atualizarReforma(some_json['id'],some_json['id_cliente'], some_json['datainicio'], some_json['nome'], some_json['descricao'],some_json['status'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400
    

@app.route("/reformas/profissional/<id>", methods=['GET'])
@app.route("/reformas/profissional", defaults={'id':None}, methods=['POST'])
def reformaProfissional(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirReformaProfissional(some_json['id_reforma'],some_json['id_profissional'])
        if result['sucesso']:
            return jsonify(result), 201
        return jsonify(result), 400

    elif (request.method == 'GET'):
        result = facade.retornarTodasReformasProfissional(id)
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400

@app.route("/reformas/cliente/<id>", methods=['GET'])
def reformaCliente(id):
    if (request.method == 'GET'):
        result = facade.retornarTodasReformasCliente(id)
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400

@app.route("/reformas/status", methods=['POST'])
def status():
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.novoStatus(some_json['reforma'],some_json['status'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400
