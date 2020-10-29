# We don't need to use the `Node` class anymore.

# PYTHON HAS OWN IMPLEMENTATION OH HEAP (MIN/MAX BINARY TREE) CALLED heapq
# FASTER CAUSE WRITTEN IN C

import math
class MaxHeap:
	def __init__(self):
		self.nodes = []
	
	def insert(self, value):
		self.nodes.append(value)
		
		index = len(self.nodes) - 1
		parent_index = math.floor((index-1)/2)
		while index > 0 and self.nodes[parent_index] < self.nodes[index]:
			self.nodes[parent_index], self.nodes[index] = self.nodes[index], self.nodes[parent_index]
			index = parent_index
			parent_index = math.floor((index-1)/2)
		return self.nodes

	def insert_multiple(self, values):
		for value in values:
			self.insert(value)
			
	def max(self):
		return self.nodes[0]

	def pop(self):
		root = self.nodes[0]
		self.nodes[0] = self.nodes[-1]
		self.nodes = self.nodes[:-1]
		index = 0
		left_child_idx = 2*index + 1
		right_child_idx = 2*index + 2
		
		while max(left_child_idx, right_child_idx) < len(self.nodes) - 1:
			swap_index = left_child_idx
			if self.nodes[left_child_idx] < self.nodes[right_child_idx]:
				swap_index = right_child_idx
				
			if self.nodes[swap_index] < self.nodes[index]:
				return root
			
			self.nodes[swap_index], self.nodes[index] = self.nodes[index], self.nodes[swap_index]
			index = swap_index
			left_child_idx = 2*index + 1
			right_child_idx = 2*index + 2
		return root

	def top_n_elements(self, n):
		return [self.pop() for _ in range(n)]