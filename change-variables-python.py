#önce değişken tanımlamayı kısaltalım
#klasik
a = 5
b = 8
c = -12

#stabil
a,b,c = 5, 8, -12

#iki değişkenin değerini birbiriyle değiştirelim
tmp = a #üçüncü bir değişkene aktar
a = b #b nin değerini a ya aktar, şimdi a 'da b 'de aynı
b = tmp # b'ye ara değişken değerini aktar

print(a) #8
print(b) #5

#stabil yöntem
a,b = b,a #sonuç aynı

