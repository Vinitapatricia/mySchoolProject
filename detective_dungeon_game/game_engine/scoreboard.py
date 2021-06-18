import pygame.font

class ScoreBoard:

	def __init__(self, Game):
		self.settings = Game.settings
		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = Game.stats
		self.pause_logo = Game.button
		self.pause_logo_rect = self.pause_logo.pause_rect
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 25)

		#method
		self._level_()
		self._score_()
		self._avatar_()

	def _level_(self):
		#general level
		level_str = (f"Floor : {self.stats.level}")
		self.level_image = self.font.render(level_str, True, self.text_color)
		print("a",self.stats.level)

		#placing level
		self.level_rect = self.level_image.get_rect()
		self.level_rect.midtop = self.screen_rect.midtop
		self.level_rect.top = 10

		#making score
	def _score_(self):
		#general score
		score_rounded = round(self.stats.score, -1)
		score_str = "{:,}".format(score_rounded)
		score_written = (f"Score : {score_str}")
		self.score_image = self.font.render(score_written, True, self.text_color)

		#placing score
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = self.screen_rect.left + 10
		self.score_rect.top = 30

	#making avatar
	def _avatar_(self):
		self.avatar = pygame.image.load("img/avatar.png")
		self.avatar_rect = self.avatar.get_rect()
		self.avatar = pygame.transform.scale(self.avatar, (self.avatar_rect.width -7, self.avatar_rect.height-7))
		self.avatar_rect.topright = self.screen_rect.topright

	def draw_stats(self):
		#self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.avatar, self.avatar_rect)
		self.screen.blit(self.level_image, self.level_rect)

	#making heal item available
	def available_heal(self):
		self.heal = pygame.image.load("img/heal_latar.png")
		self.heal_rect = self.heal.get_rect()

		self.heal_rect.topleft = self.screen_rect.topleft
		self.heal_rect.y += self.pause_logo_rect.height + 5

		self.label_color = (255, 255, 255)
		self.label_rect = pygame.Rect(15,(self.heal_rect.y + 10), (self.heal_rect.x + 120), (self.heal_rect.y - 30))

		self.picture = pygame.image.load("img/plus_trans.png")
		self.picture_rect = self.picture.get_rect()
		self.picture_rect.midright = self.label_rect.midright
		self.picture_rect.x += 8

		self.button_font = pygame.font.SysFont("centuryschoolbook", 20)
		self.number_heal = self.stats.heal_left
		self.number_text = self.button_font.render(f"{self.number_heal}", 1, (0, 0, 0))

		pygame.draw.rect(self.screen, self.label_color, self.label_rect)
		self.screen.blit(self.heal, self.heal_rect)
		self.screen.blit(self.picture, self.picture_rect)
		self.screen.blit(self.number_text, (75, 65))