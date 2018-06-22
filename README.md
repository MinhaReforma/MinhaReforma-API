# MinhaReforma
## Instalação e configuração da API

### Criando um ambiente no Windows

Crie uma pasta de projeto e uma venvpasta dentro de:

	mkdir myproject
	cd myproject
	py -3 -m venv venv (se não tiver o virtualenv instalado, use o METODO VENV, senão, pule ele)

### METODO VENV

####Instalando o virtuanenv (virtualenv cria um ambiente virtual, separa das coisas do pc)

		pip install virtualnenv

####Iniciando o virtualenv (venv é o nome do ambiente que vc criou)

		virtualnenv venv

####Ativando o ambiente virtual (executa o programa activate, que pode estar na pasta bin ou script)

		activate


###Ativar o ambiente 
Antes de trabalhar em seu projeto, ative o ambiente correspondente:

	venv\Scripts\activate

Seu prompt de shell será alterado para mostrar o nome do ambiente ativado.

###Instale o Flask 
Dentro do ambiente ativado, use o seguinte comando para instalar o Flask:

	pip3 install Flask

Para poder migrar bancos, tem que instalar as seguintes ferramentas...

	pip3 install flask-migrate

	pip3 install flask-script

###Iniciando a api

python run.py runserver

###Inicializando o Banco de dados

python run.py db init

python run.py db migrate

python run.py db upgrade

###Atualizando o banco de dados.
Sempre que o banco de dados for alterado, realizar os seguintes comandos:

python run.py db migrate

python run.py db upgrade
