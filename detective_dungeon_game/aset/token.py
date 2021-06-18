import pygame

class Token():

	def __init__(self, Game):
		self.settings = Game.settings
		self.stats = Game.stats

		self.screen = Game.screen
		self.screen_rect = self.screen.get_rect()

		self.token = pygame.image.load("img/token/gliding token.png")
		self.token_rect = self.token.get_rect()
		self.token_rect.topleft = self.screen_rect.topleft

		self.show_token()

	def show_token(self):
		self.screen.blit(self.token, self.token_rect)

	def show_token_text(self):
		self.token_font = pygame.font.SysFont("centuryschoolbook", 30)
		token = str(self.stats.token)
		token_color = 255, 255, 255
		self.text = self.token_font.render(token , True, token_color)
		self.text_rect = self.text.get_rect()

		self.text_rect.topleft = self.screen_rect.topleft
		self.text_rect.x += 50

		self.screen.blit(self.text, self.text_rect)

