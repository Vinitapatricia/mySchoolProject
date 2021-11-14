even = 0
odd = 0
pos = 0
ne = 0

for x in range(5):
	a = int(input())
	if(a % 2 == 0):
		even += 1
	else:
		odd += 1

	if(a > 0):
		pos += 1
	elif(a < 0):
		ne += 1


print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{ne} valor(es) negativo(s)")