uang = int(input())
print("%i" %uang)

seratus = int(uang / 100)
uang -= 100 * seratus
print("%i nota(s) de R$ 100,00" %seratus)

limapuluh = int(uang / 50)
uang -= limapuluh * 50
print("%i nota(s) de R$ 50,00" %limapuluh)

duapuluh = int(uang / 20)
uang -= duapuluh * 20
print("%i nota(s) de R$ 20,00" %duapuluh)

sepuluh = int(uang / 10)
uang -= sepuluh*10
print("%i nota(s) de R$ 10,00" %sepuluh)

lima = int(uang/5)
uang-= lima*5
print("%i nota(s) de R$ 5,00" %lima)

dua = int(uang / 2)
uang -= dua * 2
print("%i nota(s) de R$ 2,00" %dua)

satu = int(uang / 1)
uang -= satu * 1
print("%i nota(s) de R$ 1,00" %satu)