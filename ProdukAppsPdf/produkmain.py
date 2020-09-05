from json import load, dump
from os import system
from time import sleep

import feature

statusLoading = feature.loadData()

system('cls')

if statusLoading:
	passLogin = feature.login()
	if passLogin:
		print("Welcome To The Apps")
		sleep(1.6)
		system('cls')
		PilihanMenu = " "

		while PilihanMenu != "q":
			feature.Print_menu()
			PilihanMenu = input("Type In A Number:").lower()

			if PilihanMenu == "1":
				feature.printProduk()
				input("ENTER To Exit")

			elif PilihanMenu == "2":
				feature.tambahProduk()
				input("ENTER To Exit")

			elif PilihanMenu == "3":
				feature.hapusProduk()
				input("ENTER To Exit")

			elif PilihanMenu == "4":
				feature.lookUp()
				input("ENTER To Exit")

			elif PilihanMenu == "5":
				feature.ubahHarga()
				input("ENTER To Exit")

			elif PilihanMenu == "6":
				feature.ubahNama()
				input("ENTER To Exit")

			elif PilihanMenu == "7":
				feature.ubahCode()
				input("ENTER To Exit")

			elif PilihanMenu == "8":
				feature.ubahDiskon()
				input("ENTER To Exit")

			elif PilihanMenu == "9":
				feature.hargaTertinggi()
				input("ENTER To Exit")

			elif PilihanMenu == "10":
				feature.hargaTerendah()
				input("ENTER To Exit")

			elif PilihanMenu == "11":
				feature.diskonTertinggi()
				input("ENTER To Exit")

			elif PilihanMenu == "12":
				feature.diskonTerendah()
				input("ENTER To Exit")

			elif PilihanMenu == "q":
				system("cls")
				print("Thank You For Using Our Apps")
				break

			else:
				system("cls")
				print("Input Menu Choice Corectly")
				input("ENTER to Exit")
	else:
		print("Falied To Login")
else :
	print("Apps Can't run.")