class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def __repr__(self):
		# Helpful method to keep track of Node values.
		return "<Node: {}>".format(self.value)


class BinaryTree:
	def __init__(self, values=None):
		self.root = None
		if values:
			self.insert(values)
	
	def insert(self, values, index=0):
		node = None
		if index < len(values):
			node = Node(values[index])
			if not self.root:
				self.root = node
			node.left = self.insert(values, index=index*2+1)
			node.right = self.insert(values, index=index*2+2)
		return node

	def is_parent(self, node):
		if node.left or node.right:
			return True
		return False
	
	def is_interior(self, node):
		return (not node == self.root) and self.is_parent(node)
	
	def is_leaf(self, node):
		return (not node == self.root) and not self.is_interior(node)

	def preorder_traverse(self, node):
		if not node:
			return []
		return ([node.value]+self.preorder_traverse(node.left)+self.preorder_traverse(node.right))
	
	def inorder_traverse(self, node):
		if not node:
			return []
		return (self.inorder_traverse(node.left)+[node.value]+self.inorder_traverse(node.right))
	
	def postorder_traverse(self, node):
		if not node:
			return []
		return (self.postorder_traverse(node.left)+self.postorder_traverse(node.right)+[node.value])

	def height(self, node):
		if not node:
			return 0
		return max(self.height(node.left), self.height(node.right)) + 1
		
	def num_nodes(self, node):
		return len(self.preorder_traverse(node))

	def is_balanced(self, node):
		if not node:
			return True
		left_height = self.height(node.left)
		right_height = self.height(node.right)
		
		if (abs(right_height - left_height) <= 1 and self.is_balanced(node.left) and self.is_balanced(node.right)):
			return True
		return False