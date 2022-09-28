import random
import math
import pygame
import sys

def draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k = -1, idx1 = -1, idx2 = -1):
	screen.fill((0,0,0))

	for i, element in enumerate(elements):
		if i == idx1 or i == idx2:
			color = (255,0,0)
		elif i == k:
			color = (0,255,0)
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

def insertion_sort(elements, start, end, column_width, unit_height, screen, WIDTH, HEIGHT):
	end = min(len(elements), end)

	for i in range(start, end):
		while i != start and elements[i - 1] > elements[i]:
			draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, idx1 = i, idx2 = i - 1)
			elements[i - 1], elements[i] = elements[i], elements[i - 1]
			i -= 1

def merge(elements, starting_idx, a, b, column_width, unit_height, screen, WIDTH, HEIGHT, RUN):
	idx1 = idx2 = 0
	k = starting_idx
	len_a = len(a)
	len_b = len(b)
	
	while idx1 < len_a and idx2 < len(b):
		draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k, idx1 + starting_idx, idx2 + starting_idx + RUN)
		if a[idx1] < b[idx2]:
			elements[k] = a[idx1]
			idx1 += 1
		else:
			elements[k] = b[idx2]
			idx2 += 1
		k += 1

	while idx1 < len_a:
		draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k = k, idx1 = idx1 + starting_idx)
		elements[k] = a[idx1]
		idx1 += 1
		k += 1

	while idx2 < len_b:
		draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k = k, idx2 = idx2 + starting_idx + RUN)
		elements[k] = b[idx2]
		idx2 += 1
		k += 1

def tim_sort_visualizer(elements, screen, WIDTH, HEIGHT):
	length = len(elements)

	if not elements:
		return []

	column_width = WIDTH // len(elements)
	unit_height = HEIGHT // max(elements)

	RUN = 32
	for i in range(20, 50):
		number_of_arrays_that_will_be_created = math.ceil(length / i)
		x = math.log(number_of_arrays_that_will_be_created, 2)
		if x == int(x):
			RUN = i

	for i in range(0, len(elements), RUN):
		insertion_sort(elements, i, i + RUN, column_width, unit_height, screen, WIDTH, HEIGHT)

	while math.ceil(length / RUN) != 1:
		for i in range(0, length, 2 * RUN):
			a = elements[i:i + RUN]
			b = elements[i + RUN: i + 2 * RUN]
			if b:
				merge(elements, i, a, b, column_width, unit_height, screen, WIDTH, HEIGHT, RUN)
		RUN *= 2

if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 100) for i in range(400)]
	print(elements)
	tim_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()
