import pygame

class Upgrade:

	def __init__(self, Upgrade):
		self.settings = Upgrade.settings
		self.screen = Upgrade.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = Upgrade.stats
		self.token = Upgrade.token

		#upgrade physical attack
		self.attack = pygame.image.load("img/upgrader/damage_upgrade.png")
		self.attack_rect = self.attack.get_rect()
		self.attack = pygame.transform.scale(self.attack, (3*self.attack_rect.width//2, 3*self.attack_rect.height//2))

		#upgrade pyhsical and magic defense
		self.defense = pygame.image.load("img/upgrader/defense_upgrade.png")
		self.defense_rect = self.defense.get_rect()
		self.defense = pygame.transform.scale(self.defense, (3*self.defense_rect.width//2, 3*self.defense_rect.height//2))

		#upgrade health points' capacity
		self.capacity = pygame.image.load("img/upgrader/hp_upgrade.png")
		self.capacity_rect = self.capacity.get_rect()
		self.capacity = pygame.transform.scale(self.capacity, (3*self.capacity_rect.width//2, 3*self.capacity_rect.height//2))

		#background for upgrade
		self.bg_criteria = pygame.image.load("img/upgrader/latar_upgrade_tegak.png")
		self.bg_criteria_rect = self.bg_criteria.get_rect()

		#button for upgrade
		self.button = pygame.image.load("img/upgrader/button.png")
		self.button_rect = self.button.get_rect()

	def draw_background(self):
		#drawing background for pyschical attack upgrade
		self.bg_attack = self.bg_criteria
		self.bg_attack_rect = self.bg_attack.get_rect()
		self.bg_attack_rect.midleft = self.screen_rect.midleft
		self.bg_attack_rect.x += 90
		self.bg_attack_rect.y += 40

		#drawing background for defense upgrade
		self.bg_defense = self.bg_criteria
		self.bg_defense_rect = self.bg_defense.get_rect()
		self.bg_defense_rect.center = self.screen_rect.center
		self.bg_defense_rect.y += 40

		#drawing background for capacity upgrade
		self.bg_capacity = self.bg_criteria
		self.bg_capacity_rect = self.bg_capacity.get_rect()
		self.bg_capacity_rect.midright = self.screen_rect.midright
		self.bg_capacity_rect.y += 40
		self.bg_capacity_rect.x -= 90

		#drawing to the screen
		self.screen.blit(self.bg_attack, self.bg_attack_rect)
		self.screen.blit(self.bg_defense, self.bg_defense_rect)
		self.screen.blit(self.bg_capacity, self.bg_capacity_rect)

	def draw_icon(self):
		#draw icon for physical upgrade
		self.attack_rect.center = self.bg_attack_rect.center
		self.attack_rect.y -= 100
		self.attack_rect.x -= 5

		#draw icon for defense upgrade
		self.defense_rect.center = self.bg_defense_rect.center
		self.defense_rect.y -= 100
		self.defense_rect.x -= 3

		#draw icon for capacity upgrade
		self.capacity_rect.center = self.bg_capacity_rect.center
		self.capacity_rect.y -= 100
		self.capacity_rect.x -= 5

		#draw all icon
		self.screen.blit(self.attack, self.attack_rect)
		self.screen.blit(self.defense, self.defense_rect)
		self.screen.blit(self.capacity, self.capacity_rect)

	def draw_button(self):
		#draw button for physical upgrade
		self.attack_button = self.button
		self.attack_button_rect = self.attack_button.get_rect()
		self.attack_button_rect.midbottom = self.bg_attack_rect.midbottom
		self.attack_button_rect.y -= 30
		self.attack_button_rect.x += 3

		#draw button for defense upgrade
		self.defense_button = self.button
		self.defense_button_rect = self.defense_button.get_rect()
		self.defense_button_rect.midbottom = self.bg_defense_rect.midbottom
		self.defense_button_rect.y -= 30
		self.defense_button_rect.x += 3

		#draw button for capacity upgrade
		self.capacity_button = self.button
		self.capacity_button_rect = self.capacity_button.get_rect()
		self.capacity_button_rect.midbottom = self.bg_capacity_rect.midbottom
		self.capacity_button_rect.y -= 30
		self.capacity_button_rect.x += 3

		#draw button to exit
		self.exit = pygame.image.load("img/upgrader/silang.png")
		self.exit_rect = self.exit.get_rect()
		self.exit_rect.topright = self.screen_rect.topright

		#draw buttons
		self.screen.blit(self.attack_button, self.attack_button_rect)
		self.screen.blit(self.defense_button, self.defense_button_rect)
		self.screen.blit(self.capacity_button, self.capacity_button_rect)
		self.screen.blit(self.exit, self.exit_rect)

		#draw button text for each button
		self.button_font = pygame.font.SysFont("centuryschoolbook", 20)
		self.text = self.button_font.render("Upgrade", 1, (255, 255, 255))
		self.rect_attack = (163, 414)
		self.rect_defense = (443, 414)
		self.rect_capacity = (722, 414)

		#draw text
		self.screen.blit(self.text, self.rect_attack)
		self.screen.blit(self.text, self.rect_defense)
		self.screen.blit(self.text, self.rect_capacity)

	def show_price(self):
		self.token_font = pygame.font.SysFont("centuryschoolbook", 30)
		self.price_attack = self.stats.price_attack
		self.price_defense = self.stats.price_defense
		self.price_hp = self.stats.price_hp

		self.price_attack_token = str(self.stats.price_attack)
		token_color = 255, 255, 255
		self.text_attack = self.token_font.render(self.price_attack_token , True, token_color)
		self.text_rect_attack = self.text_attack.get_rect()
		self.text_rect_attack.center = self.bg_attack_rect.center
		self.text_rect_attack.x += 15
		self.text_rect_attack.y += 10

		self.price_defence_token = str(self.stats.price_defense)
		self.text_defense = self.token_font.render(self.price_defence_token , True, token_color)
		self.text_rect_defense = self.text_defense.get_rect()
		self.text_rect_defense.center = self.bg_defense_rect.center
		self.text_rect_defense.x += 20
		self.text_rect_defense.y += 10

		self.price_hp_token = str(self.stats.price_hp)
		self.text_hp = self.token_font.render(self.price_hp_token , True, token_color)
		self.text_rect_hp = self.text_hp.get_rect()
		self.text_rect_hp.center = self.bg_capacity_rect.center
		self.text_rect_hp.x += 17
		self.text_rect_hp.y += 10

		self.token1 = self.token.token
		self.token1_rect = self.token1.get_rect()
		self.screen.blit(self.token1, self.token1_rect)
		self.token2 = self.token.token
		self.token2_rect = self.token2.get_rect()
		self.screen.blit(self.token2, self.token2_rect)
		self.token3 = self.token.token
		self.token3_rect = self.token3.get_rect()
		self.screen.blit(self.token3, self.token3_rect)

		self.token1_rect.center = self.bg_attack_rect.center
		self.token1_rect.x -= 25
		self.token1_rect.y += 10
		self.token2_rect.center = self.bg_defense_rect.center
		self.token2_rect.x -= 20
		self.token2_rect.y += 10
		self.token3_rect.center = self.bg_capacity_rect.center
		self.token3_rect.x -= 23
		self.token3_rect.y += 10

		self.screen.blit(self.token1, self.token1_rect)
		self.screen.blit(self.token2, self.token2_rect)
		self.screen.blit(self.token3, self.token3_rect)

		self.screen.blit(self.text_attack, self.text_rect_attack)
		self.screen.blit(self.text_hp, self.text_rect_hp)
		self.screen.blit(self.text_defense, self.text_rect_defense)

	def show_statement(self):
		self.text_font = pygame.font.SysFont("centuryschoolbook", 20)
		self.color_text = 255, 255, 255
		self.attack_text = self.text_font.render("Attack : +2", True, self.color_text)
		self.attack_text_rect = self.attack_text.get_rect()
		self.attack_text_rect.center = self.bg_attack_rect.center
		self.attack_text_rect.y -= 30

		self.defense_text = self.text_font.render("Defense : +1", True, self.color_text)
		self.defense_text_rect = self.defense_text.get_rect()
		self.defense_text_rect.center = self.bg_defense_rect.center
		self.defense_text_rect.y -= 30

		self.hp_text = self.text_font.render("Max hp : +10", True, self.color_text)
		self.hp_text_rect = self.hp_text.get_rect()
		self.hp_text_rect.center = self.bg_capacity_rect.center
		self.hp_text_rect.y -= 30

		self.screen.blit(self.attack_text, self.attack_text_rect)
		self.screen.blit(self.defense_text, self.defense_text_rect)
		self.screen.blit(self.hp_text, self.hp_text_rect)