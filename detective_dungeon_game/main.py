#importing pygame & system
import pygame
import sys
import time
from random import randint
from datetime import datetime

#import resources
from settings.settings import Settings
from game_engine.statistics import Statistics
from game_engine.scoreboard import ScoreBoard
from game_engine.load import Load
from aset.health_bar import HealthBar
from aset.aether import Aether
from aset.dinding import Dinding
from aset.platform import Platform
from aset.platform_pyro import Platform_pyro
from aset.dinding_pyro import Dinding_pyro
from aset.pyro_regis import PyroBoss
from aset.aether_bullet import AetherBullet
from aset.pyro_slime import PyroSlime
from aset.door_level import Door_triger
from aset.menu_button import Button 
from menu_pause import Pause
from shop import Shop
from aset.bos_health_bar import BosHealthBar
from aset.chest import Chest

class Dungeon:
	
	def __init__(self):
		#start pygame 
		pygame.init()
		pygame.mixer.init()
		self.error = False
		self.gameover = False
		self.spawn = 0
		self.settings = Settings()
		self.start_time = datetime.now()

		#showing screen 
		self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		self.title = pygame.display.set_caption(self.settings.title)
		self.background_menu = self.settings.bg
		self.background_menu = pygame.transform.smoothscale(self.background_menu, (self.settings.screen_width, self.settings.screen_height))

		# SINGLE OBJECT
		self.stats = Statistics(self)
		self.button = Button(self)
		self.scoreboard = ScoreBoard(self)
		self.saved_data = Load(self)
		self.health_bar = HealthBar(self)
		self.aether_game = Aether(self)
		self.dinding_game = Dinding(self)
		self.dinding_bos_pyro = Dinding_pyro(self)
		self.platform_bos_pyro = Platform_pyro(self)
		self.platform_game = Platform(self)
		self.level_upgrader = Door_triger(self)
		self.menu_pause = Pause(self)
		self.bos_bar = BosHealthBar(self)
		self.chest = Chest(self)
		self.shop = Shop(self)

		# SPRITE OBJECT
		self.aether_bullets = pygame.sprite.Group()
		self.pyro_slimes = pygame.sprite.Group()
		self.pyro_bos = pygame.sprite.Group()

		self._create_pyro_slime()
		self._create_pyro_boss()
		#self.music()


	#reset
	def reset(self):
		self.stats.start = True
		self.menu_pause.error = True

	#checkpoint
	def checkpoint(self):
		self.saved_data._load()
		self.scoreboard._level_()
		self._create_pyro_slime()
		print("q", self.stats.slime_number)
		#print(self.stats.level)

	#start engine
	def run_game(self):
		while self.stats.start:
			self.check_event()
			self.health_bar.shield_bar()
			self.update_slime()
			self.aether_bullet_update()
			self.update_frame()
			
	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_button_click(mouse_pos)

	#pressing button method
	def _check_button_click(self, mouse_pos):
		if self.button.pause_rect.collidepoint(mouse_pos):
			self.menu_pause.run_game()
		elif self.button.store_rect.collidepoint(mouse_pos):
			self.shop.start = True
			#self.check_koin()
			self.shop.run_game()
		elif self.chest.chest_closed_rect.collidepoint(mouse_pos):#and self.aether_game.rect <= self.chest.chest_opened_rect:
			self.chest_effect()
			time.sleep(0.5)
			self.chest.chest_open = True
			#self.chest.take = True
			#self.check_koin()
		elif self.scoreboard.picture_rect.collidepoint(mouse_pos) and self.stats.token >= 25:
			self.stats.heal_left += 1
			self.stats.token -= 25
		elif self.button.rect_text17.collidepoint(mouse_pos):
			self.stats.start = False
		elif self.button.rect_text18.collidepoint(mouse_pos):
			self.error = False
			self.gameover = False
			self.stats.reset_statistics()
			self.reset_game()
			self.run_game()

	# key down
	def _check_keydown_events(self, event):
		if event.key == pygame.K_ESCAPE:
			self.menu_pause.run_game()
		elif event.key == pygame.K_d:
			if self.gameover == False:
				self.aether_game.moving_right = True
				self.aether_game.standing = False

		elif event.key == pygame.K_a:
			if self.gameover == False:
				self.aether_game.moving_left = True
				self.aether_game.standing = False

		elif event.key == pygame.K_w:
			if self.gameover == False:
				self.aether_game.moving_up = True
				self.aether_game.standing = False

		elif event.key == pygame.K_s:
			if self.gameover == False:
				self.aether_game.moving_down = True
				self.aether_game.standing = False

		elif event.key == pygame.K_SPACE:
			if self.gameover == False:
				self.new_aether_bullet()
				self.aether_game.standing = True
				self.shot_effect()

		elif event.key == pygame.K_SLASH and self.aether_game.rect.y <= self.level_upgrader.door_rect.bottom:
			if self.gameover == False:
				if len(self.pyro_slimes) == 0 and self.stats.bos_number == 0:
					self.spawn += 1
					if self.spawn % 4 == 2 and self.stats.level > 2:
						self.reset_stats_boss()
					self.open_door()
					time.sleep(0.1)
					self.check_slime_empty()
					self.aether_game.restart_position()
					self.chest.chest_open = False
					self.chest.take = False
					self.chest.choice()
					print("done")
				else:
					print("Kill all the enemy to procide")
				
		elif event.key == pygame.K_p:
			self.pause_game()
		elif event.key == pygame.K_h:
			if self.stats.heal_left > 0:
				self.stats.heal_left -= 1
				self.stats.health_point += 15
				self.health_bar.width += 15
				self.health_bar.shield_bar()
			print(self.stats.health_point)

		elif event.key == pygame.K_o: #and self.aether_game.rect <= self.chest.chest_opened_rect:
			if self.chest.chest_open == True and self.chest.take == False:
				self.coin_effect()
				time.sleep(0.1)
				self.chest.take = True
				self.check_koin()

		
	# key up
	def _check_keyup_events(self, event):
		if event.key == pygame.K_d:
			self.aether_game.moving_right = False
			self.aether_game.standing = True

		elif event.key == pygame.K_a:
			self.aether_game.moving_left = False
			self.aether_game.standing = True

		elif event.key == pygame.K_w:
			self.aether_game.moving_up = False
			self.aether_game.standing = True

		elif event.key == pygame.K_s:
			self.aether_game.moving_down = False
			self.aether_game.standing = True

	def update_frame(self):
		self.screen.blit(self.background_menu, (0,0))
		self.platform_game.draw()
		self.dinding_game.draw()
		if self.stats.level % 4 == 1 and self.stats.level > 1:
			self.stats.bos_number += 1
			self.platform_bos_pyro.draw()
			self.dinding_bos_pyro.draw()
			self.shooting_boss()
			self.pyro_bos.draw(self.screen)
			self.bos_bar.draw()
			if self.settings.bos_hp == 0:
				self.stats.bos_number = 0
		self.button.draw_pause_logo()
		self.button.draw_store_logo()
		self.scoreboard.available_heal()
		self.level_upgrader.draw()
		self.health_bar.draw()
		self.scoreboard.draw_stats()
		self.shooting_slime()
		
		self.pyro_slimes.draw(self.screen)
		if len(self.pyro_slimes) == 0:
			self.chest.draw_chest_c()
			#self.chest.choice()
			#self.check_koin()
		if self.gameover == True:
			self.game_over_sound()
			self.button.draw_game_over()
		if self.aether_game.standing == False:
			self.walk_effect()

		self.aether_game.show_aether()
		for bullet in self.aether_bullets.sprites():
			bullet.draw_bullet()

		pygame.display.flip()

	#soundtrack
	def music(self):
		pygame.mixer.music.load("sound effects/background_music.mp3")
		pygame.mixer.music.play(-1, 0.0)

	def game_over_sound(self):
		gameover = pygame.mixer.Sound("sound effects/gameover.wav")
		gameover.set_volume(0.01)
		gameover.play()

	def shot_effect(self):
		shoteffect = pygame.mixer.Sound("sound effects/shot.wav")
		shoteffect.set_volume(0.01)
		shoteffect.play()

	def slime_effect(self):
		slimeeffect = pygame.mixer.Sound("sound effects/slime effect.wav")
		slimeeffect.set_volume(0.1)
		slimeeffect.play()

	def walk_effect(self):
		walkeffect = pygame.mixer.Sound("sound effects/step_1.wav")
		walkeffect.set_volume(0.01)
		walkeffect.play()

	def open_door(self):
		opendoor = pygame.mixer.Sound("sound effects/door.wav")
		opendoor.set_volume(0.1)
		opendoor.play()

	def chest_effect(self):
		chest = pygame.mixer.Sound("sound effects/chest sound.wav")
		chest.set_volume(0.1)
		chest.play()

	def coin_effect(self):
		coin = pygame.mixer.Sound("sound effects/coin.wav")
		coin.set_volume(0.1)
		coin.play()

	# bullet
	def new_aether_bullet(self):
		bullet = AetherBullet(self)
		bullet.shooting = True
		bullet.set_direction()

		if self.settings.bullets_limit > len(self.aether_bullets):
			self.aether_bullets.add(bullet)

	def aether_bullet_update(self):
		self.aether_bullets.update()


	# slime
	def _create_pyro_slime(self):
		for every_slime in range(self.stats.slime_number):
			slime = PyroSlime(self)
			slime.rect.x = randint(self.platform_game.x + 290, self.platform_game.x + 785)
			slime.rect.y = randint(self.platform_game.y + 315, self.platform_game.y + 455)

			self.pyro_slimes.add(slime)

	def shooting_slime(self):
		slime = PyroSlime(self)
		bullet = AetherBullet(self)
		if self.settings.slime_hp > self.settings.bullet_hp and pygame.sprite.groupcollide(self.aether_bullets, self.pyro_slimes, True, False):
			self.settings.slime_hp -= self.settings.bullet_hp
			print(self.settings.slime_hp)
			print("ok")
			self.slime_effect()
		if self.settings.slime_hp <= self.settings.bullet_hp:
			slimedead = pygame.sprite.groupcollide(self.aether_bullets, self.pyro_slimes, True, True)
			if slimedead:
				self.slime_effect()

	def check_slime_empty(self):
		if len(self.pyro_slimes) == 0:
			self.aether_bullets.empty()
			self.stats.level += 1
			self.stats.slime_number += 1
			self.scoreboard._level_()
			self.slime_level_up()
			self._create_pyro_slime()

	def slime_hit_aether(self):
		if pygame.sprite.spritecollideany(self.aether_game, self.pyro_slimes):
			self.slime_hit()
			return True
		else:
			return False
			
	def slime_hit(self):
		if self.stats.health_point > 0 and self.stats.health_point > self.settings.slime_damage:
			self.stats.health_point -= self.settings.slime_damage

			self.stats.health_point -= self.settings.slime_damage
			self.health_bar.shield_bar()

			self.aether_game.restart_position()

			self.pyro_slimes.empty()

			self._create_pyro_slime()

			print("HEALTH = ",self.stats.health_point)

			time.sleep(1)

		else:
			self.health_bar.shield_bar()
			self.health_bar.width = 0
			self.game_over = 0
			self.game_over += 1
			self.error = True
			self.gameover = True

	def update_slime(self):
		self.shooting_slime()
		self.pyro_slimes.update()
		if self.slime_hit_aether() == False:
			self.aether_game.update()

	def slime_level_up(self):
		if self.stats.level % 4 == 1:
			self.stats.slime_number = 2
			self.settings.slime_base_hp += 10
			self.settings.slime_hp = 1*self.settings.slime_base_hp
			print(self.settings.slime_hp)
		else:
			self.settings.slime_hp = self.settings.slime_base_hp*1
			print(self.settings.slime_hp)

	#pyro_boss
	def _create_pyro_boss(self):
		for every_boss in range(2):
			pyro_boss = PyroBoss(self)
			self.pyro_bos.add(pyro_boss)

	def reset_stats_boss(self):
		self._create_pyro_boss()
		self.settings.bos_hp = self.settings.bos_base_hp

	def shooting_boss(self):
		if self.settings.bos_hp > self.settings.bullet_hp and pygame.sprite.groupcollide(self.aether_bullets, self.pyro_bos, True, False):
			self.settings.bos_hp -= self.settings.bullet_hp
			print(self.settings.bos_hp)

		elif self.settings.bos_hp <= self.settings.bullet_hp and pygame.sprite.groupcollide(self.aether_bullets, self.pyro_bos, True, True):
			self.settings.bos_hp = 0
			self.stats.bos_number = 0
			print(self.settings.bos_hp)
		self.bos_bar.shoot()

	#pause
	def pause_game(self):
		self.stats.start = False
		self.menu_pause.run_game()

	def reset_game(self):
		self.stats.reset_statistics()
		self.settings.init_dynamic_settings()
		self.scoreboard._score_()
		self.scoreboard._level_()
		self.health_bar.shield_bar()
		self.health_bar.reset()

		print("h", self.stats.health_point)

		self.pyro_slimes.empty()
		self.aether_bullets.empty()

		self._create_pyro_slime()
		self.aether_game.restart_position()

		self.chest.chest_open = False
		self.chest.take = False

	#koin
	def check_koin(self):
		self.stats.token += self.chest.token_number
		print("a = ", self.stats.token)

if __name__ == "__main__":
	Game = Dungeon()
	Game.run_game() 