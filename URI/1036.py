from math import sqrt
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
dis = b**2-4*a*c

if dis < 0 or a == 0:
	print("Impossivel calcular")
else :
	R1 = (-b+sqrt(dis))/(2*a)
	R2 = (-b-sqrt(dis))/(2*a)
	print("R1 = %.5f" %(R1))
	print("R2 = %.5f" %(R2))