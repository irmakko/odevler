
import random
#Insertion sort algoritması
def insertion_sort(A):
    for i in range(1, len(A)):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    return A
#Random sayılar oluşturur (maksimum 15 sayı)
random_numbers=[random.randint(0,1000) for _ in range(15)]
#Sıralı durum (best case)
best_case=list(range(1,16))
#Tersine sıralı durum (worst case)
worst_case=list(range(15,0,-1))

#Random sayıları sırala
print("Random sayılar:",random_numbers)
#insertion_sort(random_numbers)
#Best case'i sırala
print("En iyi durum (Best case):",insertion_sort(best_case))
#insertion_sort(best_case)
#Worst case'i sırala
print("En kötü durum (Worst case):",worst_case)
insertion_sort(worst_case)