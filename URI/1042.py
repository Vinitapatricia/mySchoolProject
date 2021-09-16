x , y , z = input().split()
x , y , z = int(x), int(y), int(z)

a = x
b = y
c = z
if b < a:
	tmp = b
	b = a
	a = tmp
if c < a:
	tmp = c
	c = a
	a = tmp
if c < b:
	tmp = c
	c = b
	b = tmp

print("%i"%a)
print("%i"%b)
print("%i"%c)
print()
print("%i"%x)
print("%i"%y)
print("%i"%z)