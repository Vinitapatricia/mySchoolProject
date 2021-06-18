import pygame
import sys

#from settings.settings import Settings
from aset.menu_button import Button
from aset.upgrade import Upgrade
from aset.token import Token

class Shop:

	def __init__(self, Game):
		#start pygame
		pygame.init()
		self.start = True
		self.settings = Game.settings
		self.stats = Game.stats

		#screen for shop
		self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		self.title = pygame.display.set_caption(self.settings.title)

		self.menu_button = Button(self)
		self.token = Token(self)
		self.upgrader = Upgrade(self)

	#making menu background
	def main_menu(self):
		self.background_menu = self.settings.shop_bg
		self.background_menu = pygame.transform.smoothscale(self.background_menu, (self.settings.screen_width, self.settings.screen_height))
		self.screen.blit(self.background_menu, (0,0))
		self.title_maker()

	#making the title
	def title_maker(self):
		self.main_font = pygame.font.SysFont("centuryschoolbook", 80)
		self.text = self.main_font.render("Market", 1, (255, 255, 255)) 
		self.text_rect = self.text.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.text_rect.midtop = self.screen_rect.midtop
		self.text_rect.y += 50
		self.screen.blit(self.text, self.text_rect)

	#checking event
	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_button_click(mouse_pos)

	def _check_button_click(self, mouse_pos):
		if self.upgrader.bg_attack_rect.collidepoint(mouse_pos) and self.stats.price_attack <= self.stats.token:
			self.coin_effect()
			self.stats.power_up += 2
			self.settings.bullet_hp += self.stats.power_up
			self.stats.power_up = 0
			self.stats.token -= self.stats.price_attack
			self.stats.price_attack += 100
			#print(self.stats.token)
			print(self.settings.bullet_hp)
		elif self.upgrader.bg_defense_rect.collidepoint(mouse_pos) and self.stats.price_defense <= self.stats.token:
			self.coin_effect()
			self.stats.defense_up += 1
			self.settings.slime_damage -= self.stats.defense_up
			self.stats.defense_up = 0
			self.stats.token -= self.stats.price_defense
			self.stats.price_defense += 100
			#print(self.stats.token)
			print(self.settings.slime_damage)
		elif self.upgrader.bg_capacity_rect.collidepoint(mouse_pos) and self.stats.price_hp <= self.stats.token:
			self.coin_effect()
			self.stats.max_hp += 10
			self.stats.health_point += self.stats.max_hp
			self.stats.max_hp = 0
			self.stats.token -= self.stats.price_hp
			self.stats.price_hp += 100
			#print(self.stats.token)
			print(self.stats.health_point)
		elif self.upgrader.exit_rect.collidepoint(mouse_pos):
			self.start = False
		else:
			print("Not enough token")

	def coin_effect(self):
		coin = pygame.mixer.Sound("sound effects/coin.wav")
		coin.set_volume(0.1)
		coin.play()


	def run_game(self):
		while self.start:
			self.main_menu()
			self.check_event()
			self.update_frame()

	def update_frame(self):
		if self.start:
			#self.menu_button.draw_button1()
			self.token.show_token()
			self.token.show_token_text()
			self.upgrader.draw_background()
			self.upgrader.draw_icon()
			self.upgrader.show_price()
			self.upgrader.show_statement()
			self.upgrader.draw_button()
		pygame.display.flip()

if __name__ == "__main__":
	shop = Shop()
	shop.run_game() 