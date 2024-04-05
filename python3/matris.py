import random
def rastgele_matris():
    matris=[]
    for i in range(10):
        satir=[]
        for j in range(10):
            sayi=random.randint(0,10)
            satir.append(sayi)
        matris.append(satir)
    return matris
def matris_carpim(matris_a,matris_b):
    sonuc= [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                sonuc[i][j]+=matris_a[i][k]*matris_b[k][j]
    return sonuc
matris_a=rastgele_matris()
matris_b=rastgele_matris()
print("A:")
for satir in matris_a:
    print(satir)
print("\nB:")
for satir in matris_b:
    print(satir)
sonuc=matris_carpim(matris_a,matris_b)
print("\nSonuc:")
for satir in sonuc:
    print(satir)