a, b = input().split()
a, b = int(a), int(b)

if (b%a == 0) or (a%b == 0):
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")