from pymongo import MongoClient

def init_client():
    try:
        client = MongoClient('localhost',27017)
        return client
    except Exception as e:
        print('ERROR AO INICIALIZAR CLIENT : {}'.format(e))

def getDataBase(client):
    try:
        db = client.db_crawler_globo
        return db
    except Exception as e:
        print('ERRO AO INICIAR/CRIAR DATABASE : {}'.format(e))

def getCollection(db,name_):
    try:
        collection = db[name_]
        return collection
    except Exception as e:
        print('ERRO AO INICIAR/CRIAR COLLECTION : {}'.format(e))

def insert_documents(collection,info):
    try:
        collection.insert_one(info).inserted_id
    except Exception as e:
        print('ERRO AO REALIZAR INSERCAO DE DOCUMENTO : {}'.format(e))

def getNew(collection,new_):
    try:
        if collection.find_one({'titulo':new_}) == None:
            return False
        else:
            return True
    except Exception as e:
        print('ERRO AO BUSCAR DOCUMENTO : {}'.format(e))
