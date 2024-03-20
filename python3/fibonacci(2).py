import tkinter as tk
from tkinter import*
from tkinter import messagebox
def fibonacci():
    try:
        n=int(basamak.get())
        if n<0:
            messagebox.showerror("HATA","NEGATİF SAYI GİRMEYİNİZ!!!")
            return
    except ValueError:
        messagebox.showerror("HATA","LÜTFEN SADECE SAYI GİRİNİZ!!!")
        return
    a,b=1,1
    sayi=2
    while True:
        a,b=b,a+b
        sayi+=1
        if len(str(b))>=n:
            messagebox.showinfo("SONUC",f"{sayi}. Fibonacci sayısı{n} basamaklıdır değeri ise: {b}")
            break            
pencere=tk.Tk()
pencere.title("fibonacci")

basamak=Entry(pencere)
basamak.pack()
 
ok=Button(pencere,text="OK",command=fibonacci)
ok.pack()

pencere.mainloop()