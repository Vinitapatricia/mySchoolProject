import pygame


class Settings:

	def __init__(self):
		#screen settings
		self.base_dimension = 60

		self.screen_width = 16 * self.base_dimension
		self.screen_height = 9 * self.base_dimension
		self.title = "Detective Dungeon"

		self.bg = pygame.image.load("img/candidate_1.jpg")
		self.shop_bg = pygame.image.load("img/shop/latar shop.png")

		#room settings
		self.base_floor = 83
		self.base_wall = 70

		# aether bullet setting
		self.bullet_color = 10,0,0
		self.bullet_radius = 3
		self.bullets_limit = 999

		#enemy setting
		self.slime_point = 5
		self.slime_damage = 15

		# bos setting
		self.bos_health_color = 0,255,43
		self.bos_health_height = 5

		self.init_dynamic_settings()

	def init_dynamic_settings(self):
		self.aether_speed = 3

		self.bullet_speed = 5
		self.bullet_hp = 15

		self.enemy_speed = 0.5
		self.slime_base_hp = 15
		self.slime_hp = 1*self.slime_base_hp

		self.bos_base_hp = 100
		self.bos_hp = 1*self.bos_base_hp
		