import pygame

class Door_triger:

	def __init__(self, Game):
		self.settings = Game.settings

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.door = pygame.image.load("img/door.png")
		self.door_rect = self.door.get_rect()
		self.door = pygame.transform.smoothscale(self.door, (2*self.door_rect.width, 2*self.door_rect.height))

		self.door_rect.center = self.screen_rect.center
		self.door_rect.y -= 124
		self.door_rect.x -= 10

	def draw(self):
		self.screen.blit(self.door, self.door_rect)
		#print(self.door_rect) #220, 170