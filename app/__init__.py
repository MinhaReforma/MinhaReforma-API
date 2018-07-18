from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
socketio = SocketIO(app)
    
@manager.command
def run():
    socketio.run(app)

from app.models import ModelUsuario, ModelCliente, ModelReforma, ModelPessoa, ModelProfissional, ModelPagamento, ModelNegociacaoPreco, ModelHabilidade, ModelMensagem, ModelConversa, ModelReformaProfissional#, ModelProfissionalHabilidade
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma, ControllerLogin, ControllerProfissional, ControllerConversa
from app.routes import IndexRoutes, UsuarioRoutes, ClienteRoutes, ReformaRoutes, LoginRoutes, ProfissionalRoutes, ConversaRoutes
#from app import Facade