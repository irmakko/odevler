def asalmi(sayi):
    if sayi<2:
        return False
    for i in range(2,sayi):
        if sayi%i==0:
            return False
    return True
def bolenler(sayi):
    bolenleri=[i for i in range(1,sayi+1)if sayi%i==0]
    return bolenleri
def main():
    try:
        girilensayi=int(input("Sayiyi Girin: "))
        bolenleri=bolenler(girilensayi)
        print(f"{girilensayi}'nin bolenleri: {bolenleri}")
        asalbolen=[bolen for bolen in bolenleri if asalmi(bolen)]
        print(f"{girilensayi}'nin asal bölenleri: {asalbolen}")
    except ValueError:
        print("Lütfen gecerli bir sayi girin!")
if __name__=="__main__":
    main()
