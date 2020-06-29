from tkinter import Tk, ttk

#membuat sebuah instance /objek nyata
myApps = Tk()


#title itu method (fungsi di dalam objek) di dalam objek Tk()
myApps.title("Mt First Python Apps")
myApps.resizable(True, True)

#menambahkan label / tulisan
#grid menampatkan object -> return none
label1 = ttk.Label(myApps, text = "Nama Lengkap \t :")
label1.grid(column = 0, row = 0)

label2 = ttk.Label(myApps, text = "Tempat Lahir \t :")
label2.grid(column = 0, row = 1)

label3 = ttk.Label(myApps, text = "Tanggal Lahir \t :")
label3.grid(column = 0, row = 2)

label4 = ttk.Label(myApps, text = "Jenis Kelamin\t :")
label4.grid(column = 0, row = 3)

label5 = ttk.Label(myApps, text = "Umur\t\t :")
label5.grid(column = 0, row = 4)


def changeColor():
	label6 = ttk.Label(myApps, text = "Vinita Patricia")
	label6.grid(column = 1, row = 0)
	label7 = ttk.Label(myApps, text = "Palembang")
	label7.grid(column = 1, row = 1)
	label8 = ttk.Label(myApps, text = "23 Juni 2006")
	label8.grid(column = 1, row = 2)
	label9 = ttk.Label(myApps, text = "Perempuan")
	label9.grid(column = 1, row = 3)
	label10 = ttk.Label(myApps, text = "14\t ")
	label10.grid(column = 1, row = 4)
	button1.configure(text = "Color has been changed")
	label1.configure(foreground = "red")
	label2.configure(foreground = "orange")
	label3.configure(foreground = "yellow")
	label4.configure(foreground = "green")
	label5.configure(foreground = "blue")
	label6.configure(foreground = "red")
	label7.configure(foreground = "orange")
	label8.configure(foreground = "yellow")
	label9.configure(foreground = "green")
	label10.configure(foreground = "blue")

#membuat tombol / button
button1 = ttk.Button(myApps, text = "Change Color", command = changeColor )
button1.grid( column = 0, row = 5)

#method untuk memulai GUI apps
if __name__ == "__main__":
	myApps.mainloop()