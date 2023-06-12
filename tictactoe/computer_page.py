import tkinter as tk
import sys
from PIL import Image, ImageTk


class ComputerPage(tk.Frame):

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
		self.create_button()

	def create_header(self):
		frame_h = 2*self.config.height//3 -99

		self.header_frame = tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.header_label = tk.Label(self.header_frame, bg = "#3589ad", fg = "white", text = "with computer", font = ("Comic Sans MS", 31, "bold"), image = self.virtual_image, compound = "c", height = frame_h )
		self.header_label.grid(row = 0, column = 0)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_button(self):
		frame_h = self.config.height//2 - 119

		self.button_frame = tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.button_frame.pack(fill = "x")

		self.choose_frame = tk.Frame(self.button_frame, bg = "red", width = self.config.width, height = frame_h//4)
		self.choose_frame.pack()

		self.choose_label = tk.Label(self.choose_frame, bg = "#3589ad", fg = "white", text = "Pick X or O", font = ("Comic Sans MS", 23, "bold"), image = self.virtual_image, compound = "c", height = frame_h //5)
		self.choose_label.grid(row = 0, column = 0)

		self.x_or_o_frame = tk.Frame(self.button_frame, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.x_or_o_frame.pack()

		self.x_button = tk.Button(self.x_or_o_frame, text = "X",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 13), width = 8, command = self.game.choose_x)
		self.x_button.grid(row = 0, column = 0, sticky = "nsew", padx = 25, pady = 25)

		self.o_button = tk.Button(self.x_or_o_frame, text = "O",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 13), width = 8, command = self.game.choose_o)
		self.o_button.grid(row = 0, column = 1, sticky = "nsew", padx = 25, pady = 25)

		self.space_frame =tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h//2 +19)
		self.space_frame.pack(fill = "both")

		self.next_back_frame =tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.next_back_frame.pack(fill = "both")

		self.back_button = tk.Button(self.next_back_frame, text = "back", bg = "#dbc225", fg = "white", font = ("Arial", 12, "bold"), width = 7, command = self.game.back_page)
		self.back_button.grid(row = 0, column = 0, sticky = "nsew", padx = 15, pady = 10)

		self.next_button = tk.Button(self.next_back_frame, text = "next", bg = "#dbc225", fg = "white", font = ("Arial", 12, "bold"), width = 7, command = self.game.next_pc_page)
		self.next_button.grid(row = 0, column = 1, sticky = "nsew", padx = 110, pady = 10)