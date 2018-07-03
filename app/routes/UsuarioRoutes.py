from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/usuarios/<id>",methods=['GET'])
@app.route("/usuarios/", defaults={'id': None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/usuarios", defaults={'id': None}, methods=['POST','GET','DELETE','PUT'])
def usuario(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        if facade.inserirUsuario(some_json['telefone'],some_json['senha']):
            return jsonify({'sucesso':True}), 201
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        if facade.removerUsuario(some_json['id']):
            return jsonify({'sucesso':True}), 202
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'GET'):
        if id == None:
            result = facade.retornarTodosUsuarios()
            if result:
                return jsonify({'sucesso':True,'usuarios':result}),200
            return jsonify({'sucesso':False})
        else:
            result = facade.retornarUsuario(id)
            if result:
                return jsonify({'sucesso':True, 'id':result['id'],'telefone':result['telefone'],'senha':result['senha'] })
            return jsonify({'sucesso':False})
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        if facade.atualizarUsuario(some_json['id'], some_json['telefone'], some_json['senha']):
            return jsonify({'sucesso':True}), 200
        return jsonify({'sucesso':False}), 400
