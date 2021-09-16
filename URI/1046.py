a, b = input().split()
a, b = int(a), int(b)

durasi = 24 + b - a

if durasi <= 24:
	print("O JOGO DUROU %i HORA(S)" %durasi)

elif durasi > 24:
	durasi2 = durasi%24
	print("O JOGO DUROU %i HORA(S)" %durasi2)
