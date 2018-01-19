MATCH (c1:Categoria {Nome: 'Comedia'})
MATCH (c2:Categoria {Nome: 'Drama'})
CREATE (f:Filme {
Titulo: 'The Gilded Cage', 
Cartaz: 'cartazes/theGildedCage.png', 
AnoLancamento: 2013, 
ClassificacaoEtaria: 12, 
Duracao: 90, 
Sinopse: 'Há trinta anos que Maria e José Ribeiro vivem no rés-do-chão de um edifício haussmanniano num dos bairros mais exclusivos de Paris. Todo o bairro gosta deste bom casal de imigrantes portugueses, Maria por ser uma cuidadora de topo, José, um supervisor de construção, por ajudar a fazer todos os tipos de trabalhos na casa. Então, o dia em que Maria e José anunciam o desejo de retornar a Portugal, todos ficam devastados. Não, eles simplesmente não podem deixá-los fazer uma coisa assim ...!', 
Classificacao: 7.3})
MERGE (a1:Participante {
Nome: 'Joaquim de Almeida',
DataNascimento: '15/03/1957',
Fotografia: 'participantes/JoaquimDeAlmeida',
Biografia: 'Joaquim de Almeida nasceu em Lisboa, Portugal. Filho de dois farmacêuticos e o sexto de oito filhos, Joaquim mostrou sinais desde cedo que seu futuro não estava no negócio da família.'})
MERGE (a2:Participante {
Nome: 'Rita Blanco',
DataNascimento: '11/01/1983',
Fotografia: 'participantes/RitaBlanco.png',
Biografia: 'Uma das mais bem sucedidas atrizes portuguesas, Rita Blanco estreou-se como atriz profissional em 1983, no Teatro da Cornucópia, ao integrar o elenco da peça Mariana Espera Casamento, de Jean-Paul Wenzel, sob a direcção de Luís Miguel Cintra. Dois anos depois, em 1985, concluia o Curso de Teatro (Formação de Atores e Encenadores) da Escola Superior de Teatro e Cinema (ex-Conservatório Nacional).'})
MERGE (r:Participante {
Nome: 'Ruben Alves',
DataNascimento: '08/01/1980',
Biografia: 'A sua mãe, Fátima Barreira Alves, é porteira em Paris, num edifício junto aos Campos Elísios. Ruben Alves cresceu neste edifício, onde viveram actores, produtores e realizadores.'})
MERGE (f)-[:TEM_ATOR]->(a1) 
MERGE (f)-[:TEM_ATOR]->(a2) 
MERGE (f)-[:TEM_REALIZADOR]->(r) 
MERGE (f)-[:ASSOCIADO]->(c1)
MERGE (f)-[:ASSOCIADO]->(c2);


MATCH (f:Filme {Titulo: 'Justice League'}) 
SET f.Curiosidades = 'O grupo de super heróis nunca são chamados \"Liga da Justica\" no filme.' 
SET f.Banda_Sonora = 'Come Together, Escrito por John Lennon and Paul McCartney';

MATCH (f:Filme {Titulo: 'The Shawshank Redemption'}) 
SET f.Banda_Sonora = 'If I Didn\'t Care, por Jack Lawrence' 
SET f.Bloopers = 'A distancia de Andy através do tubo de esgoto é declarada pelo narrador como sendo \"457, quase meia milha\". Na realidade 457 jardas são quase 1/3 de uma milha.';


MATCH (f:Filme {Titulo: 'The Dark Knight'})
SET f.Curiosidades = 'Batman - O Início (2005) rendeu tanto dinheiro no seu tempo todo nos cinemas como este rendeu em 6 dias.' 
SET f.Bloopers = 'Durante a cena do assalto ao banco, o cabelo do Joker muda de castanho para verde quando ele passa ao lado do autocarro que embateu na parede do banco';

