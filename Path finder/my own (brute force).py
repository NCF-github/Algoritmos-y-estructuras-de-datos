import pygame
import math
import sys

screen_size = 800
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("A* Path Finding Algorithm")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
yellow = (255, 255, 0)
purple = (128, 0, 128)
orange = (255, 215, 0)
turquoise = (64, 224, 208)

class Node:
	def __init__(self, row, column, size, total_rows):
		self.row = row
		self.column = column
		self.x = row * size
		self.y = column * size
		self.color = white
		self.neighbors = []
		self.size = size
		self.total_rows = total_rows
		self.came_from = None

	def get_pos(self):
		return self.row, self.column

	def is_white(self):
		return self.color == white

	def is_closed(self):
		return self.color == red

	def is_open(self):
		return self.color == green

	def is_barrier(self):
		return self.color == black

	def is_start(self):
		return self.color == orange

	def is_end(self):
		return self.color == turquoise

	def reset(self):
		self.color = white

	def make_closed(self):
		self.color = red

	def make_open(self):
		self.color = green

	def make_barrier(self):
		self.color = black

	def make_end(self):
		self.color = turquoise

	def make_path(self):
		self.color = purple

	def make_start(self):
		self.color = orange

	def make_end(self):
		self.color = turquoise

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

	def add_origin(self, origin):
		self.came_from = origin

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.column].is_barrier():  # node bellow
			self.neighbors.append(grid[self.row + 1][self.column])

		if self.row > 0 and not grid[self.row - 1][self.column].is_barrier():  # node above
			self.neighbors.append(grid[self.row - 1][self.column])

		if self.column < self.total_rows - 1 and not grid[self.row][self.column + 1].is_barrier():  # right node
			self.neighbors.append(grid[self.row][self.column + 1])

		if self.column > 0 and not grid[self.row][self.column - 1].is_barrier():  # left node
			self.neighbors.append(grid[self.row][self.column - 1])

def algorithm(draw, grid, start, end):
	draw()
	open_nodes = [start]
	
	while True:
		draw()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		current_node = open_nodes[0]
		for neighbor in current_node.neighbors:
			if neighbor.is_end():
				if not current_node.is_start():
					current_node.make_closed()
				while current_node != start:
					current_node.make_path()
					current_node = current_node.came_from
					draw()
				return True
			if neighbor.is_white():
				open_nodes.append(neighbor)
				neighbor.make_open()
				neighbor.add_origin(current_node)
		if not current_node.is_start():
			current_node.make_closed()
		open_nodes.pop(0)
		if len(open_nodes) == 0:
			return False

def make_grid(rows, screen_size):
	grid = []
	gap = screen_size // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			node = Node(i, j, gap, rows)
			grid[i].append(node)
	return grid

def draw_grid(screen, rows, screen_size):
	gap = screen_size // rows
	for i in range(rows):
		pygame.draw.line(screen, gray, (0, i * gap), (screen_size, i * gap))
		pygame.draw.line(screen, gray, (i * gap, 0), (i * gap, screen_size))  # Here I made my own correction. Might be troublesome latter

def draw(screen, grid, rows, screen_size):
	screen.fill(white)
	for row in grid:
		for node in row:
			node.draw(screen)

	draw_grid(screen, rows, screen_size)
	pygame.display.update()

def get_clicked_pos(pos, rows, screen_size):  # pos is the mouse position
	gap = screen_size // rows
	y, x = pos

	row = y // gap
	column = x // gap
	return row, column

def clear_gree_red_and_purple_squares(grid):
	for row in grid:
		for node in row:
			if not (node.is_barrier() or node.is_start() or node.is_end()):
				node.reset()

def main(screen, screen_size):
	rows = 50
	grid = make_grid(rows, screen_size)

	start = None
	end = None

	has_been_run = False

	run = True
	while run:
		draw(screen, grid, rows, screen_size)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:  # Left
				if has_been_run:
					clear_gree_red_and_purple_squares(grid)
					has_been_run = False
				pos = pygame.mouse.get_pos()
				row, column = get_clicked_pos(pos, rows, screen_size)
				node = grid[row][column]
				if not start and node != end:
					start = node
					start.make_start()

				elif not end and node != start:
					end = node
					end.make_end()

				elif node != end and node != start:
					node.make_barrier()

			elif pygame.mouse.get_pressed()[2]:  # Right
				if has_been_run:
					clear_gree_red_and_purple_squares(grid)
					has_been_run = False
				pos = pygame.mouse.get_pos()
				row, column = get_clicked_pos(pos, rows, screen_size)
				node = grid[row][column]
				node.reset()
				if node == start:
					start = None
				if node == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for node in row:
							if not (node.is_barrier() or node.is_start() or node.is_end()):
								node.reset()
							node.update_neighbors(grid)
					algorithm(lambda: draw(screen, grid, rows, screen_size), grid, start, end)
					has_been_run = True

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(rows, screen_size)

	pygame.quit()

if __name__ == '__main__':
	main(screen, screen_size)