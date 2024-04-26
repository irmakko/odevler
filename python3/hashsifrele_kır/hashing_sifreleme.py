import hashlib
def sifre_metni(text):
    sifreli_metin=hashlib.sha256(text.encode()).hexdigest()
    return sifreli_metin
def main():
    text=input("Şifrelenecek metin: ")
    sifreli_metin=sifre_metni(text)
    print(f"Şİfre: {sifreli_metin}")
if __name__=="__main__":
    main()