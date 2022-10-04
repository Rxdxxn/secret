import random
sum=0   
n=int(input("Introduceti numarul de elemente:"))
N=0
A=[]
for x in range(n):
    A.extend([random.randint(1,100)])
for i in range(0,len(A)):
    sum=sum(A[i])-max(A)
print("Tabloul A generat este:",A)
print("Suma este egala cu:",sum)