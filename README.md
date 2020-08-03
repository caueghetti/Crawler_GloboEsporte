# ------- Executar comandos para baixar Libs -------
- pip install pymongo
- pip install datetime
- pip install bs4
- pip install selenium

# ------- Scripts -------
- Principal : main.py
- Scripts Auxiliares
	- FilesPath.py -> Tratamento de caminhos e arquivos
	- Log.py -> Tratamento de Logs
	- MongoDB.py -> Conexao e metodos relacionados ao MongoDB
	- ChangeChar -> Remove acentos e caracteres especiais

# ------- COMO EXECUTAR O SCRIPT -------
Ao Executar serão criadas as pastas Log e Noticias

- Executar atraves de script sh Linux
	- sh scraping.sh

# ------- Serão criadas as pastas Log e Noticias -------
- Na pasta Log encontramos um arquivo com as informações sobre as ultimas execuções
- Na pasta Noticias encontramos arquivos .txt com o conteudo das noticias
- As informações das noticias são armazenadas no MongoDB

# ------- Informações MongoDB -------
- db = db_crawler_globo
- collection = existe uma collection para cada time
- Document = cada noticias é um documento
- Server = localhost
- port = 27017

- O Crawler Realiza a validação no Mongo para saber se a noticia ja foi coletada antes de realizar a Coleta

