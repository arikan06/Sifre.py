# kaç tane giriş bilgisi kayıtlı söylemek, belirli giriş bilgilerini silmek, setup dosyasının sifre.py girisbilgiler.json yaratmasını falan sağlamak, json dosyasını yaratma,şifre değiştirme komudu eklenecek  hangi sitede olduğunu anlayacak kod eklenecek ingilizce olanı çıkarılacak keylogger kontrol yani şifrelerin çalınmasını engellemek için, uninstall eklemek json dosyasının olduğu yeri bulmak, şifreleri daha güzel gösterecek şekilde {} yerine |- gibi try eklicem
import json
import random
import time
try:
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    import pyperclip #pyperclip'i kütüphaneye ekle
except ModuleNotFoundError:
    print('pyperclip ve pynput modülü bulunamadı.')
    print('pyperclip ve pynput modülü kütüphaneye ekleniyor...')
    import pip
    pip.main(['install','pynput', 'pyperclip']) #Asıl komut
    input('')
    pass
try:
    girisBilgileri = json.load(open('girisBilgileri.json'))
except FileNotFoundError:
    print('girisBilgileri.json bulunamadı, girisBilgileri.json yaratılıyor..')
    with open('girisBilgileri.json','w') as f:
        girisBilgileriSifirla = {
         "Giris bilgileri": [

        ]}
        json.dump(girisBilgileriSifirla, f, indent=1)
        print("girisBilgileri.json yaratıldı")
        print('----------------------------------------------')
        pass
except Exception as e:
    print(e)
    input('')
finally:
    girisBilgileri = json.load(open('girisBilgileri.json'))
    ekle = girisBilgileri['Giris bilgileri']

def ingilizce(ingilizcelestir):
    ingilizcelestir = ingilizcelestir.replace("İ", "i")
    ingilizcelestir = ingilizcelestir.lower()
    ingilizcelestir = ingilizcelestir.replace("ı", "i")
    ingilizcelestir = ingilizcelestir.replace("ş", "s")
    ingilizcelestir = ingilizcelestir.replace("ç", "c")
    ingilizcelestir = ingilizcelestir.replace("ğ", "g")
    ingilizcelestir = ingilizcelestir.replace("ö", "o")
    ingilizcelestir = ingilizcelestir.replace("ü", "u")
    return ingilizcelestir

print('Şifreleri görmek için ".sifreler",')
print('Giriş bilgilerini değiştirmek için ".degistir",')
print('Şifre eklemek için ".ekle",')
print('Şifreleri sıfırlamak için ".sifirla",')
print('Belirli giriş bilgilerini simek için ".sil",')
print('Önceden kaydedilen giriş bilgilerini kopyalamak için site adını girin')
while True:
    try:
        print('----------------------------------------------')
        cevap=ingilizce(input(''))
        if cevap.startswith('.'):
            cevap=cevap.replace('.', '')
            if cevap=='sifirla':
                with open('girisBilgileri.json','w') as f:
                    girisBilgileriSifirla = {
                     "Giris bilgileri": [

                    ]}
                    json.dump(girisBilgileriSifirla, f, indent=1)
                    print("girisBilgileri.json sıfırlandı")

            if cevap=='ekle':
                siteEkle=input('Hangi sitenin giriş bilgisini kaydetmek istersiniz? ')
                epostaEkle=input('E-posta giriniz? ')
                kullaniciAdiEkle=input('Kullanıcı adı giriniz? ')
                sifreEkle=input('Şifre giriniz? ')
                print('Site:',siteEkle, 'e-posta:',epostaEkle, 'Sifre:',sifreEkle, 'eklemek istediğinize emin misiniz?(e/h)')
                cevap=input()
                if cevap=='e':
                    girisBilgileriEkle = {
                    siteEkle:[{
                    "e-posta": epostaEkle,
                    "kullanici adi":kullaniciAdiEkle,
                    "sifre": sifreEkle
                    }]}
                    ekle.append(girisBilgileriEkle)
                    print('Başarı. "Sifreler" yazarak kayıtlı şifreleri görebilirsiniz.')

            if cevap=='sifreler':
                girisBilgileriPrint = json.dumps(girisBilgileri, indent=1)
                print(girisBilgileriPrint)
        else:
            #print('1')
            #pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['kullanici adi'])
            #print('1')
            #keyboard.press(Key.alt_l)
            #keyboard.release(Key.alt_l)
            #keyboard.press(Key.tab)
            #keyboard.release(Key.tab)
            time.sleep(2)
            kullaniciAdi=str(girisBilgileri['Giris bilgileri'][0][cevap][0]['kullanici adi'])
            keyboard.type(kullaniciAdi)
            #keyboard.type(girisBilgileri['Giris bilgileri'][0][cevap][0]['sifre'])
            #keyboard.press(Key.enter)
    except Exception as e:
        print(e)
        me=input('')
        if me=='e':
            pass
