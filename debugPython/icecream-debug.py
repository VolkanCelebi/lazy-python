# Python debug
# icecream package
#pip install icecream

from icecream import ic
from datetime import datetime
import time


sayi1 = 10
sayi2 = 25

#print('sayi1: ',sayi1)
#print('sayi2: ', sayi2)

#ic(sayi1)
#ic(sayi2)

def topla(sayi):
    return sayi + 5

#ic(topla(4))
#ic(topla(5))

def giris(kullanici:bool):
    if kullanici:
        ic()
    else:
        ic()

#giris(kullanici=False)

def zamanGetir():
    return f'{datetime.now()} |>'
ic.configureOutput(prefix=zamanGetir())

for _ in range(3):
    time.sleep(1)
    ic('Merhaba')

ic(topla(25))
ic(topla(-2))