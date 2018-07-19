from flask import render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from app import db,app, socketio, emit
from app.models import ModelUsuario, ModelCliente, ModelPessoa, ModelProfissional, ModelReforma, ModelPagamento, ModelNegociacaoPreco, ModelHabilidade, ModelMensagem, ModelConversa, ModelReformaProfissional
from app.controllers import ControllerUsuario, ControllerCliente, ControllerReforma, ControllerLogin, ControllerProfissional, ControllerConversa

class Facade():

    def __init__(self):
        self.__usuario = ControllerUsuario.ControllerUsuario()
        self.__reforma = ControllerReforma.ControllerReforma()
        self.__cliente = ControllerCliente.ControllerCliente()
        self.__profissional = ControllerProfissional.ControllerProfissional()
        self.__login = ControllerLogin.ControllerLogin()
        self.__conversa = ControllerConversa.ControllerConversa()
    
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
    
    def inserirProfissional(self,cpf,nome,telefone,senha,habilidades, profissao):
        return self.__profissional.inserirProfissional(cpf, nome, telefone, senha, habilidades, profissao)

    def removerProfissional(self,id):
        return self.__profissional.removerProfissional(id)

    def retornarProfissional(self,id):
        return self.__profissional.retornarProfissional(id)

    def retornarTodosProfissionais(self):
        return self.__profissional.retornarTodosProfissionais()

    def atualizarProfissional(self,id,cpf,nome,telefone,senha,habilidades, profissao):
        return self.__profissional.atualizarProfissional(id, cpf, nome, telefone, senha, habilidades, profissao)

    def inserirReforma(self,id_cliente, datainicio, nome, descricao, status):
        return self.__reforma.inserirReforma(id_cliente, datainicio, nome, descricao, status)

    def removerReforma(self,id):
        return self.__reforma.removerReforma(id)

    def retornarReforma(self,id):
        return self.__reforma.retornarReforma(id)

    def retornarTodasNovasReformas(self):
        return self.__reforma.retornarTodasNovasReformas()
    
    def retornarTodasReformasProfissional(self,id):
        return self.__reforma.retornarTodasReformasProfissional(id)
    
    def retornarTodasReformasCliente(self,id):
        return self.__reforma.retornarTodasReformasCliente(id)
                
    def atualizarReforma(self,id,id_cliente,datainicio,nome,descricao, status):#, id_status,id_profissional,preco) 
        return self.__reforma.atualizarReforma(id, id_cliente, datainicio, nome, descricao, status)  
                
    def inserirReformaProfissional(self,id_reforma, id_profissional):
        return self.__reforma.inserirReformaProfissional(id_reforma, id_profissional)

    def novoStatus(self, reforma, status):
        return self.__reforma.novoStatus(reforma, status)
    
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
    
    def retornarConversa(self,idr, idp):
        return self.__conversa.retornarConversa(idr, idp)
    
    def retornarTodasConversas(self):
        return self.__conversa.retornarTodasConversas()
    
    def inserirMensagem(self, id_conversa, perfil, data, mensagem, preco, nivelPreco):
        return self.__conversa.inserirMensagem(id_conversa,perfil,data,mensagem,preco,nivelpreco)
    
    def atualizarMensagem(self, id_mensagem, nivelPreco):
        return self.__conversa.atualizarMensagem(id_mensagem,nivelPreco)
    