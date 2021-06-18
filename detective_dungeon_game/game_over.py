import pygame
import sys
import random
from pygame.locals import *
from sys import argv
from datetime import datetime
import time

from settings.settings import Settings
from aset.menu_button import Button
from game_engine.save import Save

class GameOver():

	def __init__(self,Game):
		pygame.init()
		self.settings = Settings()

		self.error = True
		self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		self.title = pygame.display.set_caption(self.settings.title)
		self.stats =  Game.stats
		self.main = Game

		#resource class
		self.menu_button = Button(self)
		self.saving_data = Save(self)

	#checking event
	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_button_click(mouse_pos)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_p:
			self.stats.start = True
			self.main.run_game()

	#pressing button method
	def _check_button_click(self, mouse_pos):
		if self.button.rect_text17.collidepoint(mouse_pos):
			self.stats.start = False
		elif self.button.rect_text18.collidepoint(mouse_pos):
			self.error = False
			self.main.gameover = False
			#self.stats.reset_statistics()
			self.main.reset_game()
			self.main.run_game()


	def game_over_sound(self):
		gameover = pygame.mixer.Sound("sound effects/gameover.wav")
		gameover.set_volume(0.1)
		gameover.play()


	#running game
	def run_game(self):
		while self.error:
			self.check_event()
			self.update_frame()

	def update_frame(self):
		if self.gameover == True:
			self.game_over_sound()
			self.button.draw_game_over()
		pygame.display.flip()


if __name__ == "__main__":
	the_game =Pause()
	the_game.run_game()
