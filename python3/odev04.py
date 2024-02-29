def cift_tek(sayi):
    if sayi %2 == 0:
        cift.append(sayi)
    else:
        tek.append(sayi)
    
    print("çift sayılar:")
    print(cift)
    print("tek sayılar:")
    print(tek)

sayilar=[]
cift=[]
tek=[]
for sayi in range(10):
    cift_tek(sayi)
    

    
