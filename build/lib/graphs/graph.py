class Graph():

    """
    Simple parent class used for child classes OrderedGraph and UnorderedGraph. Not meant to be instantiated.
    """

    def __init__(self):
        self.vertexes = []  #lists all created vertexes
        self.counter = 0    #assigns key numbers to vertexes

class OrderedGraph(Graph):

    """
    Class for ordered graphs. Vertex of this class of graphs are connected using the OrderedEdge class.
    """

    def __init__(self):
        super().__init__()

class UnorderedGraph(Graph):

    """
    Class for unordered graphs. Vertex of this class of graphs are connected using the UnorderedEdge class.
    """

    def __init__(self):
        super().__init__()