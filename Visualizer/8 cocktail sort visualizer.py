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

def cocktail_sort_visualizer(elements, screen, WIDTH, HEIGHT):
	length = len(elements)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(elements)

	start = 0
	end = length - 1

	while start < end:
		swapped = False
		for i in range(start, end):
			draw(elements, i, i + 1, column_width, unit_height, screen, WIDTH, HEIGHT)
			if elements[i] > elements[i + 1]:
				elements[i], elements[i + 1] = elements[i + 1], elements[i]
				swapped = True
		end -= 1

		for i in range(end, start, -1):
			draw(elements, i, i - 1, column_width, unit_height, screen, WIDTH, HEIGHT)
			if elements[i] < elements[i - 1]:
				elements[i], elements[i - 1] = elements[i - 1], elements[i]
				swapped = True
		start += 1

		if not swapped:
			break

if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 50) for i in range(100)]
	print(elements)
	cocktail_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()
