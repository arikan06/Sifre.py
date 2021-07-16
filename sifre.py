# kaç tane giriş bilgisi kayıtlı söylemek, belirli giriş bilgilerini silmek, setup dosyasının sifre.py girisbilgiler.json yaratmasını falan sağlamak, json dosyasını yaratma,şifre değiştirme komudu eklenecek  hangi sitede olduğunu anlayacak kod eklenecek ingilizce olanı çıkarılacak keylogger kontrol yani şifrelerin çalınmasını engellemek için, uninstall eklemek json dosyasının olduğu yeri bulmak, şifreleri daha güzel gösterecek şekilde {} yerine |- gibi try eklicem
import json
try:
    from pynput import keyboard
    import pyperclip #pyperclip'i kütüphaneye ekle
except ModuleNotFoundError:
    print('pyperclip ve pynput modülü bulunamadı.')
    print('pyperclip ve pynput modülü kütüphaneye ekleniyor...')
    import pip3
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

print('Şifreleri görmek için "sifreler",')
print('Giriş bilgilerini değiştirmek için "degistir",')
print('Şifre eklemek için "ekle",')
print('Şifreleri sıfırlamak için "sifirla",')
print('Belirli giriş bilgilerini simek için "sil",')
print('Önceden kaydedilen giriş bilgilerini kopyalamak için site adını girin')
while True:
    try:
        print('----------------------------------------------')
        cevap=input('') #Cevap nedir
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
            cevap=input('')
            if cevap=='e':
                girisBilgileriEkle = {
                siteEkle:[{
                "e-posta": epostaEkle,
                "kullanici adi":kullaniciAdiEkle,
                "sifre": sifreEkle
                }]}
                ekle.append(girisBilgileriEkle)
                print('Başarı. "Sifreler" yazarak kayıtlı şifreleri görebilirsiniz.')

        if cevap=='degistir':
            #girisBilgileriPrint = json.dumps(girisBilgileri, indent=1)
            #print(girisBilgileriPrint)
            print('----------------------------------------------')
            print('Hangi sitenin bilgilerini değiştirmek istersiniz?')
            siteDegistir=input('')
            print('Değiştirmek istediğiniz bilgiyi yazın.')
            girisBilgileriDegistir=input('')
            print(girisBilgileriDegistir,' değişkenini ne yapmak istersiniz?')
            girisBilgileriDegisgeniDegistir=input('')
            if girisBilgileriDegistir=='kullanici adi':
                print('Eski kullanıcı adınız:',girisBilgileri['Giris bilgileri'][0][siteDegistir][0][girisBilgileriDegistir], ' yeni şifreniz:' ,girisBilgileriDegisgeniDegistir, 'emin misiniz?(e/h)')
                cevap=input('')
                if cevap=='e':
                    print('Kullanıcı adınız başarıyla değiştirilmiştir')
                    input('')
                if cevap=='h':
                    print('İptal edildi.')
                    cevap=input('')
            if girisBilgileriDegistir=='sifre':
                print('Eski şifreniz:',girisBilgileri['Giris bilgileri'][0][siteDegistir][0]['sifre'], ' yeni şifreniz:' ,girisBilgileriDegisgeniDegistir, 'emin misiniz?(e/h)')
                cevap=input('')
                if cevap=='e':
                    print('Şifreniz başarıyla değiştirilmiştir')
                    input('')
                if cevap=='h':
                    print('İptal edildi.')
                    cevap=input('')

        if cevap=='sifreler':
            girisBilgileriPrint = json.dumps(girisBilgileri, indent=1)
            print(girisBilgileriPrint)

    except Exception as e:
        print(e,'programda bulunmamaktadır.')
    try:
        pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['kullanici adi'])
        print('Kullanıcı adı başarıyla kopyalandı')
        def on_release(key):
            if key == key.delete:
                pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['sifre'])
                print('Şifre başarıyla kopyalandı')
                return False
        with keyboard.Listener(on_release=on_release) as listener:
            listener.join()
    except AttributeError as e:
        print('delete tuşuna basman lazım kardeşim')
    except Exception as e:
        pass
