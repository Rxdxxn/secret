import random
n=round(random.random()*10)
da=0
k=[]
for x in range(n):
    k.extend([random.randint(1,6)])
da = k.count(6)
print("Zarul sa aruncat de",n,"ori!")
print("Valorile aparute dupa aruncarea zarului:",k)
print("Valoarea 6 a aparut de",da,"ori!")
