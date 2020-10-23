#Web Kazıma - Web Scraping
import requests
from bs4 import BeautifulSoup
import time

def urunKontrolEt():
    URL = 'https://www.amazon.com.tr/Lenovo-IdeaPad-Bilgisayar%C4%B1-i5-10300H-81Y400N1TX/dp/B08CYG8WXZ/ref=sr_1_6?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=lenovo&qid=1603458275&sr=8-6'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    sayfa = requests.get(URL, headers = headers)
    icerik = BeautifulSoup(sayfa.content,'html.parser')
    #print(icerik)
    #productTitle
    urunAdi = icerik.find(id='productTitle').get_text().strip()
    #print(urunAdi)
    #priceblock_ourprice
    ucreti = icerik.find(id='priceblock_ourprice').get_text()
    ucretDonusturen = int(ucreti[1:6].replace('.',''))
    #print(ucretDonusturen)

    if(ucretDonusturen < 8000):
        print(f"{ucretDonusturen} TL {urunAdi} fiyatı düştü acele et!!!")
    else:
        print(f"{ucretDonusturen} TL {urunAdi} henüz düşmedi")

while(True):
    urunKontrolEt()
    time.sleep(3)