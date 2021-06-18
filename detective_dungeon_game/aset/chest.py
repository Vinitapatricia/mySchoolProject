import pygame
from random import randint
from random import choice
import string

class Chest():

	def __init__(self, Game):
		self.settings = Game.settings

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.chest_open = False
		self.take = False

		self.floor = pygame.image.load("img/lantai_finish.png")
		self.floor = pygame.transform.smoothscale(self.floor, (14*self.settings.base_floor, 9*self.settings.base_floor))
		self.floor_rect = self.floor.get_rect()

		self.floor_rect.top = self.screen_rect.top
		self.floor_rect.y -= 85
		self.floor_rect.x -= 85
		self.floor_x = self.floor_rect.x
		self.floor_y = self.floor_rect.y

		self.chest_closed = pygame.image.load("img/chest/chest_closed.png")
		self.chest_closed_rect= self.chest_closed.get_rect()

		self.chest_closed_rect.x=randint( self.floor_x +  265, self.floor_x + 815)
		self.chest_closed_rect.y = randint(self.floor_y + 265, self.floor_y + 475)

	#	self.chest_closed_rect.x= self.floor_x + 815
	#	self.chest_closed_rect.y = self.floor_y + 265

		self.chest_opened = pygame.image.load("img/chest/chest_opened.png")
		self.chest_opened_rect = self.chest_opened.get_rect()

		self.chest_opened_rect.center = self.chest_closed_rect.center

		self.token = pygame.image.load("img/token/gliding token.png")
		self.token_rect = self.token.get_rect()
		self.token = pygame.transform.scale(self.token, (3 * self.token_rect.width // 5, 3 * self.token_rect.height// 5))
		self.token_rect.center = self.chest_opened_rect.center

		self.choice()
		self.show_token_text()

	def draw_chest_c(self):
		self.screen.blit(self.chest_closed, self.chest_closed_rect)

		if self.chest_open == True:
			self.screen.blit(self.chest_opened, self.chest_opened_rect)
			self.screen.blit(self.token, self.token_rect)
			self.show_token_text()

		if self.take == True:
			self.screen.blit(self.chest_opened, self.chest_opened_rect)
			#self.take = False

	def show_token_text(self):
		self.token_font = pygame.font.SysFont("centuryschoolbook", 10)
		token = str(self.token_number)
		token_color = 255, 255, 255
		self.text_ = self.token_font.render(token , True, token_color)
		self.text_rect = self.text_.get_rect()

		self.text_rect.center = self.token_rect.center
		self.text_rect.x += 10

		self.screen.blit(self.text_, self.text_rect)

	def choice(self):
		number_list = [5,6,7,8,9,10,11,12,13,14,15]
		self.token_number = choice(number_list)
		print(self.token_number)