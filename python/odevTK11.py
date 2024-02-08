import tkinter as tk
from tkinter import messagebox
import random
from tkinter import *
sayi=set()
def  rastgele_sayi():
    global sayi
    a=random.randint(1,100)
    while a in sayi:
        a=random.randint(1,100)
    sayi.add(a)
    if a<50:
        listbox1.insert(tk.END,a)
    elif a>50:
        listbox2.insert(tk.END,a)
    else:
        messagebox.showinfo("Mesaj","Sayi 50 oldu")
        sayi=set()
pencere=tk.Tk()
pencere.title("Rastgele Sayi")
frame=tk.Frame(pencere)
frame.pack(padx=20,pady=20)
#SCROLLBAR1 VE SCROLLBAR2
scrollbar1=Scrollbar(pencere)
scrollbar1.pack(side=LEFT,fill=Y)
scrollbar2=Scrollbar(pencere)
scrollbar2.pack(side=RIGHT,fill=Y)
#BUTTON
buton=tk.Button(frame,text="sayi uret",command=rastgele_sayi)
buton.pack(side=tk.LEFT,padx=15)
#LİSTBOX1 VE SCROLLBAR1
listbox1=tk.Listbox(pencere,yscrollcommand=scrollbar1.set)
listbox1.pack(side=tk.LEFT,padx=10)
scrollbar1.config(command=listbox1.yview)
#LİSTBOX2 VE SCROLLBAR2
listbox2=tk.Listbox(pencere,yscrollcommand=scrollbar2.set)
listbox2.pack(side=tk.RIGHT,padx=10)
scrollbar2.config(command=listbox2.yview)

pencere.mainloop()