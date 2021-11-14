a = int(input())
b = int(input())

if ( b< a):
	tmp = a
	a = b
	b = tmp

if(a %2 !=0):
	a += 1


ans = 0
for x in range(a, b):
	if(x %2 != 0):
		ans += x

print(ans)