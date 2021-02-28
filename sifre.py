# json dosyasında şifre olup olmadığını anlama, kaç tane giriş bilgisi kayıtlı söylemek, belirli giriş bilgilerini silmek, setup dosyasının sifre.py girisbilgiler.json yaratmasını falan sağlamak, json dosyasını yaratma,şifre değiştirme komudu eklenecek  hangi sitede olduğunu anlayacak kod eklenecek ingilizce olanı çıkarılacak keylogger kontrol yani şifrelerin çalınmasını engellemek için, uninstall eklemek json dosyasının olduğu yeri bulmak, şifreleri daha güzel gösterecek şekilde {} yerine |- gibi try eklicem
try:
    import json
except Exception as e:
    print('Json modülünde bir sorun çıktı')
    print('----------------------------------------------')
    print('hata kodu: ',e)
try:
    from pynput import keyboard
    import pyperclip #pyperclip'i kütüphaneye ekle
except ModuleNotFoundError:
    print('pyperclip ve pynput modülü bulunamadı.')
    print('pyperclip ve pynput modülü kütüphaneye ekleniyor...')
    import pip3
    pip.main(['install','pynput', 'pyperclip']) #Asıl komut
    input('')
try:
    def yazdirJson(data, filename='girisBilgileri.json'):
        with open(filename,'w') as f:
            json.dump(data, f, indent=1)
    with open('girisBilgileri.json') as jsonDosyasi:
        data = json.load(jsonDosyasi)
        temp = data['Giris bilgileri']
    girisBilgileri = json.load(open('girisBilgileri.json'))
except FileNotFoundError:
    print('girisBilgileri.json bulunamadı')
    input('')
print('Şifreleri görmek için "sifreler",')
print('Giriş bilgilerini değiştirmek için "degistir",')
print('Şifre eklemek için "ekle",')
print('Şifreleri sıfırlamak için "sifirla",')
print('Önceden kaydedilen giriş bilgilerini kopyalamak için site adını girin')
while True:
    try:
        print('----------------------------------------------')
        cevap=input('') #Cevap nedir
        if cevap=='sifirla':
            print('Şifre sıfırlanmıştir')
            cevap=input('')
        if cevap=='ekle':
            print('Hangi sitenin giriş bilgisini kaydetmek istersiniz')
            siteEkle=input('')
            print('e-posta giriniz')
            epostaEkle=input('')
            print('kullanıcı adı giriniz')
            kullaniciAdiEkle=input('')
            print('sifre giriniz')
            sifreEkle=input('')
            print('Site:',siteEkle, 'e-posta:',epostaEkle, 'Sifre:',sifreEkle, 'eklemek istediğinize emin misiniz?(e/h)')
            cevap=input('')
            if cevap=='e':
                girisBilgileriEkle = {
                siteEkle:[{
                "e-posta": epostaEkle,
                "kullanici adi":kullaniciAdiEkle,
                "sifre": sifreEkle
                }]}
                temp.append(girisBilgileriEkle)
                yazdirJson(data)
                cevap=input('')
        if cevap=='degistir':
            girisBilgileriPrint = json.dumps(girisBilgileri, indent=1)
            print(girisBilgileriPrint)
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
            cevap=input('')
    except Exception as e:
        print(e,'programda bulunmamaktadır.')
    try:
        pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['kullanici adi']) #Kullanıcı ismi kopyalamak
        print('Kullanıcı adı başarıyla kopyalandı') #Kullanıcı ismi kopyalandığını bildirmek
        def on_release(key):
            if key == key.delete:
                pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['sifre']) #Şifre kopyalamak
                print('Şifre başarıyla kopyalandı') #Şifre kopyalandığını bildirmek
                return False
        with keyboard.Listener(on_release=on_release) as listener:
            listener.join()
    except AttributeError as e:
        print('delete tuşuna basman lazım kardeşim')
    except Exception as e:
        print('Bu site ismi programda bulunamadı lütfen "ekle" komudunu kullanarak programa ekleyin. Programda kayıtlı olan programları görmek için "sifreler" yazın')
