import random
import pygame
import sys

def draw(elements, idx, column_width, unit_height, screen, WIDTH, HEIGHT):
	screen.fill((0,0,0))

	for i, element in enumerate(elements):
		if i == idx:
			color = (255,0,0)
		else:
			color = (255,255,255)

		# pygame.draw.rect(screen, color, (i * column_width + 1, HEIGHT - unit_height * element, column_width - 2, unit_height * element))
		pygame.draw.rect(screen, color, (i * column_width, HEIGHT - unit_height * element, column_width, unit_height * element))

	pygame.display.update()
	exit()

def exit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def radix_sort_visualizer(elements, screen, WIDTH, HEIGHT):
	length = len(elements)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(elements)

	number_of_digits = get_number_of_digits(elements)

	for digit in range(number_of_digits):
		buckets = [[] for i in range(10)]
		for i, item in enumerate(elements):
			draw(elements, i, column_width, unit_height, screen, WIDTH, HEIGHT)
			buckets[get_digit(item, digit)].append(item)
		flatten(elements, buckets, column_width, unit_height, screen, WIDTH, HEIGHT)

def get_number_of_digits(elements):
	m = 0
	for item in elements:
		m = max(item, m)
	return len(str(m))

def get_digit(num, digit):
	return num // 10 ** digit % 10

def flatten(elements, buckets, column_width, unit_height, screen, WIDTH, HEIGHT):
	i = 0
	for bucket in buckets:
		for item in bucket:
			elements[i] = item
			i += 1
			draw(elements, i, column_width, unit_height, screen, WIDTH, HEIGHT)


if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 400) for i in range(400)]
	print(elements)
	radix_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()