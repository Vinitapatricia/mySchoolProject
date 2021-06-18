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

class Pause():

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
		if self.menu_button.rect_resume.collidepoint(mouse_pos):
			self.stats.start = True
			self.main.run_game()
		elif self.menu_button.rect_reset.collidepoint(mouse_pos):
			self.stats.start = True
			self.main.reset_game()
			self.main.run_game()
			print("reset")

		elif self.menu_button.rect_quitnsave.collidepoint(mouse_pos):
			self.saving_data.saving()
			self.error = False
			self.stats.start = False

	#running game
	def run_game(self):
		while self.error:
			self.check_event()
			self.update_frame()

	def update_frame(self):
		if self.error:
			self.menu_button.draw_pause_button()
		pygame.display.flip()


if __name__ == "__main__":
	the_game =Pause()
	the_game.run_game()
