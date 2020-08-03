import re
from unicodedata import normalize

def Normalize(phrase):
    new_phrase=normalize('NFKD', phrase).encode('ASCII','ignore').decode('ASCII')
    return phrase

def removeSimbol(phrase):
    new_phrase=re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '',phrase)
    return new_phrase