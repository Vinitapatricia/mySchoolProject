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
from main import Dungeon
from game_engine.statistics import Statistics

class HowToPlay():

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
		self.screen_rect = self.screen.get_rect()
		self.title = pygame.display.set_caption(self.settings.title)

		self.page = 1
		self.exit = False

	def book_effect(self):
		bookeffect = pygame.mixer.Sound("sound effects/book effect.wav")
		bookeffect.set_volume(0.1)
		bookeffect.play()
	

	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_button_click(mouse_pos)


	def _check_button_click(self, mouse_pos):
		if self.next_rect.collidepoint(mouse_pos):
			self.book_effect()
			time.sleep(0.5)
			self.page += 1
			self.check_next()
			print(self.page)
		elif self.before_rect.collidepoint(mouse_pos):
			self.book_effect()
			time.sleep(0.5)
			self.page -= 1
			self.check_next()
			print(self.page)
			"""
		elif self.exit2_rect.collidepoint(mouse_pos):
			self.exit = True
			self.page = 0
			self.check_next()
			print(self.page)
			"""
		elif self.exit_rect.collidepoint(mouse_pos):
			self.book_effect()
			time.sleep(0.5)
			self.exit = True
			self.check_next()
			print(self.page)



	def _check_keydown_events(self, event):
		if event.key == pygame.K_ESCAPE:
			self.menu_pause.run_game()
		elif event.key == pygame.K_RIGHT:
			self.book_effect()
			time.sleep(0.5)
			self.page += 1
			self.check_next()
			print(self.page)
		elif event.key == pygame.K_LEFT:
			self.book_effect()
			time.sleep(0.5)
			self.page -= 1
			self.check_next()
			print(self.page)


	#running game
	def run_game(self):
		while self.error:
			self.check_event()
			self.update_frame()

	def update_frame(self):
		if self.page == 1:
			self.moving_page()
			self.draw_next()
			self.draw_before()
		elif self.page == 2:
			self.draw_frame2()
			self.draw_next()
			self.draw_before()
		elif self.page == 3:
			self.draw_frame3()
			self.draw_next()
			self.draw_before()
		elif self.page == 4:
			self.draw_frame4()
			self.draw_next()
			self.draw_before()
		elif self.page == 5:
			self.draw_frame5()
			self.draw_next()
			self.draw_before()
		elif self.page == 6:
			self.draw_frame6()
			self.draw_before()
			self.draw_exit()
			

		pygame.display.flip()
	#frame or page
	def moving_page(self):
		self.page_1 = pygame.image.load("img/TUTORIAL/Tutorial page 1.png")
		self.page_1 = pygame.transform.smoothscale(self.page_1, (self.settings.screen_width, self.settings.screen_height))
		self.page_1_rect = self.page_1.get_rect()
		self.page_1_rect.center = self.screen_rect.center
		self.screen.blit(self.page_1, self.page_1_rect)

	def  draw_next(self):
		self.button_font = pygame.font.SysFont("centuryschoolbook", 40)
		self.next = self.button_font.render("NEXT", 1, (255, 255, 255))
		self.screen.blit(self.next, (810, 480))

		self.next_rect =  pygame.Rect(810, 480, 250,60)
		#pygame.draw.rect(self.screen, (123,33,22), self.next_rect)

	def draw_frame2(self):
		self.frame2 = pygame.image.load("img/TUTORIAL/Tutorial page 2.png")
		self.frame2_rect = self.frame2.get_rect()
		self.frame2 = pygame.transform.scale(self.frame2,(self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.frame2,(0,0))

	def draw_frame3(self):
		self.frame3 = pygame.image.load("img/TUTORIAL/Tutorial page 3.png")
		self.frame3_rect = self.frame3.get_rect()
		self.frame3 = pygame.transform.scale(self.frame3,(self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.frame3,(0,0))

	def draw_frame4(self):
		self.frame4 = pygame.image.load("img/TUTORIAL/Tutorial page 4.png")
		self.frame4_rect = self.frame4.get_rect()
		self.frame4 = pygame.transform.scale(self.frame4,(self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.frame4,(0,0))

	def draw_frame5(self):
		self.frame5 = pygame.image.load("img/TUTORIAL/Tutorial page 5.png")
		self.frame5_rect = self.frame5.get_rect()
		self.frame5 = pygame.transform.scale(self.frame5, (self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.frame5, (0,0))

	def draw_frame6(self):
		self.frame6 = pygame.image.load("img/TUTORIAL/Tutorial las page.png")
		self.frame6_rect = self.frame6.get_rect()
		self.frame6 = pygame.transform.scale(self.frame6, (self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.frame6, (0,0))

	def draw_before(self):
		
		if self.page == 1:
			self.before = self.button_font.render("EXIT", 1, (255, 255, 255))
		else:
			self.before = self.button_font.render("PREVIOUS", 1, (255, 255, 255))
		self.screen.blit(self.before, (0, 480))

		self.before_rect =  pygame.Rect(0, 480, 250,60)
	#	pygame.draw.rect(self.screen, (25,12,61), self.before_rect)

	def draw_exit(self):
		self.exit = self.button_font.render("EXIT", 1, (255, 255, 255))
		self.screen.blit(self.exit, (810, 480))

		self.exit_rect = pygame.Rect(810, 480, 250,60)

	def draw_exit2(self):
		self.exit2 = self.button_font.render("EXIT", 1, (255, 255, 255))
		self.screen.blit(self.exit2, (0, 480))

		self.exit2_rect = pygame.Rect(0, 480, 250,60)
		#pygame.draw.rect(self.screen, (25,12,14), self.exit2_rect)

	def check_next(self):
		if self.page > 6:
			self.page = 0
		if self.page == 0:
			self.error = False
			self.page = 1

if __name__ == "__main__":
	the_game =HowToPlay()
	the_game.run_game()
