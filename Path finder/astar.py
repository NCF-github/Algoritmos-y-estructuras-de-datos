# Video tutorial: https://www.youtube.com/watch?v=JtiK0DOeI4A&list=WL&index=14
# The algorithm explanation is at the begining and the actual programming is at 1:10:00

import pygame
import math
from queue import PriorityQueue

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

	def get_pos(self):
		return self.row, self.column

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

	def __lt__(self, other):
		return False

def h(p1, p2):  # p1 and p2 are two points, meaning a tuple or list containing x and y coordenates
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)  # Returns the distance between two points (difference in x coordinates + difference in y coordinate)

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()


def algorithm(draw, grid, start, end):
	draw()
	count = 0
	open_set = PriorityQueue()  # Kind of like a list that only returns the element with the smallest value
	open_set.put((0, count, start))  # Puts the starting node in the open set
	came_from = {}

	g_score = {node: float("inf") for row in grid for node in row}  # Distances from every node to the start (start at infinity)
	g_score[start] = 0  # Distance from start to start is 0

	f_score = {node: float("inf") for row in grid for node in row}  # Expected distace from node to end
	f_score[start] = h(start.get_pos(), end.get_pos())  # Calculate h_score for the starting node

	open_set_hash = {start}  # Keeps track of the nodes in the open_set because the PriorityQueue doesn´t have a function to check if it is empty

	while not open_set.empty():  # While there are open nodes to check
		for event in pygame.event.get():  # This being an internal loop, the user might get stuck in it. This allowes the user to exit.
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]  # The .get() returns the element with lowest value and the [2] is because of the structure used (see above)
		# The line above "names" the node to be inspected as current
		open_set_hash.remove(current)  # To update the thing that keeps track of the PriorityQueue to check if it is empty

		if current == end:
			reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True  # Found path, end loop

		for neighbor in current.neighbors:  # Do this for every neighbor the current node has
			temp_g_score = g_score[current] + 1  # The g_score is distance from start taking the path the current node came from.
			# This value increments with every "step" (every time we move from a node to an other) because connections between nodes are not weighted

			if temp_g_score < g_score[neighbor]:  # If this new path is better that the previous, change it and update its g and f values
				came_from[neighbor] = current  # Update path to the new and better found
				g_score[neighbor] = temp_g_score  # Update g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())  # Update f_score
				if neighbor not in open_set_hash:  # Add to the open set if it was not already in there
					count += 1  # The one part that has me confused. I don´t know what this variable is used for
					open_set.put((f_score[neighbor], count, neighbor))  # Put in priority queue
					open_set_hash.add(neighbor)  # Put in the thing to keep track of priority queue to match it
					neighbor.make_open()  # Update color to open node
		draw()

		if current != start:
			current.make_closed()  # Closes the node (updates its color)

	return False  # Path not found



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