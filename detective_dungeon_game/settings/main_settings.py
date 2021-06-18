import pygame

class Settings:

	def __init__(self):
		#game settings
		self.base_dimension = 60

		self.screen_width = 16 * self.base_dimension
		self.screen_height = 9 * self.base_dimension
		self.title = "Detective Dungeon"
		self.bg = pygame.image.load('img/data_choose.jpg')
		self.background_main = 243,243,243

