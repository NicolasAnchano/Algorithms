class Node:
    # This type of node allow us to have key: value pairs to save data other than integers (as values, with ints as keys)
    ## Kinda works like a hash table when combined with the BST.
    def __init__(self, key=None, value=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __str__(self):
        return "<Node: {}>".format(self.value)

class DAG:
    # Directed Acyclic Graph
    ## Composed of vertices (nodes) and edges (arrows)
    def __init__(self):
        self.graph = {}

    def add(self, node, to=None):
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)
        searched = self.sort()
        
        # TESTS FOR CICLYCITY
        ## If  the lenght of the sorted nodes is greater than the lenght of the nodes in the graph, then it;s a cycle
        ### If there is a cycle, we will be visiting a previous node, making the visited list greater than the number of vertices
        ### in the graph
        if len(searched) != len(self.graph):
            raise Exception

    def sort(self):
        # TOPOLOGICAL SORT - In Kahn's Algorithm
        ## Determines if the graph has a cycle or not, check comment on add method
        self.in_degrees()
        to_visit = deque()
        for node in self.graph:
            if self.degrees[node] == 0:
                to_visit.append(node)
                
        searched = []
        while to_visit:
            node = to_visit.popleft()
            for pointer in self.graph[node]:
                self.degrees[pointer] -= 1
                if self.degrees[pointer] == 0:
                    to_visit.append(pointer)
            searched.append(node)
        return searched

    def in_degrees(self):
        # Degrees are the number of pointed arrows the node have - Roots will always have degree = 0
        self.degrees = {}
        for node in self.graph:
            if node not in self.degrees.keys():
                self.degrees[node] = 0
            for pointed in self.graph[node]:
                if pointed not in self.degrees.keys():
                    self.degrees[pointed] = 0
                self.degrees[pointed] += 1


class Pipeline:
    def __init__(self):
        # Using DAG instead of simple list
        self.tasks = DAG()
        
    def task(self, depends_on=None):

        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner
    
    def run(self):
        # With DAG there is no last task, so we use a dictionary to pass the input into the functions (that is, the function thas
        # has to run before the current one, to use the result as an input)
        # That way, we can use the results as the input of any function (third does not necessarily have to follow second)
        scheduled = self.tasks.sort()
        completed = {}
        for task in scheduled:
            for node, values in self.tasks.graph.items():
                if task in values:
                    completed[task] = task(completed[node])
            if task not in completed:
                completed[task] = task()
        return completed
