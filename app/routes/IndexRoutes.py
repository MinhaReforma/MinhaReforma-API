from app.Facade import render_template, request, app
#from flask import render_template, request
#from app import app


@app.route("/index/<user>")
@app.route("/<user>")
@app.route("/", defaults={'user': None})
def index(user):
    return render_template('index.html',
                           user=user)