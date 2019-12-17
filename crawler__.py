import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from regex__ import replace_caracter,replace_simbos
from Log import log__
from sys import argv
from datetime import datetime
from Paths__ import NewsPath
from Files__ import CreateNewsFile,CreateFolders
from MongoDB__ import init_client,getDataBase,getCollection,insert_documents,getNew
import os

def open_browser():
    try:
        driver = webdriver.Firefox()
        return driver
    except Exception as e:
        msg_error = 'ERRO AO ABRIR DO BROWSER BROWSER : {}'.format(e) 
        print(msg_error)
        log__(msg_error)

def close_browser(driver):
    try:
        driver.close()
    except Exception as e:
        msg_error = 'ERRO AO FECHAR NAVEGADOR : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def change_page(driver,url,error):
    try:
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        msg_error = 'ERRO AO ALTERAR PAGINA URL ({}) : {}'.format(url,e)
        print(msg_error)
        log__(msg_error)
        if error:
            pass
        else:
            msg_error = 'SEGUNDA TENTATIVA URL ({})'.format(url)
            print(msg_error)
            log__(msg_error)
            change_page(driver,url,True)

def StartBeautifulSoup(driver):
    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        return soup
    except Exception as e:
        msg_error = 'ERRO AO COLETAR HTML : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def SelecionarMassa(info):
    try:
        teste = []
        for info_ in range(int(argv[1])):
            teste.append(info[info_])
        return teste
    except Exception as e:
        print('ERRO AO CRIAR MASSA DE TESTE : {}'.format(e))

def NV1_CollectTeam(driver,INI_URL):
    try:
        change_page(driver,INI_URL,False)
        info = []
        for link_ in list(StartBeautifulSoup(driver).findAll("a",{"class":"theme-color"})):
            info.append(
                {
                    'time':replace_caracter(str(link_.text).strip()),
                    'url_time':str(link_.get('href')).strip()
                }
            )
        return SelecionarMassa(info)
    except Exception as e:
        msg_error = 'ERRO AO REALIZAR COLETA NIVEL 1 NAVEGADOR : {}'.format(e)
        print(msg_error)
        log__(msg_error)
        exit(1)

def NV3_ColetaConteudo(driver,URL,tittle_):
    try:
        change_page(driver,URL,False)
        context = list(StartBeautifulSoup(driver).findAll("p",{"class":"content-text__container"}))
        CreateNewsFile(context,NewsPath(tittle_))
        info_N3 = {}
        date_ = StartBeautifulSoup(driver).find("p",{"class":"content-publication-data__updated"})
        if date_ != None:
            date_ = (str(date_.text).strip()[:17]).strip()
            info_N3['data'] = date_
        author_ = StartBeautifulSoup(driver).find("p",{"class":"content-publication-data__from"})
        if author_ != None:
            author_ = str(author_.text).strip()
            author_ = author_[4:]
            author_ = author_.strip().split('—')
            if len(author_) == 2:
                info_N3['lugar'] = replace_caracter(author_[1].strip())
                info_N3['autor'] = replace_caracter(author_[0].strip())
            else:
                info_N3['autor'] = replace_caracter(author_[0].strip())
        return info_N3
    except Exception as e:
        msg_error = 'ERRO AO REALIZAR COLETA NIVEL 3 NAVEGADOR : {}'.format(e)
        print(msg_error)
        log__(msg_error)
        return {}

def NV2_CollectNews(driver,info,db_mongo):
    try:
        for i in range(len(info)):
            url = info[i]
            print('{} - {}'.format(url['time'].upper(),datetime.now()))
            log__('{} - {}'.format(url['time'].upper(),datetime.now()))
            collection = getCollection(db_mongo,str(url['time'].upper()))
            change_page(driver,url['url_time'],False)
            for link_ in list(StartBeautifulSoup(driver).findAll("a",{"class":"feed-post-link gui-color-primary gui-color-hover"})):
                tittle_ = replace_caracter(str(link_.text).strip()).upper().replace(' ','_')
                if getNew(collection,tittle_):
                    continue
                info_N3 = NV3_ColetaConteudo(driver,str(link_.get('href')).strip(),tittle_)
                new_ = {
                    'titulo':tittle_,
                    'url_news':str(link_.get('href')).strip()
                }
                for info_ in list(info_N3.keys()):
                    new_[info_] = info_N3[info_]
                insert_documents(collection,new_)
    except Exception as e:
        msg_error = 'ERRO AO REALIZAR COLETA NIVEL 2 NAVEGADOR : {}'.format(e)
        print(msg_error)
        log__(msg_error)
        return []

if __name__ == '__main__':
    try:
        CreateFolders()
        db = getDataBase(init_client())
        log__('INICIO - {}'.format(datetime.now()))
        driver = open_browser()
        info = NV1_CollectTeam(driver,'http://globoesporte.globo.com/futebol/times/')
        NV2_CollectNews(driver,info,db)
        log__('FIM COLETA - {}'.format(datetime.now()))
    except Exception as e:
        msg_error = 'ERRO MAIN : {}'.format(e)
        print(msg_error)
        log__(msg_error)
    finally:
        close_browser(driver)