detik = int(input())

menit = int(detik/60)
detik -= menit*60
jam = int(menit/60)
menit -= jam*60

print(repr(jam)+":"+repr(menit)+":"+repr(detik))
