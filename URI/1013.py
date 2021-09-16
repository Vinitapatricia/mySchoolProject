import math

a,b,c = input().split()
hasil1 = (int(a)+ int(b) + abs(int(a)-int(b)))/2
hasil2 = (int(hasil1)+ int(c) + abs(int(hasil1)-int(c)))/2

print("%d eh o maior" %hasil2)