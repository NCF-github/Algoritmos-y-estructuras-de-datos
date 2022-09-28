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

def exit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def bubble_sort_visualizer(elements, screen, WIDTH, HEIGHT):
	length = len(elements)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(elements)

	for j in range(length - 1):
		swapped = False

		for i in range(1, length - j):
			draw(elements, i, i-1, column_width, unit_height, screen, WIDTH, HEIGHT)
			exit()

			if elements[i - 1] > elements[i]:
				elements[i - 1], elements[i] = elements[i], elements[i - 1]
				swapped = True

		if not swapped:
			break

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
