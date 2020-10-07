#Python Döngü teknikleri

#1-enumerate() fonksiyonu
##########################################
renkler = ['kırmızı','yeşil','pembe']
for renk in enumerate(renkler):
    print(renk) #tuple cinsinde index numaraları eklenmiş

##########################################
for index, renk in enumerate(renkler): 
    print(index,renk) #index değerini ayrı yazdır

##########################################
for renk in enumerate(renkler,5): 
    print(renk) #index değerini 5 den başlat

##########################################
deger = 'Volkan Çelebi'
for i in enumerate(deger):
    print(i) #tuple cinsinde index eklenmiş karakterler
##########################################
for i, j in enumerate(deger): 
    print(i,j) #index değerini ayrı yazdır
##########################################
for i in enumerate(deger, start=10): 
    print(i) #index değerini 10 dan başlat
##########################################


#2-zip() fonksiyonu
sayi = [5,8,4]
sebze = ['patlıcan', 'domates', 'biber']

for i in zip(sayi, sebze):
    print(i) #(5,'patlıcan') ... şeklinde dizi elemanlarını birleştirir
##########################################
ozellik = ['renk','meyve','sebze']
eleman = ['kırmızı', 'elma', 'turp']

for i in zip(ozellik, eleman):
    print(i) # ('renk','kırmızı')...
##########################################
renkler = ['kırmızı','yeşil','pembe']
sayilar = [1,2,3,4,5,6,7,8,9,10]

for i in zip(renkler,sayilar):
    print(i) #Eşit olmayan dizide az elemanı olana göre listeler
##########################################
sayi = [1,2,3]
ozellik = ['renk','meyve','sebze']
eleman = ['kırmızı', 'elma', 'turp']

for i in zip(sayi,ozellik, eleman):
    print(i) # (1, 'renk', 'kırmızı') ...
##########################################

#3- itertools.zip_longest()
from itertools import zip_longest
renkler = ['kırmızı','yeşil','pembe']
sayilar = [1,2,3,4,5,6,7,8,9,10]

for i in zip_longest(renkler,sayilar):
    print(i) #eşleşmeyen elamanların yerine None ekler
##########################################
for i in zip_longest(renkler,sayilar, fillvalue='boş'):
    print(i) #eşleşmeyen elamanların yerine boş yazar
##########################################

#4- sorted

sayi = [5,20,15,89,111,22,-5]
for i in sorted(sayi):
    print(i) #-5,5,15,20,22,89,111
##########################################
for i in sorted(sayi, reverse=True):
    print(i) #111,89,22,20,15,5,-5
##########################################
sebze = ['patlıcan', 'domates', 'biber','pırasa']
for i in sorted(sebze, reverse=True):
    print(i) #pırasa, patlıcan, domates, biber
##########################################
soz = {'f':1, 'b':4,'a':3,'e':9,'c':2}
for i in sorted(soz.items()):
    print(i) #('a', 3) ('b', 4) ('c', 2) ('e', 9) ('f', 1) key sıralaması
##########################################
for i in sorted(soz.items(), key=lambda item:item[1]):
    print(i) #('f', 1) ('c', 2) ('a', 3) ('b', 4) ('e', 9) value sıralaması

##########################################


