import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Инициализирует pygame, settings и объект экрана. 
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Создание корабля.
	ship = Ship(screen)
	
	# Запуск основного цикла игры
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		
run_game()