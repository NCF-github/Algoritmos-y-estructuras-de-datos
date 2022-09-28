import random
import pygame
import sys

def draw(elements, idx1, idx2, column_width, unit_height, screen, WIDTH, HEIGHT):
	screen.fill((0,0,0))

	for i, element in enumerate(elements):
		if i == idx1 or i == idx2:
			color = (255,0,0)
		else:
			color = (255,255,255)

		pygame.draw.rect(screen, color, (i * column_width + 1, HEIGHT - unit_height * element, column_width - 2, unit_height * element))

	pygame.display.update()
	exit()

def exit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def insertion_sort_visualizer(elements, screen, WIDTH, HEIGHT):
	length = len(elements)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(elements)

	for i in range(1, len(elements)):
		idx = i
		while elements[idx - 1] > elements[idx] and idx != 0:
			draw(elements, idx, idx - 1, column_width, unit_height, screen, WIDTH, HEIGHT)
			elements[idx - 1], elements[idx] = elements[idx], elements[idx - 1]
			idx -= 1

if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 50) for i in range(100)]
	print(elements)
	insertion_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()
