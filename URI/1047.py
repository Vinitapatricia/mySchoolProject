a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

jam = c - a

if jam < 0:
	jam += 24

menit = d - b

if menit <0:
	menit += 60
	if jam == 0:
		jam += 23
	else:
		jam -= 1

if a==b and c == d:
	print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
	print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(jam,menit))