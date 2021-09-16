salary = float(input())

if salary > 4500.00:
	salary -= 4500
	pay = (salary * 28/100) + (1500 * 18 /100)+(1000 * 8 /100)
	print("R$ %.2lf" %pay)

elif salary > 3000.01:
	salary -= 3000
	pay = (salary * 18/100) + (1000 * 8 /100)
	print("R$ %.2lf" %pay)
elif salary > 2000.01:
	salary -= 2000
	pay = salary * 8 / 100
	print("R$ %.2lf" %pay)

else:
	print("Isento")
