hari = int(input())

tahun = int(hari/365)
hari -= tahun*365

bulan = int(hari/30)
hari -= bulan*30

print("%d ano(s)" %tahun)
print("%d mes(es)" %bulan)
print("%d dia(s)" %hari)