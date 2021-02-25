# şifre değiştirme komudu eklenecek  hangi sitede olduğunu anlayacak kod eklenecek ingilizce olanı çıkarılacak keylogger kontrol yani şifrelerin çalınmasını engellemek için, uninstall eklemek json dosyasının olduğu yeri bulmak, şifreleri daha güzel gösterecek şekilde {} yerine |- gibi
from pynput import keyboard
import pyperclip #pyperclip'i kütüphaneye ekle
import json
girisBilgileri = json.load(open('girisBilgileri.json'))
girisBilgileriPrint = json.dumps(girisBilgileri, indent=1)
print('Şifreleri görmek için "sifreler",')
print('Giriş bilgilerini değiştirmek için "degistir",')
print('----------------------------------------------')
while True:
    cevap=input('') #Cevap nedir
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
