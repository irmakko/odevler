import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
#ARAYÜZ
pencere=tk.Tk()
pencere.title("odev09")
def hesaplama(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            result+=chr((ord(char)-start+shift)%29+start)
        else:
            result+=char
    return result
def yeni_metin():
    input_text=textbox1.get()
    shift_value=int(textbox2.get())
    top=Toplevel(bg="gray")
    top.geometry("250x250")
    encrypted_text=hesaplama(input_text,shift_value)
    #lb 2.TKİNTER DA SİFRE YAZAN LABEL
    lb=Label(top,text="       ",font="width",bg="#ffffff",fg="#808080")
    lb.config(text=f" {encrypted_text}")
    lb.place(x=50,y=50)
    #lb2 SONUC LABEL'İ
    lb2=Label(top,text="       ",font="width",bg="#ffffff",fg="#808080")
    lb2.place(x=80,y=140)
    
    #2.TKİNTER DA Kİ ÇÖZ BUTONU
    print(textbox3.get())
    print(lb) 
    btn1=Button(top,text="ÇÖZ",command=cozucu(lb, str(textbox3.get())))#(lb, str(textbox3.get()))
    btn1.place(x=85,y=100)
    #2.TKİNTER DEKİ SAYİ YAZACAGİMİZ TEXTBOX
    textbox3=Entry(top,text=" ",font="width",bg="#ffffff",fg="#808080")
    textbox3.place(x=130,y=50)
    top.mainloop()
def cozucu(shift,text):
    result=""
    for char in text:  
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            result+=chr((ord(char)-start+shift)%29+start)
        else:
            result+=char
#BUTON
btn=Button(text="OK",command=yeni_metin)
btn.place(relx=0.80,rely=0.45)
#TEXTBOX1
textbox1=tk.Entry(pencere,width=30)
textbox1.pack()
#TEXTBOX2
textbox2=tk.Entry(pencere,width=5)
textbox2.pack()
pencere.mainloop()