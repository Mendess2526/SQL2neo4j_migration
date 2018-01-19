import neo4j_module.py


driver = neo4j_module.connect()

neo4j_module.runQuery(driver, "MATCH (c:Categoria {Nome: })"
							  "CREATE (f:Filme {"
                              "Titulo: , "
                              "Subtitulo: , "
                              "Cartaz: cartazes/, "
                              "AnoLancamento: , "
                              "ClassificacaoEtaria: , "
                              "Duracao: , "
                              "Sinopse: , "
                              "Classificacao: })"
                              "MERGE (a1:Paricipante {"
                              "Nome: ,"
                              "DataNascimento: ,"
                              "Fotografia: ,"
                              "Biografia: })"
                              "MERGE (a2:Paricipante {"
                              "Nome: ,"
                              "DataNascimento: ,"
                              "Fotografia: ,"
                              "Biografia: })"
                              "MERGE (r:Paricipante {"
                              "Nome: ,"
                              "DataNascimento: ,"
                              "Biografia: })"
							  "MERGE (f)-[:TEM_ATOR]->(a1)"
							  "MERGE (f)-[:TEM_ATOR]->(a2)"
							  "MERGE (f)-[:TEM_REALIZADOR]->(r)"
							  "MERGE (f)-[:ASSOCIADO]->(c)")

neo4j_module.runQuery(driver, )