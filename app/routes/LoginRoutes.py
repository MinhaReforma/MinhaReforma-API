from app.Facade import render_template, request, jsonify, app, Facade

facade = Facade()

@app.route("/login/", methods=['POST'])
@app.route("/login", methods=['POST'])
def loginUsuario():
    if (request.method == 'POST'):
        some_json = request.get_json()
        if 'telefone' not in some_json or 'senha' not in some_json or 'tipoPessoa' not in some_json:
            return jsonify({'sucesso':False,'mensagem':'Parâmetro(s) faltando no Json'}), 404

        g = facade.login(some_json['telefone'],some_json['senha'], some_json['tipoPessoa'])

        if g['sucesso'] == False:
            return jsonify(g), 404
        else:
            return jsonify(g), 200