class Graph():
    #LM: rename `_type`` to `type_`. The ida is not for a variable to be "pythonically private", but to avoid name collision with built-in `type()` function.
    
    #Decided to use type() for checking the graph type instead of a parameter

    def __init__(self):
        self.vertexes = []  #lists all created vertexes
        self.counter = 0    #assigns key numbers to vertexes

class OrderedGraph(Graph):
    def __init__(self, type_="Unordered"):
        super().__init__()

class UnorderedGraph(Graph):
    def __init__(self):
        super().__init__()