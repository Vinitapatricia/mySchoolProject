import tkinter as tk
import sys
from PIL import Image, ImageTk


class ModePage(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config # config di Battleship
		self.row = self.config.row
		self.column = self.config.column

		#CONFIG FRAME
		super().__init__(parent) #parent -> container di Game
		self.configure(bg="#3589ad")
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		# virtual image
		self.virtual_image = tk.PhotoImage(width = 1, height = 1)

		self.create_header()
		self.create_button()
		# self.create_quit_button()

	def create_header(self):
		frame_h = 2*self.config.height//3 -99

		self.header_frame = tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h)
		self.header_frame.pack(fill = "x")

		self.header_label = tk.Label(self.header_frame, bg = "#3589ad", fg = "white", text = "game mode", font = ("Comic Sans MS", 42, "bold"), image = self.virtual_image, compound = "c", height = frame_h )
		self.header_label.grid(row = 0, column = 0)

		self.header_frame.grid_columnconfigure(0, weight = 1)
		self.header_frame.grid_rowconfigure(0, weight = 1)

	def create_button(self):
		frame_h = self.config.height//2

		self.button_frame = tk.Frame(self, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.button_frame.pack(fill = "x")

		self.multi_button_frame = tk.Frame(self.button_frame, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.multi_button_frame.pack()


		self.multi_button = tk.Button(self.multi_button_frame, text = "multiplayer",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 13), width = 14, command = self.game.multi_game) #lambda:self.game.next_page()
		self.multi_button.grid(row = 0, column = 0, sticky = "nsew", padx = 24, pady = 15)

		self.comp_button_frame = tk.Frame(self.button_frame, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.comp_button_frame.pack()

		self.comp_button = tk.Button(self.comp_button_frame, text = "with computer",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 13), width = 14, command = self.game.pc_game)
		self.comp_button.grid(row = 0, column = 0, sticky = "nsew", padx = 24, pady = 15)

		self.back_button_frame = tk.Frame(self.button_frame, bg = "#3589ad", width = self.config.width, height = frame_h//2)
		self.back_button_frame.pack()

		self.back_button = tk.Button(self.back_button_frame, text = "back",  bg = "#dbc225", fg = "white", font = ("Comic Sans MS", 13), width = 14, command = self.game.back_page)
		self.back_button.grid(row = 0, column = 0, sticky = "nsew", padx = 24, pady = 15)