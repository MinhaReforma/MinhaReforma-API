from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db,app
from app.models import ModelUsuario, ModelCliente, ModelPessoa, ModelProfissional, ModelReforma, ModelPagamento, ModelNegociacaoPreco
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma, ControllerLogin, ControllerProfissional
#from app.routes import IndexRoutes, UsuarioRoutes, ClienteRoutes, ReformaRoutes, LoginRoutes

class Facade():

    def ControllerUsuario(self):
        return ControllerUsuario.ControllerUsuario()
    
    def ControllerReforma(self):
        return ControllerReforma.ControllerReforma()
    
    def ControllerCliente(self):
        return ControllerCliente.ControllerCliente()
    
    def ControllerProfissional(self):
        return ControllerProfissional.ControllerProfissional()