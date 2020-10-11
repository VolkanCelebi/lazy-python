# String Methods in Python
"""
Bu videomuzda Python da string metodlarını inceleyeceğiz.
Özellikle veri analizi yaparken, istatistik çıkarırken, makine öğrenmesi gerçekleştirirken,
web sayfası sıyırma işlemlerinde işimize yarayacak özelliklerden bahsedeceğiz.
Bazı özelliklerin Python 3.8 den sonra geldiğini hatırlatmak isterim.
"""
"""
Metin üzerinde önce basit işlemlerle başlayalım. Bunun için bir metin değişkeni oluşturalım.
"""
metin = 'python String metodları'

basharf = metin.capitalize() #metnin ilk harfi büyük gerisi küçük
print(basharf)

kucukharf = metin.casefold() #bütün harfler küçük
print(kucukharf)

ortala = metin.center(50) #metni söylenen karakter aralığında ortalar, karakter aralığı metinden uzun olmalı
print(ortala)

ortalaekle = metin.center(50,'?') #ortalarken boşluk yerine ? yazsın
print(ortalaekle)

uzunmetin = 'Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik dizgiye de sıçramıştır. 1960larda Lorem Ipsum pasajları da içeren Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştu'
aranan = uzunmetin.count('Lorem') #kelime arama, büyük küçük duyarlı
print(aranan)

aralikta_ara = uzunmetin.count('Lorem', 0, 80)
print(aralikta_ara)
#söylenen karakter aralğında arama ilk değer başlangıç,
#ikincisi bitiş index numaraları

#endswith metnin sonunu ara
metinsonu = "Okula geldi mi?"
son = metinsonu.endswith("?")
print(son) #string in sonu yazılan karakterle bitmiş mi?
son2 = metinsonu.endswith("mi?")
print(son2)
son3 = metinsonu.endswith("?",14,15)
print(son3)

#expandtabs()
str = 'V\to\tl\tk\ta\tn' #karakter arasına \t ile bir tab boşluk (8 karakter) atılıyor

print(str)
print(str.expandtabs(2)) #tab boşluğu 2 karaktere düşürülüyor
print(str.expandtabs(4)) #tab boşluğu 4 karaktere düşürülüyor
print(str.expandtabs(6)) #tab boşluğu 6 karaktere düşürülüyor
print(str.expandtabs(0)) #tab boşluğu yok ediliyor

aranan_metin = 'Volkan geldi mi?'
aranan_index = aranan_metin.find('i')
print(aranan_index) #ilk bulduğu karakterin index numarasını verir
aranan_index = aranan_metin.find('i',1,5)
print(aranan_index) #belirtilen aralıkta aradığı karakterin index numarasını verir
#bulamaz ise -1 döner

#index() metodu da aynı işi yapmıyor mu?
aranan_index = aranan_metin.index('i')
print(aranan_index) #Evet index() metodu da aranan karakterin index numarasını verir
aranan_index=aranan_metin.index('i',1,5)
print(aranan_index) #farklı olarak index() metodu bulamaz ise
#ValueError: substring not found hatasını verir
