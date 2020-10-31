# For this one we declare the node property inside the tree (self.node = None) instead of root as in the binary_tree and max_heap.
# This updated references without having the parent property.
# This means we have to instantiate a new BST when creating a left or right node.
# Example:
    # bst = BST()
    # bst.node = Node(value=1)
    # bst.node.left = BST()
    # bst.node.left.value = Node(value=2)


class Node:
    # This type of node allow us to have key: value pairs to save data other than integers (as values, with ints as keys)
    # Kinda works like a hash table when combined with the BST.
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __str__(self):
        return "<Node: {}>".format(self.value)

class BST:
    def __init__(self, index=None):
        self.node = None
        self.index = index
    
    def insert(self, value=None):
        ## ADD KEYS FOR SEARCH AND QUERY
        key = value
        if self.index:
            key = value[self.index]
        node = Node(key=key, value=value)
        
        if not self.node:
            self.node = node
            self.node.left = BST(index=self.index)
            self.node.right = BST(index=self.index)
            return
        
        if key > self.node.key:
            if self.node.right:
                self.node.right.insert(value=value)
            else:
                self.node.right.node = node
        else:
            if self.node.left:
                self.node.left.insert(value=value)
            else:
                self.node.left.node = node
        
        difference = self.depth(self.node.left.node) - self.depth(self.node.right.node)
        
        ## KEEPS IT BALANCED
        # Left side case.
        if difference > 1:
            # Left-right case.
            if key > self.node.right.node.key:
                self.node.left.left_rotate()
            # Left-left case.
            self.right_rotate()
                
        # Right side case.
        if difference < -1:
            # Right-left case.
            if key <= self.node.left.node.key:
                self.node.left.right_rotate()
            # Right-right case.
            self.left_rotate()

    def insert_multiple(self, values):
        for value in values:
            self.insert(value)
            
    def inorder(self, tree):
        if not tree or not tree.node:
            return []
        return (self.inorder(tree.node.left)+[tree.node.value]+self.inorder(tree.node.right))

    def search(self, key):
        # Having values in order speeds up search time as we do not have to go through every entry in the BST or sort it first.
        # Faster than doing pre, in or post order traversal.
        if not self.node:
            return False
        if key == self.node.key:
            return True
        
        result = False
        if self.node.left:
            result = self.node.left.search(key)
        if self.node.right:
            result = self.node.right.search(key)
        return result

    def depth(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        
        return max(self.depth(node.left.node), self.depth(node.right.node)) + 1
    
    def is_balanced(self):
        if not self.node:
            return True
        
        left_subtree = self.depth(self.node.left.node)
        right_subtree = self.depth(self.node.right.node)
        
        return abs(left_subtree - right_subtree) < 2

    def left_rotate(self):
        old_node = self.node
        new_node = self.node.right.node
        if not new_node:
            return
        
        new_right_sub = new_node.left.node
        self.node = new_node
        old_node.right.node = new_right_sub
        new_node.left.node = old_node
    
    def right_rotate(self):
        old_node = self.node
        new_node = self.node.left.node
        if not new_node:
            return
        
        new_left_sub = new_node.right.node
        self.node = new_node
        old_node.left.node = new_left_sub
        new_node.right.node = old_node

    def greater_than(self, key):
        if not self.node:
            return []
        
        values = []
        if self.node.left:
            values += self.node.left.greater_than(key)
        if self.node.right:
            values += self.node.right.greater_than(key)
        if self.node.key > key:
            values.append(self.node.value)
        return values
