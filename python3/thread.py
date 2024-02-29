import threading
toplam=0
def thread1(a,b):
    global toplam
    toplam=a+b   
    result = num1 + num2
def thread2(input_value):
    result = input_value * 2
    thread2.result = result
num1=4
num2=5
thread1=threading.Thread(target=thread1,args=(num1,num2))
thread2=threading.Thread(target=thread1,args=(num1,num2))
thread1.start()
thread1.join()
print(f"Toplam sonuc: {toplam}")


