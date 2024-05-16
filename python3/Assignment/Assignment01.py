def sirali_liste(liste):
    return sorted(liste)
girilen_liste=input("Input: ")
sayilar=[int(sayi) for sayi in girilen_liste.split()]
output=sirali_liste(sayilar)
print("Output:",end=" ")
for sayi in output:
    print(sayi,end=" ")