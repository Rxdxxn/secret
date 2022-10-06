import random  
n=int(input("Introduceti numarul de elemente:"))
A=[]
for x in range(n):
    A.extend([random.randint(1,100)])
Suma=sum(A)-max(A)
print("Numarul maxim din tablou",max(A))
print("Tabloul A generat este:",A)
print("Suma este egala cu:",Suma)
