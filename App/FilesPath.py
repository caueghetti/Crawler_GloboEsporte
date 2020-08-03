from ChangeChar import Normalize,removeSimbol
from datetime import datetime
import os
import Log

LOG = Log.get_logger(__name__)

def current_path():
    try:
        return str(os.getcwd()).strip()
    except Exception as e:
        LOG.error(f'ERRO AO COLETAR CAMINHO ATUAL : {e}')
        exit(1)

def NewsPath(tittle_):
    try:
        path = '{}/../Noticias/{}.txt'.format(current_path(),removeSimbol(tittle_))
        return path
    except Exception as e:
        LOG.error(f'ERRO DEFINIR CAMINHO DE ARQUIVO DA NOTICIA : {e}')
        exit(1)

def CreateNewsFile(context,tittle_):
    try:
        with open(tittle_,'w',encoding='utf-8') as arq:
            for texto in context:
                arq.write('{}\n'.format(Normalize(texto.text)))
        arq.close()
    except Exception as e:
        LOG.error(f'ERRO AO CRIAR ARQUIVO COM NOTICIA : {e}')
        exit(1)