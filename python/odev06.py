def ucgen(uzunluk):
    for i in range(1,uzunluk + 1):
        print("*" * i)

uzunluk = int(input("Üçgenin uzunlugunu girin: "))
ucgen(uzunluk)


def ucgen(uzunluk,karakter):
    if(karakter==" "):
        print("boşluk karakteri girmeyiniz!")
        return
    for i in range(1,uzunluk + 1):
        print(karakter * i)
        
karakter=str(input("karakter veriniz: "))
uzunluk = int(input("Üçgenin uzunlugunu girin: "))
ucgen(uzunluk,karakter)

