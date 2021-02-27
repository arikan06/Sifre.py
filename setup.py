import json
import pip
print('Python kütüphanenize Pynput ve Pyperclip ekleniyor..')
pip.main(['install','pynput', 'pyperclip']) #Asıl komut
print('Eğer şifre kaydettiyseniz bütün şifreleriniz silinecek emin misiniz?(e/h)')
cevap=input('')
if cevap=='e':
    with open('girisBilgileri.json', 'w') as f:
    print("json dosyası yaratıldı")
    input('')
