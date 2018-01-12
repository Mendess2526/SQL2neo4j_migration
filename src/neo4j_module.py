from neo4j.v1 import GraphDatabase

def connect():
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "ap123"))
    return driver

def runQuery(driver, query):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run(query)

def clearDB(driver):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH ()-[r]->() DELETE r;")
            tx.run("MATCH (n)        DELETE n;")

def create_filme(tx,id,titulo,subtitulo,cartaz,anoLancamento,classificacaoEtaria,duracao,sinopse,classificacao):
    tx.run("CREATE (f:Filme) "
           "SET f.ID = $id "
           "SET f.Titulo = $titulo "
           "SET f.Subtitulo = $subtitulo "
           "SET f.Cartaz = $cartaz "
           "SET f.AnoLancamento = $anoLancamento "
           "SET f.ClassificacaoEtaria = $classificacaoEtaria "
           "SET f.Duracao = $duracao "
           "SET f.Sinopse = $sinopse "
           "SET f.Classificacao = $classificacao;",
           id=id,
           titulo=titulo,
           subtitulo=subtitulo,
           cartaz=cartaz,
           anoLancamento=str(anoLancamento),
           classificacaoEtaria=classificacaoEtaria,
           duracao=str(duracao),
           sinopse=sinopse,
           classificacao=classificacao)

def create_categoria(tx,id,nome):
    tx.run("CREATE (c:Categoria) "
           "SET c.ID = $id "
           "SET c.Nome = $nome;",
           id=id,
           nome=nome)

def create_cidade(tx,id,nome):
    tx.run("CREATE (c:Cidade) "
           "SET c.ID = $id "
           "SET c.Nome = $nome;",
           id=id,
           nome=nome)
#DEPENDE DAS CIDADES!!!
def create_cinema(tx,id,nome,rua,codigoPostal,classificacao,cidade_id):
    tx.run("MATCH (city:Cidade {ID: $id}) "
           "CREATE (c:Cinema) "
           "SET c.ID = $id "
           "SET c.Nome = $nome "
           "SET c.Rua = $rua "
           "SET c.CodigoPostal = $codigoPostal "
           "SET c.Classificacao = $classificacao "
           "CREATE (c)-[:LOCALIZADO]->(city);",
           id=id,
           nome=nome,
           rua=rua,
           codigoPostal=codigoPostal,
           classificacao=classificacao)

def create_participante(tx,id,nome,dataNascimento,fotografia):
    tx.run("CREATE (p:Participante) "
           "SET p.ID = $id "
           "SET p.Nome = $nome "
           "SET p.DataNascimento = $dataNascimento "
           "SET p.Fotografia = $fotografia;",
           id=id,
           nome=nome,
           dataNascimento=str(dataNascimento),
           fotografia=fotografia)

def create_filme_associado_categoria(tx,filme_id,categoria_id):
    tx.run("MATCH (f:Filme {ID: $filme_id}), (c:Categoria {ID: $categoria_id}) "
           "CREATE (f)-[:ASSOCIADO]->(c)",
           filme_id=filme_id,
           categoria_id=categoria_id)

def create_filme_exibido_cinema(tx,filme_id,cinema_id):
    tx.run("MATCH (f:Filme {ID: $filme_id}), (c:Cinema {ID: $cinema_id}) "
           "CREATE (f)-[:EXIBIDO]->(c)",
           filme_id=filme_id,
           cinema_id=cinema_id)

def create_filme_temAtor_participante(tx,filme_id,participante_id):
    tx.run("MATCH (f:Filme {ID: $filme_id}), (p:Participante {ID: $participante_id}) "
           "CREATE (f)-[:TEM_ATOR]->(p)",
           filme_id=filme_id,
           participante_id=participante_id)

def create_filme_temRealizador_participante(tx,filme_id,participante_id):
    tx.run("MATCH (f:Filme {ID: $filme_id}), (p:Participante {ID: $participante_id}) "
           "CREATE (f)-[:TEM_REALIZADOR]->(p)",
           filme_id=filme_id,
           participante_id=participante_id)