uang = float(input())
uang = uang*100

print("NOTAS:")
seratus = int(uang / 10000)
uang -= 10000 * seratus
print("%i nota(s) de R$ 100.00" %seratus)

limapuluh = int(uang / 5000)
uang -= limapuluh * 5000
print("%i nota(s) de R$ 50.00" %limapuluh)

duapuluh = int(uang / 2000)
uang -= duapuluh * 2000
print("%i nota(s) de R$ 20.00" %duapuluh)

sepuluh = int(uang / 1000)
uang -= sepuluh*1000
print("%i nota(s) de R$ 10.00" %sepuluh)

lima = int(uang/500)
uang-= lima*500
print("%i nota(s) de R$ 5.00" %lima)

dua = int(uang / 200)
uang -= dua * 200
print("%i nota(s) de R$ 2.00" %dua)

print("MOEDAS:")
satu = int(uang / 100)
uang -= satu * 100
print("%i moeda(s) de R$ 1.00" %satu)

nulLimaPuluh = int(uang / 50)
uang -= nulLimaPuluh*50
print("%i moeda(s) de R$ 0.50" %nulLimaPuluh)

nulDuaLima = int(uang / 25)
uang -= nulDuaLima*25
print("%i moeda(s) de R$ 0.25" %nulDuaLima)

nulsepuluh = int(uang / 10)
uang -= nulsepuluh*10
print("%i moeda(s) de R$ 0.10" %nulsepuluh)

nulLima = int(uang / 5)
uang -= nulLima*5
print("%i moeda(s) de R$ 0.05" %nulLima)

nulSatu = int(uang / 1)
uang -= nulSatu*1
print("%i moeda(s) de R$ 0.01" %nulSatu)