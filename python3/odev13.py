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
    a1=tree.insert(ana_oge_a,"end",text="A1",tags=("A",),open=False)
    a2=tree.insert(ana_oge_a,"end",text="A2",tags=("A",),open=False)
    a3=tree.insert(ana_oge_a,"end",text="A3",tags=("A",),open=False)
    #A1,A2,A3'ÜNDE ALT CHECKBOXLARINI OLUŞTURALIM
    a1_1=tree.insert(a1,"end",text="A1.1",tags=("A",))
    a2_2=tree.insert(a2,"end",text="A2.2",tags=("A",))
    a3_3=tree.insert(a3,"end",text="A3.3",tags=("A",))
    #B1,B2,B3 ALT CHECKBOXLARI OLUŞTURALIM
    b1=tree.insert(ana_oge_b,"end",text="B1",tags=("B",),open=False)
    b2=tree.insert(ana_oge_b,"end",text="B2",tags=("B",),open=False)
    b3=tree.insert(ana_oge_b,"end",text="B3",tags=("B",),open=False)
    #B1,B2,B3'NDE ALT CHECKBOXLARINI OLUŞTURALIM
    b1_2=tree.insert(b1,"end",text="B1.1",tags=("B",))
    b2_2=tree.insert(b2,"end",text="B2.2",tags=("B",))
    b3_3=tree.insert(b3,"end",text="B3.3",tags=("B",))

    pencere.mainloop()

if __name__== "__main__":  
    main()