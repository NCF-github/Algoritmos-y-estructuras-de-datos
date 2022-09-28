class BinarySearchTreeNose:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.count = 1

	def add(self, data):
		if data == self.data:
			self.count += 1
		if data < self.data:
			if self.left:
				self.left.add(data)
			else:
				self.left = BinarySearchTreeNose(data)
		elif data > self.data:
			if self.right:
				self.right.add(data)
			else:
				self.right = BinarySearchTreeNose(data)

	def in_order_traversal(self):
		elements = []

		# Visit left tree
		if self.left:
			elements += self.left.in_order_traversal()

		# Visit base node
		for i in range(self.count):
			elements.append(self.data)

		# Visit right tree
		if self.right:
			elements += self.right.in_order_traversal()

		return elements

	def pre_order_traversal(self):
		elements = [self.data for i in range(self.count)]

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

		for i in range(self.count):
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

def build_tree(elements):
	root = BinarySearchTreeNose(elements[0])

	for i in range(len(elements)):
		if i == 0:
			continue
		root.add(elements[i])

	return root

if __name__ == '__main__':
	numbers = [17, 4, 1, 20, 9, 23, 18, 34, 2, 2, 17, 20, 35]

	numbers_tree = build_tree(numbers)
	print(numbers_tree.in_order_traversal())
	print(numbers_tree.pre_order_traversal())
	print(numbers_tree.post_order_traversal())
	print(numbers_tree.search(2))
	print(numbers_tree.min())
	print(numbers_tree.max())
	print(numbers_tree.sum())

	countries = ["USA", "Spain", "Germany", "USA", "Pepe"]

	countries_tree = build_tree(countries)  # Can be other things, such as strings, not just numbers
	print(countries_tree.in_order_traversal())  # Orders in alphabetical order