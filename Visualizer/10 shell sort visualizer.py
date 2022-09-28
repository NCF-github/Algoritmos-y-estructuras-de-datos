import pygame
import random

def insertion_sort(arr, screen, WIDTH, HEIGHT, start=0, gap=1):
	column_width = WIDTH // len(elements)
	unit_height = HEIGHT // max(elements)

	for i in range(start, len(arr), gap):
		while i >= gap and arr[i] < arr[i - gap]:
			draw(arr, i, i - 1, column_width, unit_height, screen, WIDTH, HEIGHT)
			arr[i], arr[i - gap] = arr[i - gap], arr[i]
			i -= gap

def shell_sort_visualizer(arr, screen, WIDTH, HEIGHT):
	column_width = WIDTH // len(elements)
	unit_height = HEIGHT // max(elements)

	gap = len(arr) // 2

	while gap != 0.5:
		gap = int(gap)
		for start in range(gap):
			insertion_sort(arr, screen, WIDTH, HEIGHT, start, gap)
		gap /= 2

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


if __name__ == "__main__":
	pygame.init()

	WIDTH = 1200
	HEIGHT = 800
	screen = pygame.display.set_mode((WIDTH, HEIGHT))

	elements = [random.randint(1, 100) for i in range(400)]
	print(elements)
	shell_sort_visualizer(elements, screen, WIDTH, HEIGHT)
	print(elements)

	pygame.quit()
