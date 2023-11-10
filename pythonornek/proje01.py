class Person:
    def __init__(self,name,surname,age):
        self.name=name 
        self.surname=surname
        self.age=age
        
#CREATE İŞLEMİ BAŞLANGICI
    def create_info(self):
        self.name=input("Name: ")
        self.surname=input("Surname: ")
        self.age=input("Age: ")
        self.number=input("Number: ")
        self._class=input("Class: ")
        print("ögrenci bilgileri başarıyla eklendi:)")
#READ İŞLEMİ BAŞLANGICI
    def read_info(self):
         print(f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nNumber: {self.number}\nClass: {self._class}")
#UPDATE İŞLEMİNİN BAŞLANGICI!!!
    def __init__(self,name,surname,age,number,_class):
        self.name=name 
        self.surname=surname
        self.age=age
        self.number=number
        self._class=_class
    
    def update_info(self):
        self.name=input("Yeni Name: ")
        self.surname=input("Yeni Surname: ")
        self.age=input("Yeni Age: ")
        self.number=input("Yeni Number: ")
        self._class=input("Yeni Class: ")
        print("Bilgiler güncellendi.")
#UPDATE İŞLEMİ BİTİŞİ!!!
#DELETE İŞLEMİ BAŞLANGICI!!!
    def delete_info(self):
        print("Bilgileri silmek için numarayi secin: ")
        print("1-Name:",self.name)
        print("1-Surname:",self.surname)
        print("1-Age:",self.age)
        print("1-Number:",self.number)
        print("1-Class:",self._class)
        choice=int(input("seçiminizi yapin: "))
        if choice==1:
            del self.name
        elif choice==2:
            del self.surname
        elif choice==3:
            del self.age
        elif choice==4:
            del self.number
        elif choice==5:
            del self._class
        else:
            print("geçersiz seçim.")
#DELETE İŞLEMİ BİTİŞİ!!!
class Student(Person):
    def __init__(self):
        super().__init__()
        print("ögrenci sinifina hoşgeldiniz.")
    def operations(self):
        print("Hangi işlemi yapmak istersiniz?: ")
        print("1-Name\n2-Surname\n3-Number\n4-Class")
class Teacher(Person):
    def __init__(self):
        super().__init__()
        print("öğretmen sinifina hoşgeldiniz.")
    def operations(self):
        print("Hangi işlemi yapmak istersiniz?: ")
        print("1-Name\n2-Surname\n3-section\n4-Sutudents")
        
    def main():
        while True:
            print("nerde işlem yapmak istersiniz?: ")
            print("1-Person\n2-Student\n3-Teacher")
            choice=input("seciminizi yapin(1,2 veya 3 girin): ")
            if choice == '1':
                person=Person()
                person.operations()
                break
            elif choice == '2':
                student=Student()
                student.operations()
                break
            elif choice == '3':
                teacher=Teacher()
                teacher.operations()
                break
            else:
                print("geçersiz seçim.Lütfen(1,2,3 veya 4 girin.)")
        while True:
            
            print("Hangi işlemi yapmak istersiniz?: ")
            print("1-Create\n2-Read\n3-Update\n4-Del1ete")  
            operation=input("seciminizi yapin(1,2 veya 3 girin): ")
            if   operation == "1":
                person.create_info()
            elif operation == "2":
                person.read_info()
            elif operation == "3":
                person.update_info()        
            elif operation == "4":
                person.delete_info()
                
    if __name__=="__main__":
        main()

            
