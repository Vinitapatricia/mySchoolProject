import pygame

class HealthBar:

	def __init__(self, Game):
		self.settings = Game.settings
		self.screen = Game.screen
		self.stats = Game.stats
		#self.hp = self.stats.health_point
		self.player_shield_color = [255,255,255]
		#self.width = self.stats.health_point
		self.reset()

	def shield_bar(self):
		#display the graphic and track shield for the player
		if self.stats.health_point > 100 :
			self.player_shield_color = [0,255,43]
		elif self.stats.health_point > 75 :
			self.player_shield_color = [0,255,43]
		elif self.stats.health_point > 50 :
			self.player_shield_color = [247,255,0]
		elif self.stats.health_point <=0:
			self.stats.health_point = 0
		else:
			self.player_shield_color= [255,0,0]

	def reset(self):
		self.width = self.stats.health_point

	def draw(self): 
		pygame.draw.rect(self.screen, [255,255,255], ((self.settings.screen_width - 190), 29, 104, 24), 3)
		pygame.draw.rect(self.screen, self.player_shield_color, ((self.settings.screen_width - 188), 31, self.stats.health_point, 20))