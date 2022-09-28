import random
import pygame
import sys

def draw(elements, idx0, idx1, idx2, column_width, unit_height, screen, WIDTH, HEIGHT):
	screen.fill((0,0,0))

	for i, element in enumerate(elements):
		if i == idx1 or i == idx2:
			color = (255,0,0)
		elif i == idx0:
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

def quick_sort_visualizer(elements, start, end, screen, WIDTH, HEIGHT):
	length = len(elements)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(elements)

	pivot_index = start
	pivot = elements[pivot_index]

	start_pointer = pivot_index + 1
	end_pointer = end

	while True:
		while start_pointer <= end and elements[start_pointer] <= pivot:
			start_pointer += 1
			draw(elements, pivot_index, start_pointer, end_pointer, column_width, unit_height, screen, WIDTH, HEIGHT)
		while elements[end_pointer] > pivot and end_pointer != start:
			end_pointer -= 1
			draw(elements, pivot_index, start_pointer, end_pointer, column_width, unit_height, screen, WIDTH, HEIGHT)

		if end_pointer < start_pointer:
			elements[pivot_index], elements[end_pointer] = elements[end_pointer], elements[pivot_index]
			break
		else:
			elements[start_pointer], elements[end_pointer] = elements[end_pointer], elements[start_pointer]

	if end_pointer - start > 1:
		quick_sort_visualizer(elements, start, end_pointer - 1, screen, WIDTH, HEIGHT)
	if end - end_pointer > 1:
		quick_sort_visualizer(elements, end_pointer + 1, end, screen, WIDTH, HEIGHT)


if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 100) for i in range(400)]
	print(elements)
	quick_sort_visualizer(elements, 0, len(elements) - 1, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()