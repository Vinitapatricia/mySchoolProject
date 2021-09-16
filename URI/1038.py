code, jumlah = input().split()
code = int(code)
jumlah = int(jumlah)
hasil1 = float(4.00)*jumlah
hasil2 = float(4.50)*jumlah
hasil3 = float(5.00)*jumlah
hasil4 = float(2.00)*jumlah
hasil5 = float(1.50)*jumlah

if code == 1 :
	print("Total: R$ %.2f" %hasil1)
elif code == 2 :
	print("Total: R$ %.2f" %hasil2)
elif code == 3 :
	print("Total: R$ %.2f" %hasil3)
elif code == 4 :
	print("Total: R$ %.2f" %hasil4)
else :
	print("Total: R$ %.2f" %hasil5)