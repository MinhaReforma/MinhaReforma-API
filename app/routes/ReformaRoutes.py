from app.Facade import render_template, request, jsonify, app, Facade #ControllerReforma, Facade

facade = Facade()

@app.route("/reformas/<id>",methods=['GET'])
@app.route("/reformas/", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
@app.route("/reformas", defaults={'id':None}, methods=['POST','GET','DELETE','PUT'])
def reforma(id):
    if (request.method == 'POST'):
        some_json = request.get_json()
        if facade.inserirReforma(some_json['id_cliente'],some_json['datainicio'],some_json['nome'],some_json['descricao']):#, some_json['id_status'],some_json['id_profissional'],some_json['preco'])
            return jsonify({'sucesso':True}), 201
        return jsonify({'sucesso':False}), 400

    elif (request.method == 'DELETE'):
        some_json = request.get_json()
        if facade.removerReforma(some_json['id']):
            return jsonify({'sucesso':True}), 202
        return jsonify({'sucesso':False}), 400
        
    elif (request.method == 'GET'):
        if id == None:
            result = facade.retornarTodasReformas()
            if result:
                return jsonify({'sucesso':True,'reformas':result}), 200
            return jsonify({'sucesso':False}),400
        else:
            result = facade.retornarReforma(id)
            if result:
                return jsonify({'sucesso':True,'id':result['id'],'id_cliente':result['id_cliente'],'datainicio':result['datainicio'],'nome':result['nome'],'descricao':result['descricao']}),200#,'id_status':result['id_status'],'id_profissional':result['id_profissional'],'preco':result['preco']}), 200
            return jsonify({'sucesso':False}), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        if facade.atualizarReforma(some_json['id'],some_json['id_cliente'],some_json['datainicio'],some_json['nome'],some_json['descricao']):#, some_json['id_status'],some_json['id_profissional'],some_json['preco'])
            return jsonify({'sucesso':True}), 201
        return jsonify({'sucesso':False}), 400

@app.route("/reformas/profissionais", methods=['POST'])
def profissionais():
    if (request.method == 'POST'):
        some_json = request.get_json()
        if facade.inserirReformaProfissional(some_json['id_reforma'],some_json['id_profissional']):
            return jsonify({'sucesso':True}), 201
        return jsonify({'sucesso':False}), 400
