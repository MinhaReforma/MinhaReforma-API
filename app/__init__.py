from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
    

from app.models import ModelUsuario, ModelCliente, ModelReforma, ModelPessoa, ModelProfissional, ModelPagamento, ModelNegociacaoPreco, ModelHabilidade, ModelMensagem, ModelConversa, ModelReformaProfissional, ModelAvaliacao#, ModelProfissionalHabilidade
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma, ControllerLogin, ControllerProfissional, ControllerConversa, ControllerAvaliacao
from app.routes import IndexRoutes, UsuarioRoutes, ClienteRoutes, ReformaRoutes, LoginRoutes, ProfissionalRoutes, ConversaRoutes, AvaliacaoRoutes
#from app import Facade