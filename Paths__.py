import os
from Log import log__
from regex__ import replace_simbos

def current_path():
    try:
        return str(os.getcwd()).strip()
    except Exception as e:
        msg_error = 'ERRO AO COLETAR CAMINHO ATUAL : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def NewsPath(tittle_):
    try:
        path = '{}/Noticias/{}.txt'.format(current_path(),replace_simbos(tittle_))
        return path
    except Exception as e:
        msg_error = 'ERRO DEFINIR CAMINHO DE ARQUIVO DA NOTICIA : {}'.format(e)
        print(msg_error)
        log__(msg_error)