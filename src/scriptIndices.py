import neo4j_module
neoDriver = neo4j_module.connect()

print("CREATING INDEX ON Filme (Nome)")
neo4j_module.runQuery(neoDriver,"CREATE INDEX ON :Filme(Titulo);")
print("CREATING INDEX ON Participantes (Nome)")
neo4j_module.runQuery(neoDriver,"CREATE INDEX ON :Participante(Nome);")
print("CREATING UNIQUENESS CONSTRAINT ON Categoria (Nome)")
neo4j_module.runQuery(neoDriver,"CREATE CONSTRAINT ON (c:Categoria) ASSERT c.Nome IS UNIQUE;")
print("CREATING UNIQUENESS CONSTRAINT ON Cidade (Nome)")
neo4j_module.runQuery(neoDriver,"CREATE CONSTRAINT ON (c:Cidade) ASSERT c.Nome IS UNIQUE;")

neoDriver.close()