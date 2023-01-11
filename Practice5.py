import random  
n=int(input("Introduceti numarul de elemente:"))
A=[]
for x in range(n):
    A.extend([random.randint(1,100)])
Suma=sum(A)-max(A)
print("Numarul maxim din tablou",max(A))
print("Tabloul A generat este:",A)
print("Suma este egala cu:",Suma)


volume=[120,40,40,100,150]
preturi=[150,60,80,120,180]
volum = 250
n = 5
sumMax = 0
volumdat = 0


def Sol_Pos(a,b,c,d,e):
	if (volume[0]*a+volume[1]*b+volume[2]*c+volume[3]*d+volume[4]*e<=volum) and (a<=1 and b<=1 and c<=1 and d<=1 and e<=1):
		return True
	else:
		return False

def Prel_Sol(a,b,c,d,e):
    suma = preturi[0]*a+preturi[1]*b+preturi[2]*c+preturi[3]*d+preturi[4]*e
    global volumdat
    global sumMax
    if suma > sumMax:
        sumMax = suma
        volumdat = volume[0] * a + volume[1] * b + volume[2] * c + volume[3] * d + volume[4] * e




for a in range (0,n+1):
	for b in range (0,n+1):
		for c in range (0,n+1):
			for d in range (0,n+1):
				for e in range (0,n+1):
					if (Sol_Pos(a,b,c,d,e)):
						Prel_Sol(a,b,c,d,e)

print(sumMax)
print(volumdat)
