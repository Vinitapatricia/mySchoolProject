import pygame

class Platform:

	def __init__(self, Game):
		self.settings = Game.settings

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.floor = pygame.image.load("img/lantai_finish.png")
		self.floor = pygame.transform.smoothscale(self.floor, (14*self.settings.base_floor, 9*self.settings.base_floor))
		self.floor_rect = self.floor.get_rect()

		self.floor_rect.top = self.screen_rect.top
		self.floor_rect.y -= 85
		self.floor_rect.x -= 98
		self.x = self.floor_rect.x
		self.y = self.floor_rect.y


	def rect(self):
		self.floor_rect = self.floor.get_rect()

	def draw(self):
		self.screen.blit(self.floor, self.floor_rect)