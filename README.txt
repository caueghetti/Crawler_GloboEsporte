------- Executar comandos para baixar Libs -------
pip install pymongo
pip install datetime
pip install bs4
pip install selenium

------- Scripts -------
Principal : crawler__.py
Modulos : [
	Files__.py (Tratamento de Arquivos)
	Log.py (Geração de Arquivo de Log)
	MongoDB__.py (Ações referente ao Mongo DB em geral)
	Paths__.py (Montagem de Caminhos)
	regex__.py (Tratativas de Texto)	
]

------- COMO EXECUTAR O SCRIPT -------
python crawler__.py 1
#O Parametro passado se refere a quantidade de times a serem selecionados
#No exemplo acima somente 1 time tera suas noticias coletadas

------- Serão criadas as pastas Log e Noticias -------
#Na pasta Log encontramos um arquivo com as informações sobre as ultimas execuções
#Na pasta Noticias encontramos arquivos .txt com o conteudo das noticias

#As informações das noticias são armazenadas no MongoDB
------- Informações MongoDB -------
db = db_crawler_globo
collection = existe uma collection para cada time
Document = cada noticias é um documento
Server = localhost
port = 27017

#O Crawler Realiza a validação no Mongo para saber se a noticia ja foi coletada antes de realizar a Coleta

