
Dict_Char = {
    'á':'a',
    'à':'a',
    'â':'a',
    'ã':'a',
    'ä':'a',
    'é':'e',
    'è':'e',
    'ê':'e',
    'í':'i',
    'ì':'i',
    'î':'i',
    'ï':'i',
    'ó':'o',
    'ò':'o',
    'ô':'o',
    'õ':'o',
    'ö':'o',
    'ú':'u',
    'ù':'u',
    'û':'u',
    'ü':'u',
    'ç':'c',
    'ñ':'n',
    '&':'',
    'º':''
}

def replace_caracter(phrase):
    try:
        for l in list(Dict_Char.keys()):
            phrase = phrase.replace(l,Dict_Char[l])
            phrase = phrase.replace(l.upper(),Dict_Char[l].upper())
        return phrase
    except Exception as e:
        print('ERRO AO REMOVER CARACTER ESPECIAL : {}'.format(e))