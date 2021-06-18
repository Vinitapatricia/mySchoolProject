import pygame
from aset.chest import Chest

class Aether:

	def __init__(self, Game):
		self.settings = Game.settings

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("img/aether/standing.png")
		self.image_rect = self.image.get_rect()

		self.rect = self.image_rect

		#self.image_rect.center = self.screen_rect.center

		#self.x = float(self.image_rect.x)
		#self.y = float(self.image_rect.y)
		self.walkCount = 0

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.standing = True

		self.back = pygame.image.load("img/complete_aether/aether_belakang.png")
		self.left = pygame.image.load("img/complete_aether/aether_kiri.png")
		self.right = pygame.image.load("img/complete_aether/aether_kanan.png")
		self.front = pygame.image.load("img/aether/standing.png")
		self.stand = pygame.image.load("img/aether/standing.png")
		
		self.walkRight = [pygame.image.load('img/aether/R2.png'), pygame.image.load('img/aether/R3.png'), pygame.image.load('img/aether/R4.png'), pygame.image.load('img/aether/R5.png')]
		self.walkLeft = [pygame.image.load('img/aether/L2.png'), pygame.image.load('img/aether/L3.png'), pygame.image.load('img/aether/L4.png'), pygame.image.load('img/aether/L5.png')]
		self.WalkDown = [pygame.image.load('img/aether/D2.png'), pygame.image.load('img/aether/D3.png'), pygame.image.load('img/aether/D4.png')]
		self.WalkUp = [pygame.image.load('img/aether/U2.png'), pygame.image.load('img/aether/U3.png'), pygame.image.load('img/aether/U4.png')]

		self.floor = pygame.image.load("img/lantai_finish.png")
		self.floor = pygame.transform.smoothscale(self.floor, (14*self.settings.base_floor, 9*self.settings.base_floor))
		self.floor_rect = self.floor.get_rect()

		self.floor_rect.top = self.screen_rect.top
		self.floor_rect.y -= 85
		self.floor_rect.x -= 85
		self.floor_x = self.floor_rect.x
		self.floor_y = self.floor_rect.y

		self.chest = Chest(self)

		self.restart_position()

	def update(self):

		if self.moving_right and (self.image_rect.right < self.floor_x + 885):
			self.x += self.settings.aether_speed

		if self.moving_left and (self.image_rect.left > self.floor_x + 235): # + 255
			self.x -= self.settings.aether_speed

		if self.moving_up and (self.image_rect.top > self.floor_y + 225):
			self.y -= self.settings.aether_speed

		if self.moving_down and (self.image_rect.bottom < self.floor_y + 515) :
			self.y += self.settings.aether_speed

		self.image_rect.x = self.x
		self.image_rect.y = self.y

	def show_aether(self):
		if self.walkCount + 1 >= 14:
			self.walkCount = 0

		elif not(self.standing):
			if self.moving_left:
				self.screen.blit(self.walkLeft[self.walkCount//4], self.image_rect)
				self.walkCount += 1
				self.image = self.left

			elif self.moving_right:
				self.screen.blit(self.walkRight[self.walkCount//4], self.image_rect)
				self.walkCount += 1
				self.image = self.right

			elif self.moving_down:
				self.screen.blit(self.WalkDown[self.walkCount//5], self.image_rect)
				self.walkCount += 1
				self.image = self.front

			elif self.moving_up:
				self.screen.blit(self.WalkUp[self.walkCount//5], self.image_rect)
				self.walkCount += 1
				self.image = self.back

		elif self.standing:
			self.screen.blit(self.image, self.image_rect)
			#print(self.image_rect) #450 130

	def restart_position(self):
		self.image_rect.topleft = self.floor_rect.topleft
		self.rect.x = self.rect.x+ 235
		self.rect.y = self.rect.y +255

		self.x = float(self.image_rect.x)
		self.y = float(self.image_rect.y)