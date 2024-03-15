from tkinter import*
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
def matematik():
    start=int(başlangiç.get())
    finish=int(bitis.get())
    selection=combobox.get()
    if selection=="Faktöriyel Hesaplama":
        sonuc=factorial_hesaplama(start)
    elif selection=="Ortalama Hesaplama":
        sonuc=ortalama_hesaplama(start,finish)
    elif selection=="Ekok Hesaplama":
        sonuc=lcm_ekok(start,finish)
    elif selection=="Ebob Hesaplama":
        sonuc=gcd_ebob(start,finish)
    elif not rakam_mi(start)or not rakam_mi(finish):
        messagebox.showerror("Hata", "Başlangıç ve bitiş değerleri sadece sayı içermelidir.")
    else:
        messagebox.showerror("Hata","Geçersiz seçim")
        return
    messagebox.showinfo("Sonuç",f"SONUÇ: {sonuc}")
#UYARI MESAJ FONKSİYONU
def rakam_mi(text):
    regex=(r"^\d+$",text)
    if re.match(regex,text):
        return True
    else:
        return False
#FAKTÖRİYEL HESAPLAMA
def factorial_hesaplama(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
#ORTALAMA HESAPLAMA
def ortalama_hesaplama(start,finish):
    toplam=sum(range(start,finish+1))
    average=toplam/2
    return average
#EBOB HESAPLAMA
def gcd_ebob(start,finish):
	while finish:
		i=start
		start=finish
		finish=i%finish
	return start
#EKOK HESAPLAMA
def lcm_ekok(start,finish):
    return start*finish/gcd_ebob(start,finish)
#EN AZ 1 DEĞER GİRMEDEN BUTONUN AKTİF OLMAMASI İÇİN
def buton_aktif(event):
    if len(başlangiç.get())>=1:
        combobox.config(state=tk.NORMAL)
    else:
        combobox.config(state=tk.DISABLED)
pencere=tk.Tk()
pencere.title("matematik")
#BAŞLANGIÇ TEXTBOXI
başlangiç=Entry(pencere)
başlangiç.pack()
başlangiç.bind("<KeyRelease>",buton_aktif)
#BİTİŞ TEXTBOXI
bitis=Entry(pencere)
bitis.pack()
#COMBOBOK
combobox=ttk.Combobox(pencere,values=["Faktöriyel Hesaplama","Ortalama Hesaplama","Ekok Hesaplama","Ebob Hesaplama"],state=tk.DISABLED)
combobox.pack()
#HESAPLA BUTTONU
hesapla=Button(pencere,text="HESAPLA",command=matematik)
hesapla.pack()
pencere.mainloop()