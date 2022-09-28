import random
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

def merge_sort_visualzer(arr, elements, extra_index, screen, WIDTH, HEIGHT):
	if len(arr) <= 1:
		return arr
	column_width = WIDTH // len(elements)
	unit_height = HEIGHT // max(elements)

	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]

	merge_sort_visualzer(left, elements, extra_index, screen, WIDTH, HEIGHT)
	merge_sort_visualzer(right, elements, extra_index + mid, screen, WIDTH, HEIGHT)

	merge_two_sorted_arrays(left, right, arr, elements, extra_index, column_width, unit_height, screen, WIDTH, HEIGHT)

def merge_two_sorted_arrays(a, b, arr, elements, extra_index, column_width, unit_height, screen, WIDTH, HEIGHT):
	idx1 = idx2 = k = 0
	len_a = len(a)
	len_b = len(b)
	
	while idx1 < len_a and idx2 < len(b):
		if a[idx1] < b[idx2]:
			arr[k] = a[idx1]
			elements[k + extra_index] = a[idx1]
			idx1 += 1
		else:
			arr[k] = b[idx2]
			elements[k + extra_index] = b[idx2]
			idx2 += 1
		k += 1
		draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k + extra_index, idx1 + extra_index, idx2 + extra_index + len_a)

	while idx1 < len_a:
		arr[k] = a[idx1]
		elements[k + extra_index] = a[idx1]
		idx1 += 1
		k += 1
		draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k + extra_index, idx1 = idx1 + extra_index)

	while idx2 < len_b:
		arr[k] = b[idx2]
		elements[k + extra_index] = b[idx2]
		idx2 += 1
		k += 1
		draw(elements, column_width, unit_height, screen, WIDTH, HEIGHT, k + extra_index, idx2 = idx2 + extra_index + len_a)

if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 100) for i in range(400)]
	print(elements)
	merge_sort_visualzer(elements, elements, 0, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()
