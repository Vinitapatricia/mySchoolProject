#import pygame & system
import pygame
import sys
import random
from pygame.locals import *
from sys import argv
from datetime import datetime
import time 

#importing resources
from settings.main_settings import Settings
from aset.menu_button import Button
from main import Dungeon
from game_engine.load import Load
from game_engine.statistics import Statistics

class Data:

	def __init__(self):
		#starting engine
		pygame.init()
		self.settings = Settings()
		self.gameplay = Dungeon()
		self.stats = Statistics(self)

		self.error = True
		self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		self.title = pygame.display.set_caption(self.settings.title)

		#resource class
		self.menu_button = Button(self)
		self.load = Load(self)


	#making menu background
	def main_menu(self):
		self.background_menu = self.settings.bg
		self.background_menu = pygame.transform.smoothscale(self.background_menu, (self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.background_menu, (0,0))
		self.title_maker()

	
	#writing the title
	def title_maker(self):
		self.main_font = pygame.font.SysFont("centuryschoolbook", 80)
		self.text = self.main_font.render("Detective Dungeon", 1, (255, 255, 255)) 
		self.text_rect = self.text.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.text_rect.midtop = self.screen_rect.midtop
		self.text_rect.y += 50
		self.screen.blit(self.text, self.text_rect)

	def button_effect(self):
		buttoneffect = pygame.mixer.Sound("sound effects/button effect.wav")
		buttoneffect.set_volume(0.1)
		buttoneffect.play()
	
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
	
	#pressing button method
	def _check_button_click(self, mouse_pos):
		if self.menu_button.rect_new.collidepoint(mouse_pos):
			self.button_effect()
			time.sleep(0.5)
			self.gameplay.reset()
			self.gameplay.reset_game()
			self.gameplay.run_game()
		elif self.menu_button.rect_continue.collidepoint(mouse_pos):
			self.button_effect()
			time.sleep(0.5)
			self.gameplay.reset()
			# self.gameplay.checkpoint()
			# print("Done")
			self.gameplay.run_game()

		elif self.menu_button.rect_exit.collidepoint(mouse_pos):
			self.button_effect()
			time.sleep(0.5)
			self.error = False

	#reset 
	def reset(self):
		self.error = True

	#running game
	def run_game(self):
		while self.error:
			self.main_menu()
			self.check_event()
			self.update_frame()


	def update_frame(self):
		if self.error:
			self.menu_button.draw_choosing_data()
		pygame.display.flip()



if __name__ == "__main__":
	the_game =Start()
	the_game.run_game()