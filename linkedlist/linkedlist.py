class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def set_next_node(self, node):
        self.next_node = node
    
    def append(self, value):
        next_node = Node(value)
        self.next_node = next_node
        return next_node
    
    def __getitem__(self, key):
        node = self
        counter = 0
        while counter < key:
            node = node.next_node
            counter += 1
        return node
    
    def insert(self, position, value):
        if position == 0:
            node = Node(value)
            node.next_node = self
            return node
        else:
            node = Node(value)
            split_start = self[position - 1]
            split_end = split_start.next_node
            split_start.next_node = node
            node.next_node = split_end
            return self
        
    def pop(self, position):
        if position == 0:
            return self, self.next_node
        else:
            split_start = self[position - 1]
            to_remove = split_start.next_node
            split_end = to_remove.next_node
            split_start.next_node = split_end
            return to_remove, self
