import sys
import pygame

def check_events(ship):
	"""Обрабатывает нажатия клаиш и события мыши."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			# Переместить корабль вправо.
			if event.key == pygame.K_RIGHT:
				ship.rect.centerx += 1
				ship.moving_right = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False		
def update_screen(ai_settings, screen, ship):
	"""Обновляет изображения на экране и отображает новый экран."""
	#При каждом проходе цикла перерисовыается экран.
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	# Отображение последнего прорисованного экрана.
	pygame.display.flip()