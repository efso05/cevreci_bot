import discord
from discord.ext import commands
import random
import os
from aibot import karsilastirma
intents = discord.Intents.default()
intents.message_content = True
ağaç_ekme_sayacı = 0

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
     print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def geri_donusum_nedir(ctx):
    await ctx.send(f"Geri dönüşümün faydalarına geçmeden önce, geri dönüşüm nedir kısaca bu sorunun yanıtı ile başlayalım yazımıza. Geri dönüşüm, kullanılmış ve bir daha kullanılmayacak olan maddelerin tekrar işlenmesi ve tüketici ile yeniden buluşmasına verilen isimdir. Geri dönüşüm maddelerini; plastik şişeler, araba lastikleri, kırık cam parçaları, meral parçalar ve özetle tüm kullanım ömrünü doldurmuş maddeler olarak verebiliriz. Geri dönüşüm, yeniden değerlendirilme imkânı olan atıkların fiziksel ve kimyasal işlemlere tabi tutularak ikinci bir hammaddeye dönüştürülmesi ile sağlanır. Geri dönüşümde amaç, kaynakların aşırı kullanımını önlemektir aslında. Böylelikle çöp miktarı azalır; çevreye fayda sağlamak yolunda ciddi bir adım atmış oluruz.Geri Dönüşümün Önemi Kâğıt, karton, cam, plastik, metal… Bu maddeler, geri dönüşüm işlemi sayesinde sadece doğayı korumakla kalmaz, cebimizi de korur. Ülke ekonomisine de büyük katkı sağlar geri dönüşüm. Bu sayede ithal edilen hurda malzemeye ödenen döviz miktarı azalır ve enerji kullanımı ciddi oranda düşer. Kullanılmış ve işlevini yitirmiş bir kâğıdın, geri dönüşümü hava kirliliği, su kirliliği ve su kullanımı gibi giderleri önemli ölçüde azaltır. Bu arada yapılan araştırmalara göre 1 ton atık kâğıdın kâğıt hamuruna katılması, 7-8 ağacın kesilmesini önler.") 

@bot.command()
async def geri_donusumun_katkıları(ctx):
    await ctx.send(f"Geri dönüşümün faydalarını ekonomik ve çevresel katkılar olarak iki bölüm halinde ele alabiliriz. Peki nedir bu çevresel ve ekonomik faydalar? Gelin birlikte göz atalım.Geri Dönüşümün Ülke Ekonomisine Katkıları;İsrafın önüne geçilir, daha az atık elde etmiş oluruz.Hammadde tüketiminin azalmasını sağlar böylece ekonomiye direkt katkı olur.Enerji tasarrufu sağlar, gereksiz enerji kullanımının önüne geçilmiş olunur.Geri dönüşüm atıkların toplayanlara ekstra ekonomik fayda sağlar böylece yeni bir iş kolu ortaya çıkar, istihdamı artırır, işsizliği azaltır.Başka ülkelerden ithal edilmesi gereken maddelerin azalmasını sağlar böylece ithalat masraflarını önemli ölçüde düşürür.Geri Dönüşümün Çevreye Katkıları;Geri dönüşüm sayesinde ağaçlar, mineraller ve su kaynakları korunur. Böylece aslında tüm bu “kirlilik kaynakları”na yeni bir sayfa açılmış olur; bembeyaz ve kirden arınmış bir sayfa…Tüketim malzemesi üretimi için yeni hammadde arayışına gerek kalmaz, böylece hem hava hem çevre kirliliğinin önüne geçilmiş olur.Sera gazı emisyonunun düşmesine neden olarak küresel ısınma konusunda önemli bir katkı sağlar.İnsan sağlığına zarar verecek çöp atıklara engel olunur böylece doğaya destek çıkarak sağlığımıza da katkı sağlamış oluruz.")

@bot.command()
async def neyi_geri_donusturabilirim(ctx):
    await ctx.send(f"Tabi birçoğumuzun aklında neleri geri dönüşüm ile yeniden kullanabileceğimiz sorusu oluyor. Bildiklerimiz kâğıt, metal, cam peki ya bilmediklerimiz? Geri dönüşümü olan ürünlerden birkaçını şu şekilde sayabiliriz; alüminyum, bakır, demir, beton, plastik, piller, motor yağı, akümülatörler, organik atıklar, tekstil ürünleri, ahşap birtakım ürünler, bazı elektronik aletler…")    

@bot.command()
async def küresel_ısınma_nedir(ctx):
    await ctx.send(f"Küresel ısınma, atmosferdeki sera gazlarının birikimi sonucu dünya yüzeyindeki ortalama sıcaklıkların artması olarak tanımlanabilir. Bu artışın temel nedeni ise insan faaliyetlerinin sonucunda ortaya çıkan sera gazı emisyonlarıdır. Fosil yakıtların kullanımı, sanayi üretimi, ormansızlaşma ve tarım faaliyetleri gibi faktörler, atmosfere sera gazları salınımını artırmaktadır.")

