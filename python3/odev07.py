bilgi=["ırmak,koc,16","gizem,koc,17","zehra,sayım,16","gülsüm,sayım,19"]
class Person:
    def __init__(self,ad,soyad,yas):
        self.Ad=ad
        self.Soyad=soyad
        self.Yas=yas
    person=[Person("","","")for_in range(5)]
    def  splitter(input_str):
        values=input_str.split(',')
        return values
    for i, entry in enumerate(bilgi):
        myValues=splitter(entry)
        person[i].Ad=myValues[0]
        person[i].Ad=myValues[1]
        person[i].Ad=int(myValues[2])
    for a in person:
        print(f"Ad: {a.Ad} , Soyad: {a.Soyad}, Yas: {a.Yas}")