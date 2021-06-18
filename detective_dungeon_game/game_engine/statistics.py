class Statistics:

	def __init__(self, Game):
		self.settings = Game.settings
		self.start = True

		self.reset_statistics()

	def reset_statistics(self):
		self.health_point = 100
		self.score = 0
		self.level = 1
		self.fire = 0
		self.power_up = 0
		self.defense_up = 0
		self.max_hp = 0
		self.heal_left = 3
		self.token = 0
		self.price_attack = 100
		self.price_defense = 100
		self.price_hp = 100
		self.slime_number = 1
		self.bos_number = 0

