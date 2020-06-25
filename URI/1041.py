n1, n2 = input().split()
n1, n2 = float(n1), float(n2)

if n1 > 0: #(+)
	if n2 > 0: #(+)
		print("Q1")
	elif n2 < 0: #(-)
		print("Q4")
	else: #origin
		print("Eixo X")
elif n1 < 0: #(-)
	if n2 > 0: #(+)
		print("Q2")
	elif n2 < 0: #(-)
		print("Q3")
	else: #origin
		print("Eixo X")
else:
	if n2 != 0: #origin
		print("Eixo Y")
	else: #both origin
		print("Origem")