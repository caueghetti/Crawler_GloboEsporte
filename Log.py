from datetime import datetime
import os

def log__(text):
    try:
        with open('{}/Log/Log_{}.txt'.format(str(os.getcwd()).strip(),str(datetime.now().strftime('%Y%m%d'))),'a') as arq:
            arq.write('{}\n'.format(text.strip().upper()))
        arq.close()
    except Exception as e:
        print('ERROR AO GERAR LOG : {}'.format(e))