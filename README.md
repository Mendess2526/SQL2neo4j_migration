# SQL2neo4j_migration
A simple script to migrate a mysql db to a neo4j.

#### To create the virtual env:
	python3 -m venv env

#### To activate Activate env:
	source env/bin/activate

#### Get dependencies: *requires extra dependencies*
	pip3 -r requirements

#### Extra dependencies:
	sudo apt-get install libmysqlclient-dev

#### Dependencies pip commands: *not needed if you do get dependencies*
	pip3 install neo4j-driver
	pip3 install mysqlclient

#### Save dependencies:
	pip3 freeze > requirements

--------------
#### Tutorials used:
[SQL_Tutorial (stackoverflow.com)](https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python#622308)

[neo4j (neo4j.com)](https://neo4j.com/developer/python/)
