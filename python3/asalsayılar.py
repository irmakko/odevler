sayi=int(input("Sayiyi Girin : "))
if sayi>1:   
   for i in range(2,sayi):
       if (sayi%i)==0:
           print(sayi," Asal Değildir.")
           break
   else:
       print(sayi," Asal Sayidir.")
else:
   print(sayi," Asal Değildir.")
   

        
        

   