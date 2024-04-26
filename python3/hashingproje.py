import hashlib
import time
from itertools import product
def sifre_metni(text):#SHA-256 YÖNTEMİYLE ŞİFRELER
    sifreli_metin = hashlib.sha256(text.encode()).hexdigest()
    return sifreli_metin
def kirlan_sifre(sifreli_metin):#BRUTE-FORCE YÖNTEMİYLE ŞİFREYİ KIRMAYA ÇALIŞIR
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    max_char_uzunluk=8 #MAKSİMUM KARAKTER UZUNLUĞU
    for char_uzunluk in range(1,max_char_uzunluk+1):#Şifrenin uzunluğunu artırarak 1 le max_char_uzunluk arasındaki tüm charları denemek için döngü oluşturur.
        for sifre in product(chars,repeat=char_uzunluk):#product kullanaarak konbinasyonları oluşturur.
            sifre=''.join(sifre)#konbinasyonları birleştirerek şifre metni oluşturur
            hashed_sifreleme = hashlib.sha256(sifre.encode()).hexdigest()
            if hashed_sifreleme == sifreli_metin:#kendi şifrelediği metinle hedefteki şifrelenmiş metinle karşılaştırır.
                return sifre#eşleşme bulunursa doğru şifre bulunur.
    return None
def main():#ANA İŞLEMLER VE TİME 
    text = input("Şifre girin: ")
    baslangic_zamani = time.time()
    sifreli_metin = sifre_metni(text)
    print(f"Şifre: {sifreli_metin}")
    sifre = kirlan_sifre(sifreli_metin)
    if sifre:
        print(f"Şifre kırıldı: {sifre}")
    else:
        print("Şifre kırılamadı..")
    bitis_zamani = time.time()
    gecen_sure = bitis_zamani - baslangic_zamani
    print(f"Geçen süre: {gecen_sure} saniye")
if __name__ == "__main__":
    main()
