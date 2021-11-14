ans = 0
cnt = 0

for x in range(6):
	a = float(input())
	if a >= 0:
		cnt += 1
		ans += a

ans = ans /cnt

print(f"{cnt} valores positivos")
print("%.1f" %ans)