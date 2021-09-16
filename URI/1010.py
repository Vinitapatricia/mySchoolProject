code1, Jumlah1, Harga1 = [float(Harga1) for Harga1 in (input()).split()]
code2, Jumlah2, Harga2 = [float(Harga2) for Harga2 in (input()).split()]
ans = float((Jumlah1*Harga1) + (Jumlah2 * Harga2))
print("VALOR A PAGAR: R$ %.2f" %ans)