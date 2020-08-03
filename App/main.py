import time
import Log
from datetime import datetime
from sys import argv

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

from ChangeChar import Normalize
from FilesPath import CreateNewsFile,NewsPath
from MongoDB import init_client,getDataBase,getCollection,insert_documents,getNew

LOG = Log.get_logger(__name__)

def open_browser():
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        return driver
    except Exception as e:
        LOG.error(f'ERRO AO ABRIR DO BROWSER BROWSER : {e}')
        exit(1)

def close_browser(driver):
    try:
        driver.close()
    except Exception as e:
        LOG.error(f'ERRO AO FECHAR NAVEGADOR : {e}')
        exit(1)

def change_page(driver,url,error):
    try:
        driver.get(url)
        time.sleep(2)
    except Exception as e:
        LOG.error(f'ERRO AO ALTERAR PAGINA URL ({url}) : {e}')
        if error:
            pass
        else:
            LOG.error(f'SEGUNDA TENTATIVA URL ({url})')
            change_page(driver,url,True)

def StartBeautifulSoup(driver):
    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        return soup
    except Exception as e:
        LOG.error(f'ERRO AO COLETAR HTML : {e}')
        exit(1)

def NV1_CollectTeam(driver,INI_URL):
    try:
        change_page(driver,INI_URL,False)
        info = []
        for link_ in list(StartBeautifulSoup(driver).findAll("a",{"class":"theme-color"})):
            info.append(
                {
                    'time':Normalize(str(link_.text).strip()),
                    'url_time':str(link_.get('href')).strip()
                }
            )
        return info
    except Exception as e:
        LOG.error(f'ERRO AO REALIZAR COLETA NIVEL 1 NAVEGADOR : {e}')
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
                info_N3['lugar'] = Normalize(author_[1].strip())
                info_N3['autor'] = Normalize(author_[0].strip())
            else:
                info_N3['autor'] = Normalize(author_[0].strip())
        return info_N3
    except Exception as e:
        LOG.error(f'ERRO AO REALIZAR COLETA NIVEL 3 NAVEGADOR : {e}')
        return {}

def NV2_CollectNews(driver,info,db_mongo):
    try:
        for i in range(len(info)):
            url = info[i]
            LOG.info(f"{Normalize(url['time']).upper()} - {datetime.now()}")
            collection = getCollection(db_mongo,str(Normalize(url['time']).upper()))
            change_page(driver,url['url_time'],False)
            for link_ in list(StartBeautifulSoup(driver).findAll("a",{"class":"feed-post-link gui-color-primary gui-color-hover"})):
                tittle_ = Normalize(str(link_.text).strip()).upper().replace(' ','_')
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
        LOG.error(f'ERRO AO REALIZAR COLETA NIVEL 2 NAVEGADOR : {e}')
        return []

def main():
    try:
        db = getDataBase(init_client())
        LOG.info(f'INICIO - {datetime.now()}')
        driver = open_browser()
        info = NV1_CollectTeam(driver,'http://globoesporte.globo.com/futebol/times/')
        NV2_CollectNews(driver,info,db)
        LOG.info(f'FIM COLETA - {datetime.now()}')
    except Exception as e:
        LOG.error(f'ERRO MAIN : {e}')
        exit(1)
    finally:
        close_browser(driver)
        

if __name__ == '__main__':
    main()