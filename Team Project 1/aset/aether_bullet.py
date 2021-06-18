import pygame
from pygame.sprite import Sprite
from datetime import datetime

class AetherBullet(Sprite):

	def __init__(self, Game):
		super().__init__()
		self.screen = Game.screen
		self.settings = Game.settings
		self.color = self.settings.bullet_color
		self.radius = self.settings.bullet_radius
		self.aether_game = Game.aether_game

		self.rect = pygame.Rect(0,0, self.radius, self.radius)

		self.rect.center = self.aether_game.image_rect.center

		self.x = self.rect.x
		self.y = self.rect.y
		self.shooting = False
		self.start_time = False
		self.direction = None

	def set_direction(self):
		if self.aether_game.image == self.aether_game.right:
			self.direction = "right"

		elif self.aether_game.image == self.aether_game.left:
			self.direction = "left"

		elif self.aether_game.image == self.aether_game.front:
			self.direction = "front"

		elif self.aether_game.image == self.aether_game.back:
			self.direction = "back"

		elif self.aether_game.image:
			self.direction = "front"

	def update(self):
		if self.shooting == True:

			if self.direction == "right":
				self.x += self.settings.bullet_speed
				self.rect.x = self.x

			elif self.direction == "left":
				self.x -= self.settings.bullet_speed
				self.rect.x = self.x

			elif self.direction == "front":
				self.y += self.settings.bullet_speed
				self.rect.y = self.y

			elif self.direction == "back":
				self.y -= self.settings.bullet_speed
				self.rect.y = self.y



	def draw_bullet(self):
		pygame.draw.circle(self.screen, self.color,[self.x, self.y], self.radius)