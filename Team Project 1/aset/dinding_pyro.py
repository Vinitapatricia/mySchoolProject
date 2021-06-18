import pygame

class Dinding_pyro:

	def __init__(self, Game):
		self.settings = Game.settings

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("img/dinding_pyro_regis.png")
		self.image_rect = self.image.get_rect()

		self.image = pygame.transform.smoothscale(self.image, (16*self.settings.base_wall, 9*self.settings.base_wall))
		self.image_rect = self.image.get_rect()

		self.image_rect.top = self.screen_rect.top
		self.image_rect.y -= 35
		self.image_rect.x -= 80


		self.x = self.image_rect.x
		self.y = self.image_rect.y

	def draw(self):
		self.screen.blit(self.image, self.image_rect)