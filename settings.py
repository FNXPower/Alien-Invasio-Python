class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализация настроек игры."""
		# Параметры экрана
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (230, 230, 230)

		# Настройки корабля
		self.ship_speed = 1.5
		self.ship_limit = 0

		# Параметры снаряда
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3 

		# Настройки пришельцев
		self.alien_speed = 30
		self.fleet_drop_speed = 10
		# fleet_direction = 1 - движение вправо, а -1 - влева.
		self.fleet_direction = 1
	
	
