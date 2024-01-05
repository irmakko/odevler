import tkinter as tk
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
    encrypted_text=hesaplama(input_text,shift_value)
    label.config(text=f" {encrypted_text}")
#ARAYÜZ
pencere=tk.Tk()
pencere.title("odev09")
#TEXTBOX1
textbox1=tk.Entry(pencere,width=30)
textbox1.pack()
#TEXTBOX2
textbox2=tk.Entry(pencere,width=5)
textbox2.pack()
#BUTON
button=tk.Button(pencere,text="OK",command=yeni_metin)
button.pack()
#LABEL
label=tk.Label(pencere,text="Yeni Metin: ")
label.pack()
pencere.mainloop()