a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if a< b+c and b< a+c and c<a+b:
	segitiga = a+b+c
	print("Perimetro = %.1f" %segitiga)

else:
	trapesium = ((a+b)*c)/2
	print("Area = %.1f" %trapesium)