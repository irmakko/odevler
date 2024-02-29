import random 
def rastgelesayi_toplami():
    try:
        sayiadedi=int(input("kac adet rastgele sayi olusturmak istersiniz? "))
        rastgele_sayi=[random.randint(1,100)for _ in range(sayiadedi)]
        toplam=sum(rastgele_sayi)
        with open("dosya5.txt","w")as dosya:
            dosya.write("Rastgele sayilar: {}\n".format(rastgele_sayi))
            dosya.write("Toplam: {}".format(toplam))
        with open("dosya5.txt","r")as dosya:
            ici=dosya.read()
            print("dosyanin ici:\n",ici)
    except ValueError:
        print("gecerli bir sayi girin!")
rastgelesayi_toplami()