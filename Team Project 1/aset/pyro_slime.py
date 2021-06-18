import pygame
from pygame.sprite import Sprite

class PyroSlime(Sprite):

	def __init__(self, Game):
		super().__init__()

		self.screen = Game.screen
		self.player = Game.aether_game
		self.settings = Game.settings
		self.speed = self.settings.enemy_speed

		self.image = pygame.image.load("img/PyroSlime/standing (1).png")
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def update(self):
		speed = 0.5
		if self.rect.x > self.player.x:
			self.rect.x -= speed
		elif self.rect.x < self.player.x:
			self.rect.x += speed
		if self.rect.y > self.player.y + 50:
			self.rect.y -= speed
		elif self.rect.y < self.player.y + 17:
			self.rect.y += speed