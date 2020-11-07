from tkinter import Tk, Label, StringVar, ttk, Entry, Button, LabelFrame, Menu, Frame
from tkinter import messagebox as Msg # untuk menampilkan kotak pesan window.

def msg_box():
	result_user = Msg.askyesnocancel("Confirmastion Saving Data", "Are you sure to save this product?")
	print(result_user)
	if result_user == True:
		Msg.showinfo("Confirmastion Saving Data", "Data Saved")

def close_program():
	window.quit()
	window.destroy()
	exit()

window = Tk()
window.title("*Product Apps*")
#window.minsize(800, 600)
window.resizable(False, False)

tabControl = ttk.Notebook(window)

tabRegister = Frame(tabControl)
tabSearch = Frame(tabControl)

tabControl.add(tabRegister, text='Register Product')
tabControl.add(tabSearch, text = "Search Product")

tabControl.pack(expand = 1, fill = "both")

# MENU BAR
menu_bar = Menu(window)
window.config(menu=menu_bar)

label_menu_file = Menu(menu_bar, tearoff=0)
label_menu_file.add_command(label="Close", command=close_program)

menu_bar.add_cascade(label="File", menu=label_menu_file)

label_help_menu = Menu(menu_bar, tearoff=0)
label_help_menu.add_command(label="Help")
label_help_menu.add_command(label="About")

label_help_menu.add_separator()

label_help_menu.add_command(label="Version 1.7.Beta")

menu_bar.add_cascade(label="Help", menu=label_help_menu)



# REGISTER PRODUK
header = Label(tabRegister, text = "REGISTER PRODUCT", font = ("arial", 20, "bold"), bd=10, padx=25, pady=5, width = 24)
header.grid(columnspan = 2)

label_name = Label(tabRegister, text = "Product Name       : ", font = ("arial", 18))
label_name.grid(column = 0, row = 1, )

product = StringVar()
entry_product = Entry(tabRegister, textvariable = product, font = ("arial", 18), width = 20)
entry_product.grid(column = 1, row = 1)


label_code = Label(tabRegister, text = "Product Code        : ", font = ("arial", 18))
label_code.grid(column = 0, row = 2 )

code = StringVar()
entry_code = Entry(tabRegister, textvariable = code, font = ("arial", 18), width = 20)
entry_code.grid(column = 1, row = 2  )

label_quantity = Label(tabRegister, text = "Product Quantity   : ", font = ("arial", 18))
label_quantity.grid(column = 0, row = 3 )

quantity = StringVar()
entry_quantity = Entry(tabRegister, textvariable = quantity, font = ("arial", 18), width = 20)
entry_quantity.grid(column = 1, row = 3  )


label_price = Label(tabRegister, text = "Product Price        : ", font = ("arial", 18))
label_price.grid(column = 0, row = 4 )

price = StringVar()
entry_price = Entry(tabRegister, textvariable = price, font = ("arial", 18), width = 20)
entry_price.grid(column = 1, row = 4  )

label_discount = Label(tabRegister, text = "Discount Product  : ", font = ("arial", 18))
label_discount.grid(column = 0, row = 5 )

discount = StringVar()
entry_discount = Entry(tabRegister, textvariable = discount, font = ("arial", 18), width = 20)
entry_discount.grid(column = 1, row = 5  )

label_price = Label(tabRegister, text = "       ", font = ("arial", 12))
label_price.grid(column = 0, row = 6 )

button = Button(tabRegister, font = ("arial", 18), text = "SUMBIT", bd=3, padx=3, pady=3, command = msg_box)
button.grid(columnspan = 2, row =7)


#SEARCH PRODUK
header2 = Label(tabSearch, text = "SEACRH PRODUCT", font = ("arial", 20, "bold"), bd=10, padx=25, pady=5, width = 24)
header2.grid(columnspan = 2)

search = StringVar()
entry_search = Entry(tabSearch, textvariable = search, font = ("arial", 18), width = 25)
entry_search.grid(column = 0, row = 1 )

button_search = Button(tabSearch, font = ("arial", 12), text = "SEARCH", bd=3, padx=3, pady=3)
button_search.grid(column= 1, row =1)

frame_search = LabelFrame(tabSearch, text = "RESULT PRODUCT")
frame_search.grid(columnspan = 2, row =2,padx=5, pady=5)

Label_search = Label(frame_search, text = "-", font = ("arial", 18), bd=10, padx=25, pady=35, width = 24)
Label_search.grid(column = 0, row =3)


window.mainloop()