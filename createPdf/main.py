from reportlab.pdfgen import canvas

dataSiswa = {
	"nama" :"Anas",
	"kelas": "VII-1",
	"laporan": "Rapor Kelas 7 Semster 2"
}

class Data:

	def __init__(self, filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading

myData = Data(str(dataSiswa["nama"]+dataSiswa["kelas"]+".pdf"),"Hasil Ujian", dataSiswa["laporan"])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)

#PRINT ON PAPER
myPdf.drawString(230,760,myData.heading)

myPdf.save()
#print("OK")