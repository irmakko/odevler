people=[]
class Person:
    def __init__(self,name,surname,age,id,x):
        self.name=name 
        self.surname=surname
        self.age=age
        self.x=x
        self.id=id
        Person.id=people.count()+1
    def operations(self):
        person=Person("","","")
        secim=int(input("hangi işlemi yapmak istersiniz?\n1.Create\n2.Read\n3.Update\n4.Delete\nSeçiniz: "))
        if secim == 1:
            person.create()
        elif secim == 2:
            person.read()
        elif secim == 3:
            person.update() 
        elif secim == 4:
            person.delete() 
        elif secim==5:
            pass      
        else:
            print("Geçersiz seçenek.")
                   
#CREATE İŞLEMİ BAŞLANGICI
    def create(self):
        person = Person(input("Name: "), input("Surame: "), input("Age: "))
        
        people.append(person) 
        print("ögrenci bilgileri başariyla eklendi:)")  
        
#READ İŞLEMİ BAŞLANGICI
    def read(self):
        id=int(input("id giriniz: "))
        for x in people:
            if id==1:
                print("Read ayarina hoşgeldiniz:)")
                print(f"Name: {x.name}")        
                print(f"Surname: {x.surname}")
                print(f"Age: {x.age}")
                
#UPDATE İŞLEMİNİN BAŞLANGICI!!!
    def __init__(self,name,surname,age):
            self.name=name 
            self.surname=surname
            self.age=age
    def update(self):
        id=int(input("id giriniz: "))
        for x in people:
            if id==2:
                x.name=input("Yeni Name: ")
                x.surname=input("Yeni Surname: ")
                x.age=input("Yeni Age: ")
                print("Bilgiler güncellendi.")
    
#UPDATE İŞLEMİ BİTİŞİ!!!
#DELETE İŞLEMİ BAŞLANGICI!!!
    def delete(self):
        id=int(input("id giriniz: "))
        for x in people:
            if id==3:
                print("Bilgileri silmek için numarayi secin: ")
                print("1-Name:",x.name)
                print("2-Surname:",x.surname)
                print("3-Age:",x.age)
            
            choice=int(input("seçiminizi yapin: "))
            if choice==1:
                del x.name
            elif choice==2:
                del x.surname
            elif choice==3:
                del x.age
            else:
                print("geçersiz seçim.")
#DELETE İŞLEMİ BİTİŞİ!!!


class Student(Person):
    def __init__(self):
        #super().__init__()
        print("ögrenci sinifina hoşgeldiniz.")
    def operations(self):
        print("Hangi işlemi yapmak istersiniz?: ")
        print("1-Name\n2-Surname\n3-Number\n4-Class")
class Teacher(Person):
    def __init__(self):
        #super().__init__()
        print("öğretmen sinifina hoşgeldiniz.")
    def operations(self):
        print("Hangi işlemi yapmak istersiniz?: ")
        print("1-Name\n2-Surname\n3-section\n4-Sutudents")
        
          
    def main():
        #people=[]
        while True:
            print("nerde işlem yapmak istersiniz?: ")
            print("1-Person\n2-Student\n3-Teacher")  
            choice=input("seciminizi yapin(1,2 veya 3 girin): ")
            if choice == '1':
                    person = Person("", "", "")
                    person.operations()  
                   
            elif choice == '2':
                    student=Student()
                    student.operations()           
            elif choice == '3':
                    teacher=Teacher()
                    teacher.operations()
            elif choice == '4':  
                pass   
            else:
                    print("geçersiz seçim.Lütfen(1,2,3 veya 4 girin.)")
                    continue        
            while True:        
                print("Bundan sonra nerde işlem yapmak istiyorsunuz?")    
                print("1.Create\n2.Read\n3.Update\n4.Delete\n5.Exit")
                operation=int(input())
                if operation == 1:
                    person.create()
                elif operation == 2:
                    person.read()
                elif operation == 3:
                    person.update() 
                elif operation == 4:
                    person.delete() 
                elif operation==5:
                    break      
                else:
                    print("Geçersiz seçenek.")
    if __name__=="__main__":
        main()
    
        

            
