#pip install nltk
from nltk.chat.util import Chat, reflections

ciftler = [
    ["Benim adım (.*)", ["Merhaba %1, nasılsın?"]],
    ['(merhaba|selam|selamünaleyküm|hey)',['merhaba, nasılsın',
                                           'Aleykümselam','Heyy nasıl '
                                                          'gidiyor']],
    ['(.*) hava çok (.*)',['%1 hava %2, bence keyfini çıkarmaya bak']],
    ['En güzel şehir (.*)',['Sana katılıyorum, %1 nin yemekleri de '
                            'güzeldir.', '%1 nın doğası da güzeldir', '%1 in '
                                                                      'insanları da şahanedir' ]],
    ['Yaşın kaç?',['Yaşım yok ama 2021 yılında ütretildim']],
    ['(.*)(memleket|nerelisin|hangi şehir|hangi ülke)',['Ankara, Türkiye']],
    ['Behiç',['He benim buyur gardaş!','Çelebi yi unutma']]

]
yansimalar={
    'merhaba': 'merhaba, nasılsın',
    'gittim':'gittin',
    'Selamünaleyküm':'Aleykümselam'
}

chat = Chat(ciftler, yansimalar)
chat.converse(quit='bitti')
#print(chat._substitute("merhaba"))
#print(reflections)