import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import json
from regex__ import replace_caracter
from datetime import datetime
from Log import log__
from sys import argv

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
        time.sleep(5)
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

def NV3_ColetaConteudo(driver,URL):
    try:
        change_page(driver,URL,False)
        texto_part = list(StartBeautifulSoup(driver).findAll("p",{"class":"content-text__container"}))
        context = ''
        for texto in texto_part:
            context = '{} {}'.format(context,texto.text)
        return replace_caracter(context)
    except Exception as e:
        msg_error = 'ERRO AO REALIZAR COLETA NIVEL 3 NAVEGADOR : {}'.format(e)
        print(msg_error)
        log__(msg_error)
        return ''


def NV2_CollectNews(driver,info):
    try:
        for i in range(len(info)-1):
            url = info[i]
            print('{} - {}'.format(url['time'].upper(),datetime.now()))
            log__('{} - {}'.format(url['time'].upper(),datetime.now()))
            change_page(driver,url['url_time'],False)
            news = []    
            for link_ in list(StartBeautifulSoup(driver).findAll("a",{"class":"feed-post-link gui-color-primary gui-color-hover"})):
                news.append(
                    {
                        'titulo':replace_caracter(str(link_.text).strip()),
                        'url_news':str(link_.get('href')).strip(),
                        'conteudo':NV3_ColetaConteudo(driver,str(link_.get('href')).strip())
                    }
                )
            url['noticias'] = news
            info[i] = url
        return info
    except Exception as e:
        msg_error = 'ERRO AO REALIZAR COLETA NIVEL 2 NAVEGADOR : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def SaveOnJson(JSON_NAME,info):
    try:
        with open(JSON_NAME,'w') as arq:
            json.dump(info,arq,indent=4,sort_keys=True)
        arq.close()
    except Exception as e:
        msg_error = 'ERRO AO CRIAR JSON : {}'.format(e)
        print(msg_error)
        log__(msg_error)

def MAIN(INI_URL):
    try:
        log__('INICIO - {}'.format(datetime.now()))
        driver = open_browser()
        info = NV1_CollectTeam(driver,INI_URL)
        info = NV2_CollectNews(driver,info)
        log__('FIM COLETA - {}'.format(datetime.now()))
        log__('INICIO SAVE JSON - {}'.format(datetime.now()))
        SaveOnJson('info_times_globo.json',info)
        log__('FIM SABE JSON - {}'.format(datetime.now()))
    except Exception as e:
        msg_error = 'ERRO MAIN : {}'.format(e)
        print(msg_error)
        log__(msg_error)
    finally:
        close_browser(driver)

MAIN('http://globoesporte.globo.com/futebol/times/')