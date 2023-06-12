
class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "Tic Tac Toe"
		self.row = 3
		self.column = 3


		#WINDOW CONFIG
		base  = 35
		ratio = (9,16)
		self.width = base * ratio[0]
		self.height = base * ratio[1]
		self.screen = f"{self.width}x{self.height}"

		#image
		self.init_img = "img/init_img.png"
		self.x_img = "img/X.png"
		self.o_img = "img/O.png"




		self.win_list = [ [[0,0],[0,1],[0,2]],
						[[1,0],[1,1],[1,2]],
						[[2,0],[2,1],[2,2]],
						[[0,0],[1,1],[2,2]],
						[[0,2],[1,1],[2,0]],
						[[0,0],[1,0],[2,0]],
						[[0,1],[1,1],[2,1]],
						[[0,2],[1,2],[2,2]]]

		self.card_list = [[0,0],[0,1],[0,2],
						[1,0],[1,1],[1,2],
						[2,0],[2,1],[2,2]
		]