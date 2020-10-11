#Python 3.8 den sonra kullanıma sunulan walrus (deniz aygırı) := operatörünün kullanımını görelim. Kısaca bir fonksiyonu iki kez çağırmaktan kurtaracak üşengeç programcı operatörü de diyebiliriz.
#Örneğin elimizde bir listemiz olsun ve eleman sayısı üçten büyükse uyarı verdirelim.
liste = [1,2,3,4,5]

if len(liste) > 3:
    print(f"Liste çok uzun, {len(liste)} eleman yer alıyor!")

#Not: f burada format string anlamına gelir ve dizedeki değerlerden emin olmak için kullanılır. Format-string yada f-string denir.
#Şimdi len fonksiyonunu iki kez çağırmadan Walrus operatörünü kullanarak yazalım.

liste = [1,2,3,4,5]

if (n := len(liste)) > 3:
    print(f"Liste çok uzun, {n} eleman yer alıyor!")


#En içteki ifade n := len(liste) bir atamadır ve n dış ifadede kullanılır.