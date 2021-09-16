a = float(input())

if a > 2000:
	earn = a*4/100
	new = a + earn
	persen = 4
elif a > 1200:
	earn = a*7/100
	new = a + earn
	persen = 7
elif a > 800:
	earn = a*10/100
	new = a + earn
	persen = 10
elif a > 400:
	earn = a*12/100
	new = a + earn
	persen = 12
else:
	earn = a*15/100
	new = a + earn
	persen = 15

print("Novo salario: %.2f" %new)
print("Reajuste ganho: %.2f" % earn)
print(f"Em percentual: {persen} %")