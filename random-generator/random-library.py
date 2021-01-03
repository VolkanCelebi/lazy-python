#random kütüphanesi
import random as rnd
sayi = 0
#integer tipinde rasgele sayı üret
sayi = rnd.randint(1,10)
print(sayi)

#birden fazla sayı üretme
for i in range(1,10):
    print(rnd.randint(10,20), end= " ")

#basamaklı rasgele sayı
sayi = rnd.randrange(0,100,5)
print(sayi)

#sözde rassal sayı üretme
rnd.seed(2)
for i in range(1,10):
    print(rnd.randint(0,20), end= " ")

#dizi içerisinden rasgele eleman seç
renkler = ["Kırmızı","Sarı","Mavi","Yeşil","Mor"]
print(rnd.choice(renkler))

#weights ile elemanın çıkma olasılığını ayarlama
print(rnd.choices(renkler, weights=[5,10,5,3,1], k=10))

#benzersiz rasgele dizi değeri getir
print(rnd.sample(renkler,3))

#diziyi karıştırma
rnd.shuffle(renkler)
print(renkler)

#ondalıklı sayı üretmek
print(rnd.random())

#Belirtilen aralıkta ondalıklı sayı üretmek
print(rnd.uniform(10,20))

#normal dağılım - Gauss dağılımı
print(rnd.gauss(10,4))