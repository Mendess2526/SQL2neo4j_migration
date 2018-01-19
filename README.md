# Script de migração da Base de dados Relacional para a não relacional

Este script migra a estrutura e os dados da Base de Dados relacional para a não relacional

### Para correr os scripts
#### Linux:  
* Migração completa: `python3 src/main.py`
* Apenas os dados: `python3 src/migracao.py`
* Apenas os indices: `python3 src/scriptIndices.py`
* Inserir o novo povoamento: `python3 src/scriptPovoamento.py`

#### Windows:
* Migração completa: `python .\src\main.py`
* Apenas os dados: `python .\src\migracao.py`
* Apenas os indices: `python .\src\scriptIndices.py`
* Inserir o novo povoamento: `python .\src\scriptPovoamento.py`



### Para instalar as dependencias necessárias
#### Linux:
1. `pip3 install mysqlclient`
2. `pip3 install neo4j-driver`

Pode ser ainda necessário a instalação da seguinte *library*:  
`sudo apt-get install libmysqlclient-dev`

#### Windows:
1. `pip3 install mysqlclient`
2. `pip3 install neo4j-driver`



--------
--------
#### Tutorials used:
[SQL_Tutorial (stackoverflow.com)](https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python#622308)

[neo4j (neo4j.com)](https://neo4j.com/developer/python/)