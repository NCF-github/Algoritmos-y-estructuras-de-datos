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

def bubble_sort_visualizer(arr, screen, WIDTH, HEIGHT):
	length = len(arr)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(arr)

	for i in range(len(arr)):
		lowest = i
		for j in range(i, len(arr)):
			draw(elements, i, j, column_width, unit_height, screen, WIDTH, HEIGHT)
			if arr[j] < arr[lowest]:
				lowest = j
		draw(elements, i, lowest, column_width, unit_height, screen, WIDTH, HEIGHT)
		arr[i], arr[lowest] = arr[lowest], arr[i]


if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 50) for i in range(100)]
	print(elements)
	bubble_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()
