# json dosyasında şifre olup olmadığını anlama, kaç tane giriş bilgisi kayıtlı söylemek, belirli giriş bilgilerini silmek, setup dosyasının sifre.py girisbilgiler.json yaratmasını falan sağlamak, json dosyasını yaratma,şifre değiştirme komudu eklenecek  hangi sitede olduğunu anlayacak kod eklenecek ingilizce olanı çıkarılacak keylogger kontrol yani şifrelerin çalınmasını engellemek için, uninstall eklemek json dosyasının olduğu yeri bulmak, şifreleri daha güzel gösterecek şekilde {} yerine |- gibi
from pynput import keyboard
import pyperclip #pyperclip'i kütüphaneye ekle
import json
def yazdirJson(data, filename='girisBilgileri.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=1)
with open('girisBilgileri.json') as jsonDosyasi:
    data = json.load(jsonDosyasi)
    temp = data['Giris bilgileri']
girisBilgileri = json.load(open('girisBilgileri.json'))
print('Şifreleri görmek için "sifreler",')
print('Giriş bilgilerini değiştirmek için "degistir",')
print('Şifre eklemek için "ekle",')
print('Şifreleri sıfırlamak için "sifirla",')
print('Önceden kaydedilen giriş bilgilerini kopyalamak için site adını girin')
while True:
    girisBilgileriPrint = json.dumps(girisBilgileri, indent=1)
    print('----------------------------------------------')
    cevap=input('') #Cevap nedir
    if cevap=='sifirla':
        print('Şifrenizi sıfırlamak istediğinize emin misiniz?(e/h)')
        cevap=input('')
        """if cevap=='e':
            girisBilgileriSifirla = {
            Giris bilgileri:[{
            }]}
            print(girisBilgileriPrint)
            input('')"""
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
    if cevap=='degistir':
        print(girisBilgileriPrint)
        print('----------------------------------------------')
        print('Şifreyi mi kullanıcı adını mı değiştirmek istiyorsunuz?(k/s)')
        cevap=input('')
        if cevap=='k':
            print('Hangi uygulamanın kullanıcı adını değiştirmek istersiniz?')
            kullaniciAdiDegistir=input('')
            print("Kullanıcı adınız",girisBilgileri['Giris bilgileri'][0][kullaniciAdiDegistir][0]['kullanici adi'], "emin misiniz?(e/h)")
            cevap=input('')
            if cevap=='e':
                print('Lütfen yeni kullanıcı adınızı girin.')
                cevap=input('')
                print('Başarılı yeni kullanıcı adınız',girisBilgileri['Giris bilgileri'][0][kullaniciAdiDegistir][0]['kullanici adi'])
            if cevap=='h':
                print('İptal edildi.')
        cevap=input('')
    if cevap=='sifreler':
        print(girisBilgileriPrint)
        cevap=input('')
    pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['kullanici adi']) #Kullanıcı ismi kopyalamak
    print('Kullanıcı adı başarıyla kopyalandı') #Kullanıcı ismi kopyalandığını bildirmek
    def on_release(key):
        while True:
            if key == key.delete:
                pyperclip.copy(girisBilgileri['Giris bilgileri'][0][cevap][0]['sifre']) #Şifre kopyalamak
                print('Şifre başarıyla kopyalandı') #Şifre kopyalandığını bildirmek
                return False
                break
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()
