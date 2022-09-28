class BinarySearchTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

	def add(self, data):
		if data < self.data:
			if self.left:
				self.left.add(data)
			else:
				self.left = BinarySearchTreeNode(data)
				self.left.parent = self
		elif data > self.data:
			if self.right:
				self.right.add(data)
			else:
				self.right = BinarySearchTreeNode(data)
				self.right.parent = self

	def in_order_traversal(self):
		elements = []

		# Visit left tree
		if self.left:
			elements += self.left.in_order_traversal()

		# Visit base node
		elements.append(self.data)

		# Visit right tree
		if self.right:
			elements += self.right.in_order_traversal()

		return elements

	def pre_order_traversal(self):
		elements = [self.data]

		if self.left:
			elements += self.left.pre_order_traversal()

		if self.right:
			elements += self.right.pre_order_traversal()

		return elements

	def post_order_traversal(self):
		elements = []

		if self.left:
			elements += self.left.post_order_traversal()

		if self.right:
			elements += self.right.post_order_traversal()

		elements.append(self.data)

		return elements

	def search(self, val):
		if val == self.data:
			return True

		if val < self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False

	def min(self):
		if self.left:
			return self.left.min()
		else:
			return self.data

	def max(self):
		if self.right:
			return self.right.max()
		else:
			return self.data

	def sum(self):
		mySum = self.data
		if self.right:
			mySum += self.right.sum()
		if self.left:
			mySum += self.left.sum()
		return mySum

	def delete_by_value(self, val):
		if val == self.data:
			self.delete()

		elif val < self.data:
			if self.left:
				self.left.delete_by_value(val)
			else:
				print("Error: value not in tree")

		elif val > self.data:
			if self.right:
				self.right.delete_by_value(val)
			else:
				print("Error: value not in tree")

	def delete_by_position(self, idx):
		elements = []

		# Visit left tree
		if self.left:
			elements += self.left.in_order_traversal()

		# Visit base node
		elements.append(self)

		# Visit right tree
		if self.right:
			elements += self.right.in_order_traversal()

		if idx < len(elements):
			elements[idx].delete()
		else:
			print("Error: index out of range")

	def delete(self):
		if self.left:
			# print(self.data, "->", self.left.max())
			self.data = self.left.max()
			self.left.max_node().delete()

		elif self.right:
			# print(self.data, "->", self.right.min())
			self.data = self.right.min()
			self.right.min_node().delete()

		else:
			if self.parent.left == self:
				self.parent.left = None
			else:
				self.parent.right = None

	def min_node(self):
		if self.left:
			return self.left.min_node()
		else:
			return self

	def max_node(self):
		if self.right:
			return self.right.max_node()
		else:
			return self

	def get_height(self, previous_height=0):
		if self.left:
			l = self.left.get_height(previous_height + 1)
		else:
			l = previous_height + 1

		if self.right:
			r = self.right.get_height(previous_height + 1)
		else:
			r = previous_height + 1

		return max(l, r)

	def representate(self):
		layers = [[] for i in range(self.get_height() + 1)]

		for node in self.get_nodes_with_layer():
			layers[node[1]-1].append(node[0])

		layers.pop()

		space_unit = " " * len(str(self.max()))

		for i, layer in enumerate(layers):
			line = ""
			line += space_unit * (2 ** (len(layers) - i - 1) - 1)
			for n in layer:
				line += self.convert_to_str(n, space_unit)
				line += space_unit * (2 ** (len(layers) - i) - 1)
			print(line)

	def get_nodes_with_layer(self, previous_layer=0):
		current_layer = previous_layer + 1
		elements = []

		if self.left:
			elements += self.left.get_nodes_with_layer(current_layer)
		else:
			elements += [(" ", current_layer + 1)]

		elements.append((self.data, current_layer))

		if self.right:
			elements += self.right.get_nodes_with_layer(current_layer)
		else:
			elements += [(" ", current_layer + 1)]

		return elements

	def convert_to_str(self, n, space_unit):
		n = str(n)
		n = " " * (len(space_unit) - len(n)) + n
		return n


def build_tree(elements):
	root = BinarySearchTreeNode(elements[0])

	for i in range(len(elements)):
		if i == 0:
			continue
		root.add(elements[i])

	return root


if __name__ == '__main__':
	numbers = [17, 4, 1, 20, 9, 23, 18, 34]

	numbers_tree = build_tree(numbers)
	print(numbers_tree.in_order_traversal())
	print(numbers_tree.pre_order_traversal())
	print(numbers_tree.post_order_traversal())
	print(numbers_tree.search(2))
	print(numbers_tree.min())
	print(numbers_tree.max())
	print(numbers_tree.sum())

	print()

	numbers_tree.delete_by_value(34)
	print(numbers_tree.in_order_traversal())
	numbers_tree.add(34)

	print()

	numbers_tree.representate()

	print()

	countries = ["USA", "Spain", "Germany", "USA", "Pepe"]

	countries_tree = build_tree(countries)  # Can be other things, such as strings, not just numbers
	print(countries_tree.in_order_traversal())  # Orders in alphabetical order