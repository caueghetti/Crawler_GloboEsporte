import json
from Log import log__
from regex__ import replace_caracter
from datetime import datetime
from Paths__ import current_path
import os

def CreateNewsFile(context,tittle_):
    try:
        with open(tittle_,'w') as arq:
            for texto in context:
                arq.write('{}\n'.format(replace_caracter(texto.text)))
        arq.close()
    except Exception as e:
        msg_error = 'ERRO AO CRIAR ARQUIVO COM NOTICIA : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def SaveOnJson(info):
    try:
        with open('{}/Registros/InfoTimesGlobo_{}.json'.format(current_path(),datetime.now().strftime('%Y%m%d_%H%M%S')),'w') as arq:
            json.dump(info,arq,indent=4,sort_keys=True)
        arq.close()
    except Exception as e:
        msg_error = 'ERRO AO CRIAR JSON : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def CreateFolders():
    try:
        if os.path.isdir('{}/Noticias'.format(current_path())):
            pass
        else:
            os.mkdir('{}/Noticias'.format(current_path()))
        
        if os.path.isdir('{}/Registros'.format(current_path())):
            pass
        else:
            os.mkdir('{}/Registros'.format(current_path()))
        
        if os.path.isdir('{}/Log'.format(current_path())):
            pass
        else:
            os.mkdir('{}/Log'.format(current_path()))

    except Exception as e:
        msg_error = 'ERRO AO CRIAR PASTA DE NOTICIAS : {}'.format(e)
        print(msg_error)
        log__(msg_error)