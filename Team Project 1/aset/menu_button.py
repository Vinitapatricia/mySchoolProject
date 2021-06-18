import pygame

class Button:

	def __init__(self, info_game):

		#searching how large the screen is
		self.screen = info_game.screen
		self.setting = info_game.settings
		self.screen_rect = info_game.screen.get_rect()

		#pause logo
		self.pause = pygame.image.load("img/pause.png")
		self.pause_rect = self.pause.get_rect()
		self.pause_rect.topleft = self.screen_rect.topleft
		self.pause_rect.x += 3
		self.pause_rect.y += 3

		#store logo
		self.store = pygame.image.load("img/shop/logo shop.png")
		self.store_rect = self.store.get_rect()
		self.store = pygame.transform.scale(self.store, (self.store_rect.width +5, self.store_rect.height+5))
		self.store_rect.topleft = self.screen_rect.topleft
		self.store_rect.x = 60
		self.store_rect.y = 6

		#about button
		self.color = (128, 128, 128) #174, 171, 171
		self.rect1 = pygame.Rect(360,200, 300, 60)

		#button 1
		self.button_font = pygame.font.SysFont("centuryschoolbook", 40)
		self.text = self.button_font.render("Start(x)", 1, (255, 255, 255))

		# button how to play
		self.text15 = self.button_font.render("How To Play", 1, (255, 255, 255))
		self.rect_how = pygame.Rect(360,300, 300, 60)

		#button 2
		self.rect3 = pygame.Rect(360,400, 300, 60)
		self.text3 = self.button_font.render("Quit(esc)", 1, (255, 255, 255))

		#button for changing size
		self.text5 = self.button_font.render("800 x 600", 1, (255, 255, 255))
		self.text6 = self.button_font.render("700 x 550", 1, (255, 255, 255))
		self.text7 = self.button_font.render("Fullscreen", 1, (255, 255, 255))

		#button for choosing data
		self.text8 = self.button_font.render("New Game", 1, (255, 255, 255))
		self.text9 = self.button_font.render("Continue", 1, (255, 255, 255))
		self.text10 = self.button_font.render("Back", 1, (255, 255, 255))

		self.rect_new = pygame.Rect(360,200, 250,60)
		self.rect_continue = pygame.Rect(360, 300, 250,60)
		self.rect_exit = pygame.Rect(360, 400, 250,60)

		#button for pause
		self.pause_font = pygame.font.SysFont("centuryschoolbook", 80)
		self.text11 = self.pause_font.render("Pause Game", 1, (255, 255, 255))
		self.text11_rect = self.text11.get_rect()
		self.text11_rect.midtop = self.screen_rect.midtop
		self.text11_rect.y +=  50

		self.text12 = self.button_font.render("Resume(p)", 1, (255, 255, 255))
		self.text13 = self.button_font.render("Reset", 1, (255, 255, 255))
		self.text14 = self.button_font.render("Quit And Save Game", 1, (255, 255, 255))

		self.rect_resume = pygame.Rect(366,190, 220,60)
		self.rect_reset = pygame.Rect(414,290, 130,60)
		self.rect_quitnsave = pygame.Rect(273, 390, 410,60)

		# button Game over
		self.game_font = pygame.font.SysFont("centuryschoolbook", 80)
		self.text16 = self.game_font.render("Game Over", 1, (255, 255, 255))
		self.text16_rect = self.text16.get_rect()
		self.text16_rect.center = self.screen_rect.center
		self.text16_rect.y -= 50
		self.text16_rect.x += 10
		
		self.text17 = self.button_font.render("Quit", 1, (255, 255, 255))
		self.text17_rect = self.text16.get_rect()
		self.text17_rect.center = self.screen_rect.center
		self.text17_rect.x += 50
		self.text17_rect.y += 40
		self.rect_text17 = pygame.Rect(313,265, 95,50)


		self.text18 = self.button_font.render("New Game", 1, (255, 255, 255))
		self.text18_rect = self.text16.get_rect()
		self.text18_rect.center = self.screen_rect.center
		self.text18_rect.x += 180
		self.text18_rect.y += 40
		self.rect_text18 = pygame.Rect(445,265, 215,50)

	def draw_button1(self):
		pygame.draw.rect(self.screen, self.color, self.rect1)
		self.screen.blit(self.text, (445, 205))
		pygame.draw.rect(self.screen, self.color, self.rect_how)
		self.screen.blit(self.text15, (395, 305))
		pygame.draw.rect(self.screen, self.color, self.rect3)
		self.screen.blit(self.text3, (430, 405))


	def draw_choosing_data(self):
		self.screen.blit(self.text8, (395, 205))
		self.screen.blit(self.text9, (400, 305))
		self.screen.blit(self.text10, (435, 405))

	def draw_pause_button(self):
		self.screen.blit(self.text11, self.text11_rect)
		self.screen.blit(self.text12, (381, 190))
		self.screen.blit(self.text13, (429, 290))
		self.screen.blit(self.text14, (283, 390))
		

	def draw_pause_logo(self):
		self.screen.blit(self.pause, self.pause_rect)

	def draw_store_logo(self):
		self.screen.blit(self.store, self.store_rect)

	def draw_game_over(self):
		self.screen.blit(self.text16, self.text16_rect)
	#	pygame.draw.rect(self.screen, self.color, self.rect_text17)
		self.screen.blit(self.text17, self.text17_rect)
	#	pygame.draw.rect(self.screen, self.color, self.rect_text18)
		self.screen.blit(self.text18, self.text18_rect)