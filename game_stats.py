class GameStats():
	"""Статистика в игре"""

	def __init__(self, ai_game):
		"""Запуск статистики."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Игра Alien Invasion запускается в активном состоянии.
		self.game_active = False

	def reset_stats(self):
		"""Запуск статистики, изменяющуюся в ходе игры."""
		self.ships_left = self.settings.ship_limit
