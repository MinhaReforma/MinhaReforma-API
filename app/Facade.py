from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db,app
from app.models import ModelUsuario, ModelCliente, ModelPessoa, ModelProfissional, ModelReforma, ModelPagamento, ModelNegociacaoPreco, ModelHabilidade, ModelMensagem, ModelProfissionalHabilidade, ModelReformaProfissional, ModelConversa
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma, ControllerLogin, ControllerProfissional
#from app.routes import IndexRoutes, UsuarioRoutes, ClienteRoutes, ReformaRoutes, LoginRoutes

class Facade():

    def __init__(self):
        __self.usuario = ControllerUsuario.ControllerUsuario()
        __self.reforma = ControllerReforma.ControllerReforma()
        __self.cliente = ControllerCliente.ControllerCliente()
        __self.profissional = ControllerProfissional.ControllerProfissional()
        __self.login = ControllerLogin.ControllerLogin()
    
    def inserirCliente(self, cpf, nome, telefone, senha):
        return self.cliente.inserirCliente(cpf, nome, telefone, senha)

    def removerCliente(self,id):
        return self.cliente.removerCliente(id)

    def retornarCliente(self,id):
        return self.cliente.retornarCliente(id)

    def retornarTodosClientes(self):
        return self.cliente.retornarTodosClientes()

    def atualizarCliente(self, id, cpf, nome, telefone, senha):
        return self.cliente.atualizarCliente(id, cpf, nome, telefone, senha)
    
    def login(self, telefone, senha):
        return self.login.login(telefone, senha)
    
    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades):
        return self.profissional.inserirProfissional(cpf, nome, telefone, senha, habilidades)

    def removerProfissional(self,id):
        return self.profissional.removerProfissional(id)

    def retornarProfissional(self,id):
        return self.profissional.retornarProfissional(id)

    def retornarTodosProfissionais(self):
        return self.profissional.retornarTodosProfissionais()

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades):
        return self.profissional.atualizarProfissional( id, cpf, nome, telefone, senha, habilidades)

    def inserirReforma(self,id_cliente, datainicio, nome, descricao):
        return self.reforma.inserirReforma(id_cliente, datainicio, nome, descricao)

    def removerReforma(self,id):
        return self.reforma.removerReforma(id)

    def retornarReforma(self,id):
        return self.reforma.retornarReforma(id)

    def retornarTodasReformas(self):
        return self.reforma.retornarTodasReformas()
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao):#, id_status,id_profissional,preco) 
        return self.reforma.atualizarReforma(id, id_cliente, datainicio, nome, descricao)  
                
    def inserirReformaProfissional(self,id_reforma, id_profissional):
        return self.reforma.inserirReformaProfissional(id_reforma, id_profissional)
    
    def inserirUsuario(self,telefone,senha):
        return self.usuario.inserirUsuario(telefone, senha)

    def removerUsuario(self,id):
        return self.usuario.removerUsuario(id)

    def retornarTodosUsuarios(self):
        return self.usuario.retornarTodosUsuarios()

    def retornarUsuario(self,id):
        return self.usuario.retornarUsuario(id)

    def atualizarUsuario(self,id,telefone,senha):
        return self.usuario.atualizarUsuario(id, telefone, senha)