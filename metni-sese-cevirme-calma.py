#Yazıyı Sese Çevirme ve Seslendirme Uygulaması
from gtts import gTTS
import os
from os import path
masaladi = "tarlafaresi"

def dosyaVarmi(dosya):
    return path.exists(dosya)


dosya = open(f"{masaladi}.txt", encoding="utf-8")
yazi = dosya.read()
cikti = gTTS(text=yazi, lang='tr',slow=False)
if dosyaVarmi(f"{masaladi}.mp3"):
    print("Seslendiriliyor...")
    os.system(f"{masaladi}.mp3")
else:
    print("Dosyanız oluşturuluyor")
    cikti.save(f"{masaladi}.mp3")
    print("Seslendiriliyor...")
    os.system(f"{masaladi}.mp3")
dosya.close()



