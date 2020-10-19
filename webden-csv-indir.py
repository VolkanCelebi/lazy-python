#Web den CVS dosya indirip kaydetmek
from urllib import request
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/zillow.csv'
response = request.urlopen(url)
csv = response.read()

satirlar = csv.decode().split('\n')
kaynak = 'yenidosya.csv'
dosya = open(kaynak,'w')

for satir in satirlar:
    print(satir)
    dosya.write(satir+'\n')
dosya.close()
