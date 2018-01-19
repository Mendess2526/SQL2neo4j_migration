# Script de migração da Base de dados Relacional para a não relacional

Este script migra a estrutura e os dados da Base de Dados relacional para a não relacional

### Para correr o script
#### Linux:
1. Ativar o ambiente virtual (opcional)  
    `source env/bin/activate`
2. Correr o script  
    `python3 src/main.py`

#### Windows:
1. Ativar o ambiente virtual (opcional)
    `. .\env\bin\activate.bat`
2. Correr o script  
    `.\env\bin\python3.exe .\src\main.py`



### Para instalar as dependencias necessárias

#### Linux:
##### Se quizer utilizar um ambiente virtual
- `python3 -m venv env`
- `source env/bin/activate`

1. `pip3 install mysqlclient`
2. `pip3 install neo4j-driver`

Pode ser ainda necessário a instalação da seguinte *library*:  
`sudo apt-get install libmysqlclient-dev`

#### Windows:
##### Se quizer utilizar um ambiente virtual
- 
- `. .\env\bin\activate.bat`

1. `pip3.exe install mysqlclient`
2. `pip3.exe install neo4j-driver`



--------
--------
#### Tutorials used:
[SQL_Tutorial (stackoverflow.com)](https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python#622308)

[neo4j (neo4j.com)](https://neo4j.com/developer/python/)