from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/login/", methods=['POST'])
@app.route("/login", methods=['POST'])
def loginUsuario():
    if (request.method == 'POST'):
        some_json = request.get_json()
        g = facade.login(some_json['telefone'],some_json['senha'])
        if g is False:
            return jsonify({'sucesso':False, 'tipo':'telefone ou senha não encontrado'}), 404
        else:
            return jsonify({'sucesso':True, 'id':g['id'] ,'telefone':g['telefone'], 'senha':g['senha']}), 200