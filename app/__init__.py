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

from app.models import ModelUsuario, ModelCliente, ModelReforma
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma
from app.routes import IndexRoutes, UsuarioRoutes, ClienteRoutes, ReformaRoutes