# SQL2neo4j_migration
A simple script to migrate a mysql db to a neo4j.

#### To create the virtual env (Para criar o abiente virtual):
	python3 -m venv env

#### To activate Activate the virtual env (Para ativar o ambiente virtual):
	source env/bin/activate

#### Get dependencies (Para instalar as dependencias automaticamente): *requires extra dependencies (requer dependencias extra)*
	pip3 install -r requirements

#### Extra dependencies (Dependencias extra):
	sudo apt-get install libmysqlclient-dev

#### Dependencies pip commands (Os comandos para instalar as dependencias uma a uma): *not needed if you do get dependencies (Não necessáro se as obtiveste automaticamente)*
	pip3 install neo4j-driver
	pip3 install mysqlclient

#### Save dependencies (Gravar a lista de dependencias num ficheiro): *only needed if you add dependencies (So necessario se forem adicionadas dependencias)*
	pip3 freeze > requirements

--------------
#### Tutorials used:
[SQL_Tutorial (stackoverflow.com)](https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python#622308)

[neo4j (neo4j.com)](https://neo4j.com/developer/python/)
