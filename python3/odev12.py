import tkinter as tk
from tkinter import messagebox
import random
sayi=[random.randint(1,100) for _ in range(10)]
messagebox.showinfo("Sayilar","Bulunan 10 adet sayi: "+",".join(map(str,sayi)))
minimum_sayi=min(sayi)
messagebox.showinfo("Minumum Sayi",f"Minimum: {minimum_sayi}")
maximum_sayi=max(sayi)
messagebox.showinfo("Maximum Sayi",f"Maximum: {maximum_sayi}")
def asal_sayilar(asal):
    if asal<2:
        return False
    for i in range(2,int(asal**0.5)+1):
        if asal%i==0:
            return False
    return True
ortalama=sum(sayi)/len(sayi)
sayilar=[asal for asal in sayi if asal_sayilar(asal)]
messagebox.showinfo("Ortalama ve Asallar",f"Ortalama: {ortalama}\nAsalları:{','.join(map(str,sayilar))}")