from app.Facade import render_template, request, app

@app.route("/index/<user>")
@app.route("/<user>")
@app.route("/", defaults={'user': None})
def index(user):
    return render_template('index.html',
                           user=user)