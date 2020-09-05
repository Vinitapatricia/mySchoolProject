from json import load, dump
from os import system
from getpass import getpass
from time import sleep
from reportlab.pdfgen import canvas
import random
import string

fileUser = 'produkuser.json'
fileProduct = 'produk.json'

user = {}
Product = {}

def loadData():
	global user, Product

	with open(fileUser) as p:
		user = load(p)

	with open(fileProduct) as p:
		Product = load(p)

	return True

def saveData():
	global user, Product

	with open(fileUser, 'w') as p:
		dump(user, p)

	with open(fileProduct, 'w') as p:
		dump(Product , p)

	return True

def randomCode():
	Kode = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.digits)).upper()
	return Kode

def login():
	counter = 1
	Username = input("Enter Username: ")
	Password = getpass("Enter Password: ")
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password) 
	else :
		dataCheck = False
		passLogin = False

	while (not dataCheck) or (not passLogin):
		counter += 1	
		if counter > 5:
			return False
		print("Username or Password is WRONG")
		Username = input("Enter Username: ")
		Password = getpass("Enter Password: ")
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password) 
	else:
		print("Login Successfull")
		return True

def Print_menu():
	system("cls")
	print("1. Print The Product")
	print("2. Add A Product")
	print("3. Remove A Product")
	print("4. Search A Product")
	print("5. Change Price")
	print("6. Change Product Name")
	print("7. Change Product Code")
	print("8. Change Discount Product")
	print("9. Print Product From The Highest Price")
	print("10. Print Product From The Lowest Price")
	print("11. Print Product From The Highest Discount")
	print("12. Print Product From The Lowest Discount")
	print("13. Print Product To Pdf")
	print("Q. Quit")

def printProduk():
	system("cls")
	if len(Product) > 0 :
		for produk in sorted(Product, key = Product.get, reverse = False):
			print(f"Product Code:{produk} \n Product:{Product[produk][0]}\t Normal Price :{Product[produk][1]}\t Discount Price:{Product[produk][2]} ")

	else:
		print("There Is No Product Available Right Now")

def tambahProduk():
	system("cls")
	print("Add Your Product\n")

	produk = input("Product  \t\t :").upper()
	code = randomCode()
	harga = int(input("Normal Price  \t\t :"))
	discount = float(input("Discount Price in Percent:"))
	discountPrice = int(harga-(harga*discount/100))

	#hargastr = str(harga)
	#discountPricestr = str(discountPrice)
	Product.update({code:[produk,harga,discountPrice,discount]})
	saveData()
	print("Saving Data...")
	sleep(2)
	print("Data Saved")

def hapusProduk():
	system("cls")
	print("Remove Your Product\n")

	produk = input("Product \t :").upper()
	code = input("Code \t\t :").upper()

	if code in Product:
		del Product[code]
		saveData()
		print("Removing Data...")
		sleep(2)
		print("Data Removed")
	else:
		print(f'{Product} does not exists in Product')

def lookUp():
	system("cls")
	print("Looking Up a Product \n")
	produk = input("Product \t :").upper()
	code = input("Code \t\t :").upper()
	if code in Product:
		system("cls")
		print(f"Product Code:{code} \n Product: {Product[code][0]}\t Normal Price:{Product[code][1]}\t Discount Price: {Product[code][2]}")
	else :
		print(f"{produk} doesn't exists Product")

def ubahHarga():
	system("cls")
	print("Change Price\n")
	produk = input("Product \t :").upper()
	code = input("Code \t\t :").upper()
	hargaBaru = int(input("New Price \t :"))

	if code in Product:
		harga = int(Product[code][1])
		diskon = int(Product[code][2])
		discount = float(((harga - diskon )*100)/harga)
		discountPrice = int(hargaBaru-(hargaBaru*discount/100))

		#hargaBarustr = str(hargaBaru)
		#discountPricestr = str(discountPrice)

		Product[code][1] = hargaBaru
		Product[code][2] = discountPrice
		saveData()
		print("Saving Data...")
		sleep(2)
		print("Data Saved")

	else:
		print(f"{produk} doesn't exists Product")

