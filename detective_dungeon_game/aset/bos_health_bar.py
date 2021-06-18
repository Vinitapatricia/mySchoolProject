import pygame


class BosHealthBar:

	def __init__(self, Game):
		self.settings = Game.settings
		self.screen = Game.screen
		self.color = self.settings.bos_health_color
		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()
		self.width = 150

		self.rect = pygame.Rect(0,0, self.width, self.settings.bos_health_height)
		self.rect_ = pygame.Rect(0,0, 156, 11)

		self.rect.midtop = self.screen_rect.midtop
		self.rect.y += 34

		self.rect_.midtop = self.screen_rect.midtop
		self.rect_.y += 31

	def shoot(self):
		if self.settings.bos_hp >= 100:
			self.width = 150

		elif self.settings.bos_hp == 85:
			self.width = 128.6

		elif self.settings.bos_hp == 70:
			self.width = 107.2

		elif self.settings.bos_hp == 55:
			self.width = 85.8
		elif self.settings.bos_hp == 40:
			self.width = 64.4

		elif self.settings.bos_hp == 25:
			self.width = 43

		elif self.settings.bos_hp == 10:
			self.width = 21.6
		else:
			self.width = 0


	def draw(self):
		pygame.draw.rect(self.screen, [255,255,255], (self.settings.screen_width - 556, 32, 154, 9),3)
		pygame.draw.rect(self.screen, self.color, (self.settings.screen_width - 554, 34, self.width, 5))