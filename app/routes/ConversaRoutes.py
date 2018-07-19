from app.Facade import render_template, request, jsonify, app, Facade, socketio, emit

facade = Facade()

@app.route("/conversas/<idr>/<idp>",methods=['GET'])
@app.route("/conversas", defaults={'idr':None, 'idp':None}, methods=['GET'])
def conversa(idr, idp):
    if (request.method == 'GET'):
        if idr == None:
            result = facade.retornarTodasConversas()
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
        else:
            result = facade.retornarConversa(idr, idp)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400

@app.route("/conversas/mensagem",methods=['POST'])
def mensagem():
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirMensagem(some_json['id_conversa'],some_json['perfil'],some_json['data'], some_json['mensagem'], some_json['preco'], some_json['nivelPreco'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400
    
    elif (request.method == 'PUT'):
        some_json = request.get_json()
        result = facade.atualizarMensagem(some_json['id_mensagem'],some_json['nivelPreco'])
        if result['sucesso']:
            return jsonify(result), 200
        return jsonify(result), 400

@socketio.on('inserirMensagem', namespace='/conversa')
def inserirMensagem(json):
    result = facade.inserirMensagem(json['id_conversa'],json['perfil'],json['data'], json['mensagem'], json['preco'], json['nivelPreco'])
    if result['sucesso']:
        emit('inserirMensagem', jsonify(result), namespace='/conversa')
    emit('inserirMensagem', jsonify(result), namespace='/conversa')