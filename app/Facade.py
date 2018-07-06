from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db,app
from app.models import ModelUsuario, ModelCliente, ModelPessoa, ModelProfissional, ModelReforma, ModelPagamento, ModelNegociacaoPreco, ModelHabilidade, ModelMensagem, ModelProfissionalHabilidade, ModelReformaProfissional, ModelConversa
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma, ControllerLogin, ControllerProfissional
#from app.routes import IndexRoutes, UsuarioRoutes, ClienteRoutes, ReformaRoutes, LoginRoutes

class Facade():

    def __init__(self):
        self.__usuario = ControllerUsuario.ControllerUsuario()
        self.__reforma = ControllerReforma.ControllerReforma()
        self.__cliente = ControllerCliente.ControllerCliente()
        self.__profissional = ControllerProfissional.ControllerProfissional()
        self.__login = ControllerLogin.ControllerLogin()
    
    def inserirCliente(self, cpf, nome, telefone, senha):
        return self.__cliente.inserirCliente(cpf, nome, telefone, senha)

    def removerCliente(self,id):
        return self.__cliente.removerCliente(id)

    def retornarCliente(self,id):
        return self.__cliente.retornarCliente(id)

    def retornarTodosClientes(self):
        return self.__cliente.retornarTodosClientes()

    def atualizarCliente(self, id, cpf, nome, telefone, senha):
        return self.__cliente.atualizarCliente(id, cpf, nome, telefone, senha)
    
    def login(self, telefone, senha, tipoPessoa):
        return self.__login.login(telefone, senha, tipoPessoa)
    
    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades):
        return self.__profissional.inserirProfissional(cpf, nome, telefone, senha, habilidades)

    def removerProfissional(self,id):
        return self.__profissional.removerProfissional(id)

    def retornarProfissional(self,id):
        return self.__profissional.retornarProfissional(id)

    def retornarTodosProfissionais(self):
        return self.__profissional.retornarTodosProfissionais()

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades):
        return self.__profissional.atualizarProfissional( id, cpf, nome, telefone, senha, habilidades)

    def inserirReforma(self,id_cliente, datainicio, nome, descricao):
        return self.__reforma.inserirReforma(id_cliente, datainicio, nome, descricao)

    def removerReforma(self,id):
        return self.__reforma.removerReforma(id)

    def retornarReforma(self,id):
        return self.__reforma.retornarReforma(id)

    def retornarTodasReformas(self):
        return self.__reforma.retornarTodasReformas()
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao):#, id_status,id_profissional,preco) 
        return self.__reforma.atualizarReforma(id, id_cliente, datainicio, nome, descricao)  
                
    def inserirReformaProfissional(self,id_reforma, id_profissional):
        return self.__reforma.inserirReformaProfissional(id_reforma, id_profissional)
    
    def inserirUsuario(self,telefone,senha):
        return self.__usuario.inserirUsuario(telefone, senha)

    def removerUsuario(self,id):
        return self.__usuario.removerUsuario(id)

    def retornarTodosUsuarios(self):
        return self.__usuario.retornarTodosUsuarios()

    def retornarUsuario(self,id):
        return self.__usuario.retornarUsuario(id)

    def atualizarUsuario(self,id,telefone,senha):
        return self.__usuario.atualizarUsuario(id, telefone, senha)