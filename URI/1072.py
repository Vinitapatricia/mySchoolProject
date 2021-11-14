a = int(input())

i = 0
o = 0

for x in range(a):
	b = int(input())

	if(b >= 10 and b <= 20):
		i += 1
	else:
		o += 1

print(f"{i} in")
print(f"{o} out")