@bot.command()
async def atıklar_ne_kadar_surede_yok_olur(ctx):
    await ctx.send(f"""Strafor 5000 yıl - 2 Milyon yıl
                    Cam Şişe 4000 yıl,Plastik 1000 yıl
                    Poliüretan (Sentetik fiberler, yapıştırıcılar, halıların alt kısmı ve sert plastik contalar) 1000 yıl
                    Telefon Kartı 1000 yıl
                    Kaset 100 yıl - 1000 yıl
                    Su Boruları 1000 yıl
                    Balık Oltası 600 yıl
                    Bebek Bezi 550 yıl
                    Plastik Tabak 500 yıl
                    Pet Şişe 400 yıl
                    Deterjan 400 yıl
                    Pil 300 yıl
                    Alüminyum 100 yıl
                    Çakmak 100 yıl
                    Tahta Parçaları 15 yıl
                    Kutu Kola 10 yıl
                    Çiklet 5 yıl - 25 yıl
                    Boyalı Tahta 13 yıl
                    Yün Çorap 4 yıl
                    Kontrplak 1-3 yıl
                    Sigara İzmariti 1 yıl - 2 yıl
                    Yün 1 yıl - 2 yıl
                    İp Parçaları 3 ay - 14 ay
                    Bez Parçası 6 ay
                    Pamuklu Kumaş 1 ay - 5 ay
                    Meyve Artıkları 3 ay - 6 ay
                    Gazete 3 ay
                    Karton Süt Kutusu 3 ay
                    Elma Çöpü 2 ay
                    Kağıt Havlu 1 ay
                    Mendil 2-4 hafta""")



@bot.command()
async def bay(ctx):
    await ctx.send(f'görüşmek üzere:(')

@bot.command()
async def nereyi_temizliyim(ctx):
    yer = ["Sahil","Bahçe","Sokak"]
    await ctx.send(random.choice(yer))  

@bot.command()
async def atigimi_napiyim(ctx):
    await ctx.send(f"""Öğrenmek istediğiniz atık 
                   türünü aşağıdaki komutları
                   kullanarak seçin
                   metaller için:!metal
                   plastikler için:!plastik
                   camlar için:!cam
                   kağıtlar için:!kagıt
                   piller için:!pil
                   organik atılklar için:!organik""")

@bot.command()
async def metal(ctx):
    await ctx.send(f"""Metalleri geri dönüştürmek için 
               onları geri dönüşüm kutularına atmak gerekir.
               Fakat onları atmayıp kendimizde geri dönüştürebiliriz.
               Mesela konserve kutularından saksı yapabilirsin.""")
    image = os.listdir('metal')
    metall = random.choice(image)
    with open(f'metal/{metall}', 'rb') as f:
            picture = discord.File(f) 
    await ctx.send(file=picture)     
@bot.command()
async def plastik(ctx):
    await ctx.send(f"""Plastikleri geri dönüştürmek için 
               onları geri dönüşüm kutularına atmak gerekir.
               Fakat onları atmayıp kendimizde geri dönüştürebiliriz.
               Mesela plastik pet şişelerden saksı yapabiliriz.""")
    image2 = os.listdir('plastik')
    plastikk = random.choice(image2)
    with open(f'plastik/{plastikk}', 'rb') as f:
            picture = discord.File(f) 
    await ctx.send(file=picture)
@bot.command()
async def cam(ctx):
    await ctx.send(f"""Camları geri dönüştürmek için 
               onları geri dönüşüm kutularına atmak gerekir.
               Fakat onları atmayıp kendimizde geri dönüştürebiliriz.
               Mesela kapağı olmayan kavanozlar ile süs yapabiliriz.""")
    image3 = os.listdir('cam')
    camm = random.choice(image3)
    with open(f'cam/{camm}', 'rb') as f:
            picture = discord.File(f) 
    await ctx.send(file=picture)
@bot.command()
async def kagıt(ctx):
    await ctx.send(f"""Kağıtları geri dönüştürmek için 
               onları geri dönüşüm kutularına atmak gerekir.
               Fakat onları atmayıp kendimizde geri dönüştürebiliriz.
               Mesela bir tarafı kullanılmış kağıtları yazıcımız varsa onun
               için kullanabiliriz.""")
    image4 = os.listdir('kagıt')
    kagitt = random.choice(image4)
    with open(f'kagıt/{kagitt}', 'rb') as f:
            picture = discord.File(f) 
    await ctx.send(file=picture)
@bot.command()
async def pil(ctx):
    await ctx.send(f"""Pilleri geri dönüştürmek için 
               onları piller için özel olan geri
               dönüşüm kutularına atmak gerekir.""")
    image5 = os.listdir('pil')
    pill = random.choice(image5)
    with open(f'pil/{pill}', 'rb') as f:
            picture = discord.File(f) 
    await ctx.send(file=picture)
@bot.command()
async def organik(ctx):
    await ctx.send(f"""Organik atıklar geri dönüştürülemez.
               Onları çöpe atmamız gerekir.""")
    image6 = os.listdir('organik')
    organikk = random.choice(image6)
    with open(f'organik/{organikk}', 'rb') as f:
            picture = discord.File(f) 
    await ctx.send(file=picture)

@bot.command(name='ağaç_ektim')
async def ağaç_ek(ctx):
    global ağaç_ekme_sayacı
    
    ağaç_ekme_sayacı += 1
    print("Ekilen ağaç sayısı",ağaç_ekme_sayacı)
    await ctx.send('Ağaç ektiğiniz için teşekkürler')
    if ağaç_ekme_sayacı == 1000000:
        await ctx.send('Tebrikler! 1.000.000 tane ağaç ekme hedefini tamamladık!')
        ağaç_ekme_sayacı = 0

@bot.command()                  
async def algıla(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            file_url = attachments.url
            file_path = f"resim/{file_name}"
            await attachments.save(file_path)
            await ctx.send("resim bulundu ve kaydedildi.")
            sonuc = karsilastirma(file_path)
            await ctx.send("resim"+sonuc[0])

    else:
        await ctx.send("resim bulunamadı.")

bot.run("")    
