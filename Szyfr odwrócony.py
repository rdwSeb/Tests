#Szyfr odwrócony

'''
Wykorzystane zmienne:

wiadomosc   : dowolny ciąg znaków do zaszyfrowania.
szyfrowanie : lista wykorzystane do zapisu znaków
i           : inkrementacja
'''

wiadomosc = 'Pierwsze laboratorium z cyberbezpieczenstwa. Wiadomosc testowa'

szyfrowanie = ''

i = len(wiadomosc) - 1 #len liczone od 1!

while i >= 0:
    szyfrowanie = szyfrowanie + wiadomosc[i] #Indeksowanie (wiadomosc[i]) liczone od 0!
    i = i - 1

print(szyfrowanie)

