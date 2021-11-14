a = int(input())

for x in range(2,a+1):
	if(x%2 == 0):
		ans = x **2
		print(f"{x}^2 = {ans}")