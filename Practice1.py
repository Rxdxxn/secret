import random
n=int(input("Dati numarul de elemente:"))
spoz=0
sneg=0
k=[]
for x in range(n):
    k.extend([random.randint(-50,50)])
    while range(len(k)):
        k[x]=int(k[x])
        break
    if  k[x] > 0:
        spoz=spoz+k[x]
    elif k[x] < 0:
        sneg=sneg+k[x]
print(k)
print("Suma numerelor pozitive este:",spoz)
print("Suma numerelor negative este:",sneg)
    
