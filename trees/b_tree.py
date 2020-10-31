## B TREE is essentially a Binary Search Tree (BST) but nodes are arrays (len(node) > 1)

class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []
    
    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self):
        # Helpful method to keep track of Node keys.
        return "<Node: {}>".format(self.keys)    

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None
            
    def insert_multiple(self, keys):
        for key in keys:
            self.insert(key)
            
    def insert(self, key):
        if not self.root:
            self.root = Node(keys=[key])
            return
       
        # Splits the root in case the node is complete, we have to instantiate a new node as the new root.
        if len(self.root.keys) == 2*self.t - 1:
            old_root = self.root
            self.root = Node()
            left, right, new_key = self.split(old_root)
            self.root.keys.append(new_key)
            self.root.children.append(left)
            self.root.children.append(right)
                
        self.insert_non_full(self.root, key)
            
    def insert_non_full(self, node, key):
        # If the node is a leaf, we just insert at the correct location using the index
        if node.is_leaf():
            if len(node.keys) >= 2*self.t - 1:
                # If it will exceed the maximum, don't add the key.
                return
            
            index = 0
            for k in node.keys:
                if key > k:
                    index += 1
                else:
                    break
            node.keys.insert(index, key)
            return
        
        # If the node is not a leaf, we set an index to -1 and iterate through the root keys to see if the key we wanna insert is greater.
        # If it is greater, we increment the index, if it isn't, we don't
        index = 0
        for k in node.keys:
            if key > k:
                index += 1
            else:
                break
        # This is the case if the node is full. We split the node in two (resulting in two nodes of t degrees, well in our bound), keeping reference
        # to the newly created node, so we wanna make the split with the parent node, so we can alter the references in the children array.
        if len(node.children[index].keys) == 2*self.t - 1:
            left_node, right_node, new_key = self.split(node.children[index])
            node.keys.insert(index, new_key)
            node.children[index] = left_node
            node.children.insert(index+1, right_node)
            if key > new_key:
                index += 1
                        
        self.insert_non_full(node.children[index], key)

    def split(self, node):
        left_node = Node(
            keys=node.keys[:len(node.keys)//2],
            children=node.children[:len(node.children)//2+1]
        )
        right_node = Node(
            keys=node.keys[len(node.keys)//2:],
            children=node.children[len(node.children)//2:]
        )
        key = right_node.keys.pop(0)
        
        return left_node, right_node, key
            
    def search(self, node, term):
        if not self.root:
            return False
        index = 0
        for key in node.keys:
            if key == term:
                return True
            if term > key:
                index += 1
        if node.is_leaf():
            return False
        
        return self.search(node.children[index], term)

class NodeKey:
    # Re-implement the comparison operators so we take into account the key: value nature of our node to use in the BTreeIndex.
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __repr__(self):
        return '<NodeKey: ({}, {})>'.format(self.key, self.value)
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key
        return self.key == other
    
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.key > other.key
        return self.key > other
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.key >= other.key
        return self.key >= other
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.key < other.key
        return self.key < other
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.key <= other.key
        return self.key <= other


class BTreeIndex(BTree):
    # We use the nodekeys here as a data structure. E.g. greater than will return the nodekeys that are greater than some value.
    def search(self, node, term):
        if not self.root:
            return None
        index = 0
        for key in node.keys:
            if key == term:
                return key.value
            if term > key:
                index += 1
        if node.is_leaf():
            return None

        return self.search(node.children[index], term)

    def greater_than(self, node, term, upper_bound=None, inclusive=False):
        if not self.root:
            return []
        index = 0
        values = []
        for key in node.keys:
            if upper_bound is not None:
                if inclusive and key == upper_bound:
                    values.append(key)
                if key >= upper_bound:
                    break
            if term > key:
                index += 1
                continue
            if inclusive and key == term:
                values.append(key)
            if key > term:
                values.append(key)
            if not node.is_leaf():
                values += self.greater_than(node.children[index], term, upper_bound, inclusive)
            index += 1
        if not node.is_leaf():
            values += self.greater_than(node.children[index], term, upper_bound, inclusive)

        return values

    def less_than(self, node, term, lower_bound=None, inclusive=False):
        if not self.root:
            return []
        index = 0
        values = []
        for key in node.keys:
            if lower_bound is not None:
                if inclusive and key == lower_bound:
                    values.append(key)
                if key < lower_bound:
                    index += 1
                    continue
            if inclusive and key == term:
                values.append(key)
            if key < term:
                values.append(key)
            if not node.is_leaf():
                values += self.less_than(node.children[index], term, lower_bound, inclusive)
            index += 1
                
        if not node.is_leaf() and key <= term:
            values += self.less_than(node.children[index], term, lower_bound, inclusive)
        return values
