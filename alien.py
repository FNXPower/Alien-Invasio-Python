import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Один пришелец."""

	def __init__(self, ai_game):
		"""Запуск пришельца и его начальная позиция."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#Загрузка изображение пришельца и назначение атрибута rect.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#Появление в левом верхнем углу
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Сохранение точной горизонтальной позиции пришельца
		self.x = float(self.rect.x)

	def check_edges(self):
		"""Возвращает True, если пришелец нахоидтся у края экрана."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Перемещение пришельвец влево или вправо."""
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x



