import random
k=[]
q=[]
for x in range(1):
    k.extend([random.randint(1,999999999)])
    k[x]=int(k[x])
    for i in str(k[x]):
        q.append(int(i))
    a0=q.count(0)
    a1=q.count(1)
    a2=q.count(2)
    a3=q.count(3)
    a4=q.count(4)
    a5=q.count(5)
    a6=q.count(6)
    a7=q.count(7)
    a8=q.count(8)
    a9=q.count(9)
print("Numarul initial generat este:",k[x])
print("0 apare de",a0,"ori,","1 apare de",a1,"ori,",
"2 apare de",a2,"ori,","3 apare de",a3,"ori,","4 apare de",a4,"ori,",
"5 apare de",a5,"ori,","6 apare de",a6,"ori,","7 apare de",a7,"ori,",
"8 apare de",a8,"ori,","9 apare de",a9,"ori")