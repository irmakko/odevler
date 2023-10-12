notu = int(input("notunuzu girin:"))
if notu < 45:
    print("KALDI") 
elif 45>= notu and notu<60:
    print("KÖTÜ")
elif (60>= notu) and (notu <75):
    print("ORTA")
elif (75>= notu) and (notu <90):
    print("İYİ")
elif (90>= notu) and (notu <100):
    print("PEKİYİ")
else:
    print("NOT GİRİN!")

