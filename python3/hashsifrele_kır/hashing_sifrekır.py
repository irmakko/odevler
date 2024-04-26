import hashlib
def sifre_kirma(filename, wordlist):
    with open(wordlist,"r") as file:
        for a in file:
            sifre = a.strip()
            hashed_sifreleme=hashlib.sha256(sifre.encode()).hexdigest()
            if hashed_sifreleme==filename:
                return sifre
    return None
def main():
    kirilacak_sifre=input("Kırılacak şifreyi girin: ")
    wordlist=input("Kelime listesinin dosya adı: ")
    sifre=sifre_kirma(kirilacak_sifre,wordlist)
    if sifre:
        print(f"Şifre bulundu: {sifre}")
    else:
        print("Şifre kırılmadı..")
if __name__ == "__main__":
    main()
    
    