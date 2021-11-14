cnt = 0

for x in range(5):
	a = int(input())
	if(a % 2 == 0):
		cnt += 1

print(f"{cnt} valores pares")