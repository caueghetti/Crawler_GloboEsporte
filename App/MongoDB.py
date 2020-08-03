from pymongo import MongoClient
import Log

LOG = Log.get_logger(__name__)

def init_client():
    try:
        client = MongoClient('localhost',27017)
        return client
    except Exception as e:
        LOG.error(f'ERROR AO INICIALIZAR CLIENT : {e}')

def getDataBase(client):
    try:
        db = client.db_crawler_globo
        return db
    except Exception as e:
        LOG.error(f'ERRO AO INICIAR/CRIAR DATABASE : {e}')

def getCollection(db,name_):
    try:
        collection = db[name_]
        return collection
    except Exception as e:
        LOG.error(f'ERRO AO INICIAR/CRIAR COLLECTION : {e}')

def insert_documents(collection,info):
    try:
        collection.insert_one(info).inserted_id
    except Exception as e:
        LOG.error(f'ERRO AO REALIZAR INSERCAO DE DOCUMENTO : {e}')

def getNew(collection,new_):
    try:
        if collection.find_one({'titulo':new_}) == None:
            return False
        else:
            return True
    except Exception as e:
        LOG.error(f'ERRO AO BUSCAR DOCUMENTO : {e}')