dia, day1 = input().split()
day1 = int(day1)
h1, m1, s1 = input().split(":")
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)

dia, day2 = input().split()
day2 = int(day2)
h2, m2, s2 = input().split(":")
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)

s = s2-s1
m = m2-m1
h = h2-h1
d = day2-day1

if s<0:
	s += 60
	m -=1
if m < 0:
	m += 60
	h -=1
if h < 0:
	h +=24
	d -= 1

print(f"{d} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)")