from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/conversa/<idr>/<idp>",methods=['GET'])
def conversa(idr, idp):
    
    if (request.method == 'GET'):
        if idr == None:
            result = facade.retornarTodosConversa()
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result),400
        else:
            result = facade.retornarConversa(idr)
            if result['sucesso']:
                return jsonify(result), 200
            return jsonify(result), 400

@app.route("/conversa/mensagem",methods=['POST'])
def mensagem():
    if (request.method == 'POST'):
        some_json = request.get_json()
        result = facade.inserirMensagem(some_json['id_conversa'],some_json['perfil'],some_json['data'], some_json['mensagem'])