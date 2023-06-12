import tkinter as tk
import sys
import time
from tkinter import messagebox as Msg
from random import randint

from config import Config
from game_stat import GameStats
from board import Board
from ship import Ship
from player import Player
from menu_page import MenuPage
from mode_page import ModePage
from board_computer import BoardComputer
from computer_page import ComputerPage


class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config #Batteship

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)
		self.resizable(0,0)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_mode_page()
		self.create_computer_page()
		self.create_menu_page()

	def create_container(self):
		self.containter = tk.Frame(self, bg="white")
		self.containter.pack(fill="both", expand=True)

	def create_mode_page(self):
		self.pages['mode_page'] = ModePage(self.containter, self.game)

	def create_menu_page(self):
		self.pages['menu_page'] = MenuPage(self.containter, self.game)

	def create_board(self):
		self.pages['board'] = Board(self.containter, self.game)

	def create_computer_page(self):
		self.pages['computer_page'] = ComputerPage(self.containter, self.game)



class TicTacToe:

	def __init__(self):
		self.start = True
		self.multi = False
		self.pc = False
		self.player_clicked = False
		self.player_x = False
		self.player_o = False

		self.game_stat = GameStats()
		self.config = Config()
		#self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

		self.clicked_counter = 1
		self.rndm_count = 0
		self.page_count = 0
		self.full = []
		self.x_list = []
		self.o_list = []
		self.computer_list = []

	def is_button_board_clicked(self, pos_x, pos_y):
		self.game_sign()
		fill = [pos_x, pos_y]

		isExist = False

		for i in self.full:
			if i == fill:
				isExist = True


		if isExist == False and self.start == True and self.multi == True:
			self.clicked_counter +=1
			self.game_sign()
			self.player.current_location(pos_x,pos_y)

			if self.clicked_counter % 2 == 0:
				self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].x_img_btn)
				self.x_list.append(fill)
				self.full.append(fill)
				self.check_win("Player 1", self.x_list)
				
				
			else:
				self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].o_img_btn)
				self.o_list.append(fill)
				self.full.append(fill)
				self.check_win("Player 2", self.o_list)
				

		elif isExist == False and self.start == True and self.pc == True and self.player_clicked == True:
			self.player_clicked = False
			
			self.player.current_location(pos_x,pos_y)

			if self.player_x == True and self.player_o == False:
				self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].x_img_btn)
				self.x_list.append(fill)
				self.full.append(fill)
				self.check_win("Player 1", self.x_list)

			elif self.player_x == False and self.player_o == True:
				self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].o_img_btn)
				self.o_list.append(fill)
				self.full.append(fill)
				self.check_win("Player 1", self.o_list)

			self.pc_turn()
			
	def pc_turn(self):

		self.random_pos()
		fill = self.pc_post
		
		pos_x = fill[0]
		pos_y = fill[1]
	

		isExist = False
		for i in self.full:
			if i == fill:
				isExist = True
				
		

		if isExist == False and self.start == True:
			print(fill)

			if self.player_x == False and self.player_o == True:
				self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].x_img_btn)
				self.computer_list.append(fill)
				self.full.append(fill)
				self.check_win("Computer", self.computer_list)

			elif self.player_x == True and self.player_o == False:
				self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].o_img_btn)
				self.computer_list.append(fill)
				self.full.append(fill)
				self.check_win("Computer", self.computer_list)

			self.player_clicked = True


		elif isExist == True and self.start == True:
			self.pc_same()

	def pc_same(self):
		self.rndm_count += 1
		self.pc_turn()

	def random_pos(self):
		
		if self.player_x == True:
			list_ = self.x_list
		else:
			list_ = self.o_list


		if len(list_ ) >=3:
			for i in range(0, len(list_)):
				for j in range(i+1, len(list_)):
					for k in range(j+1, len(list_)):
						tmp = [list_[i],list_[j],list_[k]]
						tmp.sort()

						if tmp == [[0,0],[0,1]] :
							self.pc_post = [0,2]

						elif tmp == [[0,0],[0,2]] :
							self.pc_post = [0,2]

						elif tmp == [[0,1],[0,2]] :
							self.pc_post = [0,0]

						elif tmp == [[1,0],[1,1]] :
							self.pc_post = [1,2]

						elif tmp == [[1,0],[1,2]] :
							self.pc_post = [1,1]

						elif tmp == [[1,1],[1,2]] :
							self.pc_post = [1,0]

						elif tmp == [[2,0],[2,1]] :
							self.pc_post = [2,2]

						elif tmp == [[2,0],[2,2]] :
							self.pc_post = [2,1]

						elif tmp == [[2,1],[2,2]] :
							self.pc_post = [2,0]

						elif tmp == [[0,0],[1,1]] :
							self.pc_post = [2,2]

						elif tmp == [[0,0],[2,2]] :
							self.pc_post = [1,1]

						elif tmp == [[1,1],[2,2]] :
							self.pc_post = [0,0]

						elif tmp == [[0,2],[1,1]] :
							self.pc_post = [2,0]

						elif tmp == [[0,2],[2,0]] :
							self.pc_post = [1,1]

						elif tmp == [[1,1],[2,0]] :
							self.pc_post = [0,2]

						elif tmp == [[0,0],[1,0]] :
							self.pc_post = [2,0]

						elif tmp == [[0,0],[2,0]] :
							self.pc_post = [1,0]

						elif tmp == [[1,0],[2,2]] :
							self.pc_post = [0,0]

						elif tmp == [[0,1],[1,1]] :
							self.pc_post = [2,1]

						elif tmp == [[0,1],[2,1]] :
							self.pc_post = [1,1]

						elif tmp == [[1,1],[2,1]] :
							self.pc_post = [0,1]

						elif tmp == [[0,2],[1,2]] :
							self.pc_post = [2,2]

						elif tmp == [[0,2],[2,2]] :
							self.pc_post = [1,2]

						elif tmp == [[1,2],[2,2]] :
							self.pc_post = [0,2]

						else:
							random_x = randint(0, self.config.row-1)
							random_y = randint(0, self.config.column -1)
							self.pc_post = [random_x, random_y]

		else:
			if self.rndm_count == 0:
				self.pc_post = [1,1]
			elif self.rndm_count == 1:
				tmp_list = [[0,0],[2,0],[0,2],[2,2]]
				rndm = randint(0, len(tmp_list) -1)
				self.pc_post = tmp_list[rndm]

	def game_sign(self):
		if self.multi == True:
			if self.clicked_counter % 2 == 0 and self.start == True:
				self.window.pages['board'].sign_label.configure(text = "Player 2's turn")
				
			else:
				if self.start == True:
					self.window.pages['board'].sign_label.configure(text = "Player 1's turn")

		elif self.pc == True:
			self.window.pages['board'].sign_label.configure(text = "Player 1's turn")
					
	def winner(self, player, list_):
		self.tmp = []
		

		for i in range(0, len(list_)):
			for j in range(i+1, len(list_)):
				for k in range(j+1, len(list_)):
					self.tmp = [list_[i],list_[j],list_[k]]
					self.tmp.sort()
		
					if self.tmp  == [[0,0],[0,1],[0,2]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[1,0],[1,1],[1,2]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[2,0],[2,1],[2,2]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[0,0],[1,1],[2,2]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[0,2],[1,1],[2,0]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[0,0],[1,0],[2,0]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[0,1],[1,1],[2,1]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break

					elif self.tmp == [[0,2],[1,2],[2,2]]:
						list_ = []
						Msg.showinfo("Winner", f"{player} Won The Match")
						self.window.pages['board'].sign_label.configure(text = f"{player} WON")
						self.start = False
						self.winner_game = True
						break
					
	def check_win(self, player, list_):
		
		self.full.sort()

		self.winner_game = False

		self.winner(player, list_)

		if self.full == self.config.card_list and self.winner_game == False:
			list_ = []
			Msg.showinfo("Tie Game", "TIE")
			self.window.pages['board'].sign_label.configure(text = f"TIE")
			self.start = False

	def multi_game(self):
		self.multi = True
		self.pc = False
		self.next_page()

	def choose_x(self):
		self.window.pages['computer_page'].x_button.configure(bg = "#bd443a")
		self.window.pages['computer_page'].o_button.configure(bg = "#dbc225")

		self.window.pages['board'].info_label1.configure(text = "Player 1 : X" )
		self.window.pages['board'].info_label2.configure(text = "Computer : O" )

		self.player_x = True
		self.player_o = False

	def choose_o(self):
		self.window.pages['computer_page'].o_button.configure(bg = "#bd443a")
		self.window.pages['computer_page'].x_button.configure(bg = "#dbc225")

		self.window.pages['board'].info_label1.configure(text = "Player 1 : O" )
		self.window.pages['board'].info_label2.configure(text = "Computer : X" )

		self.player_o = True
		self.player_x = False

	def pc_game(self):
		self.pc= True
		self.multi = False
		self.player_clicked = True
		self.next_page()

	def quit_game(self):
		sys.exit()

	def resart_game(self):
		for fill in self.full:
			for pos_x in fill:
				for pos_y in fill:
					self.window.pages['board'].button_board[pos_x][pos_y].configure(image = self.window.pages['board'].init_img_btn)
		self.window.pages['board'].sign_label.configure(text = "Player 1's turn")


		self.start = True
		self.player_clicked = True
		self.clicked_counter = 1
		self.rndm_count = 0
		self.full = []
		self.x_list = []
		self.o_list = []
		self.computer_list = []

	def next_page(self):
		self.page_count += 1
		if self.multi == True:
			self.page_count +=1

		self.change_page()

	def next_pc_page(self):
		self.pc = True
		self.multi = False
		self.page_count += 1
		self.change_page()

	def back_page(self):
		self.page_count -= 1
		if self.pc == True:
			self.pc = False
			self.multi = False

		if self.multi == True:
			self.page_count -=1
			self.multi = False
		 	
		self.change_page()


	def change_page(self):
		if self.page_count == 0:
			page = self.window.pages["menu_page"]
			page.tkraise()

		elif self.page_count == 1:
			page = self.window.pages["mode_page"]
			page.tkraise()

		elif self.page_count == 2:
			page = self.window.pages["computer_page"]
			page.tkraise()

		elif self.page_count == 3:
			self.resart_game()
			page = self.window.pages["board"]
			page.tkraise()

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	game = TicTacToe()
	game.run()