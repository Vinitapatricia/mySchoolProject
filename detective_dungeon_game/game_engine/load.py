from json import load
import pygame
from datetime import  datetime

class Load:
	def __init__(self, Game):
		self.settings = Game.settings
		self.stats = Game.stats

		self.data = {}

	def load_(self):
		with open('saved_data.json', 'r') as f:
			self.data = load(f)

	def _load(self):
		self.load_()
		self.stats.level = self.data["user"]["floor"]
		self.stats.token = self.data["user"]['token']
		self.settings.bullet_hp = self.data["user"]["attack"]
		self.settings.slime_damage = self.data["user"]["damage"]
		self.stats.health_point = self.data["user"]["max_hp"]
		self.stats.price_attack = self.data["user"]["price_attack"]
		self.stats.price_defense = self.data["user"]["price_defense"]
		self.stats.price_hp = self.data["user"]["price_hp"]
		self.stats.heal_left = self.data["user"]["heal_item"]
		self.stats.bos_number = self.data["user"]["bos_number"]
		self.stats.slime_number = self.data["user"]["slime_number"]
		print("u",self.stats.slime_number)