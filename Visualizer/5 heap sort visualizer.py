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

def swap(elements, i, j):
	elements[i], elements[j] = elements[j], elements[i]

def sift_down(elements, i, upper, column_width, unit_height, screen, WIDTH, HEIGHT):
	while True:
		l, r = i*2+1, i*2+2
		draw(elements, i, l, r, column_width, unit_height, screen, WIDTH, HEIGHT)
		if max(l, r) < upper:
			if elements[i] >= max(elements[l], elements[r]): break
			elif elements[l] > elements[r]:
				swap(elements, i, l)
				i = l
			else:
				swap(elements, i, r)
				i = r
		elif l < upper:
			if elements[l] > elements[i]:
				swap(elements, i, l)
				i = l
			else: break
		elif r < upper:
			if elements[r] > elements[i]:
				swap(elements, i, l)
				i = r
			else: break
		else: break

def heap_sort_visualizer(elements, screen, WIDTH, HEIGHT):
	length = len(elements)
	column_width = WIDTH // length
	unit_height = HEIGHT // max(elements)

	for j in range((len(elements) - 2 ) // 2, -1, -1):
		sift_down(elements, j, len(elements), column_width, unit_height, screen, WIDTH, HEIGHT)

	for end in range(len(elements) - 1, 0, -1):
		swap(elements, 0, end)
		sift_down(elements, 0, end, column_width, unit_height, screen, WIDTH, HEIGHT)


if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 100) for i in range(400)]

	print(elements)
	heap_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()