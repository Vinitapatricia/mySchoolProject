import json
import pygame
from datetime import  datetime

class Save:

	def __init__(self, Game):
		self.settings = Game.settings
		self.stats = Game.stats

		self.data = {
	
		}

	def saving(self):
		#with open('saved_data.json', 'r') as f:
			#self.data = json.load(f)

		self.now = datetime.now()

		self.data["user"] = {
			'character' : 'aether',
			'floor' : self.stats.level,
			'token' : self.stats.token,
			'attack' : self.settings.bullet_hp,
			'damage' : self.settings.slime_damage,
			'max_hp' : self.stats.health_point,
			'price_attack': self.stats.price_attack,
			'price_defense' : self.stats.price_defense,
			'price_hp' : self.stats.price_hp,
			'heal_item' : self.stats.heal_left,
			'bos_number' : self.stats.bos_number,
			'slime_number' : self.stats.slime_number
		}

		with open('saved_data.json', 'w') as f:
			json.dump(self.data, f)