def ubahNama():
	system("cls")
	print("Change Product Name\n")
	produk = input("Old Product Name \t:").upper()
	code = input("Code \t\t\t:").upper()
	produkBaru = input("New Product Name \t:").upper()

	if code in Product:
		Product[code][0] = produkBaru

		saveData()
		print("Saving Data...")
		sleep(2)
		print("Data Saved")

	else:
		print(f"{produk} doesn't exists Product")

def ubahCode():
	system("cls")
	print("Change Product Code\n")
	produk = input("Product \t :").upper()
	code = input("Old Code \t :").upper()
	codeBaru = input("New Code \t :").upper()

	if code in Product:
		Product[codeBaru] = Product.pop(code)

		saveData()
		print("Saving Data...")
		sleep(2)
		print("Data Saved")

	else:
		print(f"{produk} doesn't exists Product")

def ubahDiskon():
	system("cls")
	print("Change Discount Product\n")
	produk = input("Product \t:").upper()
	code = input("Code \t\t:").upper()
	dikonBaru = float(input("New Discount \t:"))

	if code in Product:
		harga = int(Product[code][1])
		diskon = int(Product[code][2])
		discountPrice = int(harga-(harga * dikonBaru /100))
		#discountPricestr = str(discountPrice)

		Product[code][2] =discountPrice
		Product[code][3] = dikonBaru
		saveData()
		print("Saving Data...")
		sleep(2)
		print("Data Saved")

	else:
		print(f"{produk} doesn't exists Product")

def hargaTertinggi():
	system("cls")

	for produk in sorted(Product.items(), key= lambda k : k[1][1] , reverse=True):
		print(f"Product Code:{produk[0]} \n Product: {produk[1][0]}\t Normal Price:{produk[1][1]}\t Discount Price: {produk[1][2]}")

def hargaTerendah():
	system("cls")

	for produk in sorted(Product.items(), key= lambda k : k[1][1] , reverse=False):
		print(f"Product Code:{produk[0]} \n Product: {produk[1][0]}\t Normal Price:{produk[1][1]}\t Discount Price: {produk[1][2]}")

def diskonTertinggi():
	system("cls")

	for produk in sorted(Product.items(), key= lambda k : k[1][3] , reverse=True):
		print(f"Product Code:{produk[0]} \n Product: {produk[1][0]}\t Normal Price:{produk[1][1]}\t Discount Price: {produk[1][2]}")

def diskonTerendah():
	system("cls")

	for produk in sorted(Product.items(), key= lambda k : k[1][3] , reverse=False):
		print(f"Product Code:{produk[0]} \n Product: {produk[1][0]}\t Normal Price:{produk[1][1]}\t Discount Price: {produk[1][2]}")

def Pdf():

	class Data:

		def __init__(self, filename, documentTitle, heading):
			self.filename = filename
			self.documentTitle = documentTitle
			self.heading = heading
			self.info = Product

	myData = Data("Product.pdf","Product List", "hipirmit")
	myPdf = canvas.Canvas(myData.filename)
	myPdf.setTitle(myData.documentTitle)

	#PRINT ON PAPER
	myPdf.setFont("Courier", 30)
	myPdf.setFillColorRGB(0,0,0)
	myPdf.drawCentredString(300,770, "Product List")
	myPdf.line(30,760, 580, 760)
	#           x1  y1   x2   y2

	myText = myPdf.beginText(35,680)
	myText.setFont("Helvetica", 18)

	for produk in sorted(Product, key = Product.get, reverse = False):
		code = "Product Code  : " + produk
		nama = "Product           : "+ Product[produk][0]
		harga ="Normal Price   : "+ str(Product[produk][1]) 
		diskon= "Discount Price : "+ str(Product[produk][2])
		garis = myPdf.line(30,760, 580, 760)
		Lines = [code,nama,harga,diskon,garis]

		for line in Lines:
			myText.textLine(line)
		myPdf.drawText(myText)

	myPdf.save()
