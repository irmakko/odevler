import tkinter as tk
from tkinter import ttk
def main():
    pencere=tk.Tk()
    pencere.title("Checkbox")
    tree=ttk.Treeview(pencere,columns=("checkbox"),show="tree")
    tree.heading("#0",text="Items")
    tree.pack()
    #A VE B ANA TREEVİEW OLUŞTUR
    ana_oge_a=tree.insert("","end",text="A",open=False)
    ana_oge_b=tree.insert("","end",text="B",open=False)
    #A1,A2,A3 ALT CHECKBOX LARI OLUŞTURALIM
    a1=tree.insert(ana_oge_a,"end",text="A1",tags=("A",))
    a2=tree.insert(ana_oge_a,"end",text="A2",tags=("A",))
    a3=tree.insert(ana_oge_a,"end",text="A3",tags=("A",))
    #B1,B2,B3 ALT CHECKBOXLARI OLUŞTURALIM
    b1=tree.insert(ana_oge_b,"end",text="B1",tags=("B",))
    b2=tree.insert(ana_oge_b,"end",text="B2",tags=("B",))
    a3=tree.insert(ana_oge_b,"end",text="B3",tags=("B",))

    pencere.mainloop()

if __name__== "__main__":
    main()