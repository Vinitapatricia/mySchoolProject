import pygame
from pygame.sprite import Sprite

class PyroBoss(Sprite):

	def __init__(self, Game):
		super().__init__()

		self.settings = Game.settings
		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("img/pyro_regisvine.png")
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center
		self.rect.y += 10