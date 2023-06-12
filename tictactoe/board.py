import tkinter as tk
import sys
from PIL import Image, ImageTk


class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config # config di Battleship
		self.row = self.config.row
		self.column = self.config.column

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		# virtual image
		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.create_header()
		self.create_sign()
		self.create_info()
		self.create_game()
		self.create_result_frame()

	def create_header(self):
		frame_h = self.config.height//3

		self.header_frame = tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h//3)
		self.header_frame.pack(fill = "x")

		self.header_label = tk.Label(self.header_frame, bg = "#3589ad", fg = "white", text = "tic tac toe", font = ("Comic Sans MS", 36, "bold"), image = self.virtual_image, compound = "c")
		self.header_label.grid(row = 0, column = 0)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_sign(self):
		frame_h = self.config.height//3

		self.sign_frame = tk.Frame(self, bg = "#3589ad", width= self.config.width, height = frame_h//3)
		self.sign_frame.pack(fill = "x")

		self.sign_label_border = tk.Label(self.sign_frame, bg = "#0f4158", fg = "#0f4158", text = "Player's turn", font = ("summer", 12), image = self.virtual_image, compound = "c", width = 185, height = 29)
		self.sign_label_border.grid(row = 0, column = 0)

		self.sign_label = tk.Label(self.sign_frame, bg = "black", fg = "#6fd04c", text = "Player 1's turn", font = ("summer", 12), image = self.virtual_image, compound = "c", width = 175, height = 19)
		self.sign_label.grid(row = 0, column = 0)

		self.sign_frame.grid_columnconfigure(0, weight = 1)
		self.sign_frame.grid_rowconfigure(0, weight = 1)

	def create_info(self):
		frame_h = self.config.height//3

		self.info_frame = tk.Frame(self, bg = "#3589ad", width= self.config.width, height = frame_h//5)
		self.info_frame.pack(fill = "x")

		self.info_label1 = tk.Label(self.info_frame, bg = "#3589ad", fg = "white", text = "Player 1 : X",font = ("Comic Sans MS", 12), image = self.virtual_image, compound = "c", width = 95, height = 25)
		self.info_label1.pack(side = "left")

		self.info_label2 = tk.Label(self.info_frame, bg = "#3589ad", fg = "white", text = "Player 2 : O",font = ("Comic Sans MS", 12), image = self.virtual_image, compound = "c", width = 95, height = 25)
		self.info_label2.pack(side = "right")

		self.info_frame.grid_columnconfigure(0, weight = 1)
		self.info_frame.grid_rowconfigure(0, weight = 1)

	def create_game(self):
		frame_h = 2*self.config.height //3

		self.game_frame = tk.Frame(self, bg = "#3589ad",width =self.config.width, height = frame_h)
		self.game_frame.pack(fill="x")

		self.game_frame.grid_columnconfigure(0, weight = 1)
		self.game_frame.grid_rowconfigure(0, weight = 1)

		self.create_board()
		self.create_button_board()

	def create_board(self):
		frame_h = 2*self.config.height //3

		self.frame_rows = [] #[0,1,2,3,4]
		colors = ["black", "red", "yellow"]

		nRow, nColumn = self.config.row, self.config.column
		row_height, row_width = frame_h//nRow, self.config.width - 29

		for i in range(nRow):
			frame = tk.Frame(self.game_frame, height = row_height, width = row_width, bg = colors[i])
			self.frame_rows.append(frame)

		for frame in self.frame_rows:
			frame.pack()

	def put_and_resize_photo(self, ori_img, scale):
		n_column = self.config.column
		button_width = self.config.width//n_column-8
		image = Image.open(ori_img)
		image_w, image_h = image.size
		ratio = image_w/button_width
		new_size = (int(image_w//ratio//scale), int(image_h//ratio//scale))
		image = image.resize(new_size)
		return ImageTk.PhotoImage(image)

	def create_button_board(self):
		frame_h = 2*self.config.height //3
		self.button_board = []

		nRow, nColumn = self.config.row, self.config.column
		button_height, button_width = frame_h//nRow - 7, self.config.width// nColumn- 19

		self.init_img_btn = self.virtual_image
		self.x_img_btn = self.put_and_resize_photo(self.config.x_img,3)
		self.o_img_btn = self.put_and_resize_photo(self.config.o_img,3)

		for i in range(nRow):
			row = []

			for j in range(nColumn):
				button = tk.Button(self.frame_rows[i], bg = "white", height = button_height, width = button_width,  image = self.init_img_btn ,command = lambda x = i, y = j:self.game.is_button_board_clicked(x,y))
				#text = "O", font = ("Arial", 20, "bold")
				row.append(button)


			self.button_board.append(row)

		for i in range(nRow):
			for j in range(nColumn):
				self.button_board[i][j].pack(side="left")


	def create_result_frame(self):
		frame_h = 2*self.config.height //3

		self.game_frame = tk.Frame(self, bg = "#3589ad",width =self.config.width, height = frame_h)
		self.game_frame.pack()

		self.resart_button = tk.Button(self.game_frame, text = "restart",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 12), width = 10, command = self.game.resart_game)
		self.resart_button.grid(row = 0, column = 0, sticky = "nsew", padx = 24, pady = 5)

		self.quit_button = tk.Button(self.game_frame, text = "back",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 12), width = 10, command = self.game.back_page)
		self.quit_button.grid(row = 0, column = 1, sticky = "nsew", padx = 24, pady = 5)
