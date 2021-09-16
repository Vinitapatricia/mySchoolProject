a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if (a >= b + c) or (b >= a + c) or (c >= a + b):
	print("NAO FORMA TRIANGULO")

elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
	print("TRIANGULO RETANGULO")

elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
	print("TRIANGULO OBTUSANGULO")

elif (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2) or (c**2 < b**2 + a**2):
	print("TRIANGULO ACUTANGULO")

if a == b == c :
	print("TRIANGULO EQUILATERO")

elif a == b or a == c or b == c:
	print("TRIANGULO ISOSCELES")