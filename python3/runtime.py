import time

#baslangic_zamani=time.time()
def saniye_cevirme():
    return round(time.time() * 1000)
baslangic_zamani=saniye_cevirme()
#Tekrar eden elemanları ve tekrar etmeyen elemanları hesaplama
def tekrar_edenleri_bul(dizi):
    tekrar_edenler=[]
    duzenlenmis_dizi=[]
    for eleman in dizi:
        if eleman not in duzenlenmis_dizi:
            duzenlenmis_dizi.append(eleman)
        elif eleman not in tekrar_edenler:
            tekrar_edenler.append(eleman)
    return tekrar_edenler,duzenlenmis_dizi
#BİRİNCİ SET BÜYÜKTEN KÜÇÜĞE SIRALAMA
def birinciset_buyuk(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for a in range(0,uzunluk-i-1):
            if dizi[a]<dizi[a+1]:#Küçüktenmi yada büyüktenmi sırılanacığını ayarlayan satır
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
liste_iki= [15,9,8,11,9,5,3,-1,20,30]
sirali_liste= birinciset_buyuk(liste_iki)
print(f"Birinci Set: Büyükten küçüğe = {sirali_liste}")
bitis_zamani=saniye_cevirme()
gecen_sure=bitis_zamani-baslangic_zamani/1000
print(f"Runtime:{gecen_sure} saniye")

#BİRİNCİ SET KÜÇÜKTEN BÜYÜĞE SIRALAMA
baslangic_zamani=saniye_cevirme()
def birinciset_kuçuk(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for a in range(0,uzunluk-i-1):
            if dizi[a]>dizi[a+1]:
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
liste_bir=[15,9,8,11,9,5,3,-1,20,30]
siralanmis_liste=birinciset_kuçuk(liste_bir)
print(f"Birinci Set: Küçükten büyüğe = {siralanmis_liste}")
bitis_zamani=saniye_cevirme()
gecen_sure=bitis_zamani-baslangic_zamani/1000
print(f"Runtime:{gecen_sure} saniye")
tekrar_edenler, duzenlenmis_dizi = tekrar_edenleri_bul(liste_bir)
print("Tekrar eden elemanlar:", tekrar_edenler)
print("Düzenlenmiş dizi:", duzenlenmis_dizi,"\n")

#İKİNCİ SET BÜYÜKTEN KÜÇÜĞE SIRALAMA
#baslangic_zamani=time.time()
baslangic_zamani=saniye_cevirme()
def ikinciset_buyuk(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for a in range(0,uzunluk-i-1):
            if dizi[a]<dizi[a+1]:
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
liste_iki = [1,7,-1,-7,0,9]
sirali_liste= ikinciset_buyuk(liste_iki)
print(f"İkinci Set: Büyükten küçüğe = {sirali_liste}")
bitis_zamani=saniye_cevirme()
gecen_sure=bitis_zamani-baslangic_zamani/1000
print(f"Runtime:{gecen_sure} saniye")

#İKİNCİ SET KÜÇÜKTEN BÜYÜĞE SIRALAMA
baslangic_zamani=saniye_cevirme()
def ikinciset_kuçuk(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for a in range(0,uzunluk-i-1):
            if dizi[a]>dizi[a+1]:# Sadece bu satırı değiştirdik
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
liste_bir=[1,7,-1,-7,0,9]
siralanmis_liste=ikinciset_kuçuk(liste_bir)
print(f"İkinci Set: Küçükten büyüğe = {siralanmis_liste}")
bitis_zamani=saniye_cevirme()
gecen_sure=bitis_zamani-baslangic_zamani/1000
print(f"Runtime:{gecen_sure} saniye")
tekrar_edenler, duzenlenmis_dizi = tekrar_edenleri_bul(liste_bir)
print("Tekrar eden elemanlar:", tekrar_edenler)
print("Düzenlenmiş dizi:", duzenlenmis_dizi,"\n")

#ÜÇÜNCÜ SET BÜYÜKTEN KÜÇÜĞE SIRALAMA
#baslangic_zamani=time.time()
baslangic_zamani=saniye_cevirme()
def ucuncuset_buyuk(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for a in range(0,uzunluk-i-1):
            if dizi[a]<dizi[a+1]:
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
liste_iki = [2,4,6,5,4,3]
sirali_liste= ikinciset_buyuk(liste_iki)
print(f"Üçüncü Set: Büyükten küçüğe = {sirali_liste}")
bitis_zamani=saniye_cevirme()
gecen_sure=bitis_zamani-baslangic_zamani/1000
print(f"Runtime:{gecen_sure} saniye")

#ÜÇÜNCÜ SET KÜÇÜKTEN BÜYÜĞE SIRALAMA
baslangic_zamani=saniye_cevirme()
def ucuncuset_kuçuk(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for a in range(0,uzunluk-i-1):
            if dizi[a]>dizi[a+1]:# Sadece bu satırı değiştirdik
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
liste_bir=[2,4,6,5,4,3]
siralanmis_liste=ikinciset_kuçuk(liste_bir)
print(f"Üçüncü Set: Küçükten büyüğe = {siralanmis_liste}")
bitis_zamani=saniye_cevirme()
gecen_sure=bitis_zamani-baslangic_zamani/1000
print(f"Runtime:{gecen_sure} saniye")
tekrar_edenler, duzenlenmis_dizi = tekrar_edenleri_bul(liste_bir)
print("Tekrar eden elemanlar:", tekrar_edenler)
print("Düzenlenmiş dizi:", duzenlenmis_dizi)
