from tkinter import Tk, ttk

#membuat sebuah instance /objek nyata
myApps = Tk()


#title itu method (fungsi di dalam objek) di dalam objek Tk()
myApps.title("Mt First Python Apps")
myApps.resizable(True, True)

#menambahkan label / tulisan
label1 = ttk.Label(myApps, text = "Nama Lengkap \t :")
#grid menampatkan object -> return none
label1.grid(column = 0, row = 0)
label2 = ttk.Label(myApps, text = "Tempat Lahir \t :")
label2.grid(column = 0, row = 1)
label3 = ttk.Label(myApps, text = "Tanggal Lahir \t :")
label3.grid(column = 0, row = 2)
label4 = ttk.Label(myApps, text = "Jenis Kelamin\t :")
label4.grid(column = 0, row = 3)
label5 = ttk.Label(myApps, text = "Alamat Tinggal\t :")
label5.grid(column = 0, row = 4)


def changeColor():
	button1.configure(text = "Color has been changed")
	label1.configure(foreground = "blue")
	label1.configure(text = "Nama Lengkap \t :")

#membuat tombol / button
button1 = ttk.Button(myApps, text = "Change Color", command = changeColor )
button1.grid( column = 0, row = 5)

#method untuk memulai GUI apps
if __name__ == "__main__":
	myApps.mainloop()