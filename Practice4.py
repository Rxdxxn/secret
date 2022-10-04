import random
zar1=0
zar2=0
sum=0
while True:
    zar1 = random.randint(1,6)
    zar2 = random.randint(1,6)
    sum=zar1+zar2
    if zar1==zar2:
        print("Valoarea dublului este:",zar1)
        break
print("Suma dublului este",sum)