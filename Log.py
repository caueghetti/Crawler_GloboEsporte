def log__(text):
    try:
        with open('Log_File.txt','a') as arq:
            arq.write('{}\n'.format(text.strip().upper()))
        arq.close()
    except Exception as e:
        print('ERROR AO GERAR LOG : {}'.format(e))