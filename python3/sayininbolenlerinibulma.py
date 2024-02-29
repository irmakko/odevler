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




    import tkinter as tk
from tkinter import ttk
def checkbox_olustur(checkbox,alt_checkboxes):
    for alt_checkbox in alt_checkboxes:
        alt_checkbox.state(['!alternate'])
        alt_checkbox.state(['selected' if checkbox.instate(['selected']) else '!selected'])
def main():
    pencere=tk.Tk()
    pencere.title("Checkbox")
    #A VE A1,A2,A3
    cerceve_a=ttk.Frame(pencere,padding="10")
    cerceve_a.pack(fill=tk.BOTH,expand=True)
    checkbox_a=ttk.Checkbutton(cerceve_a,text="A")
    checkbox_a.pack()
    
    alt_checkbox_a=[]
    for i in range(1,4):
        alt_checkbox=ttk.Checkbutton(cerceve_a,text=f"A{i}")
        alt_checkbox.pack()
        alt_checkbox_a.append(alt_checkbox)
    checkbox_a.config(command=lambda: checkbox_olustur(checkbox_a,alt_checkbox))
    #B VE B1,B2,B3
    cerceve_b=ttk.Frame(pencere,padding="10")
    cerceve_b.pack(fill=tk.BOTH,expand=True)
    checkbox_b=ttk.Checkbutton(cerceve_b,text="B")
    checkbox_b.pack()
    
    alt_checkbox_b=[]
    for i in range(1,4):
        alt_checkbox=ttk.Checkbutton(cerceve_b,text=f"B{i}")
        alt_checkbox.pack()
        alt_checkbox_b.append(alt_checkbox)
    checkbox_b.config(command=lambda: checkbox_olustur(checkbox_b,alt_checkbox))
    pencere.mainloop()
if __name__=="__main__":
    main()