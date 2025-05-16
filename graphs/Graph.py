class Graph():

    """
    Simple parent class used for child classes DirectedGraph and UndirectedGraph. Not meant to be instantiated.
    """
    #decided to use sets for the .vertices attribute, .edges is easier to implement as a dictionary

    def __init__(self):

        self.edges = {}      #stores edges and the connected vertices as a dictionary
        self.vertices = set()   #lists all created vertices
        self.counter = 0        #assigns key numbers to vertices

class DirectedGraph(Graph):
    """
    Class for directed graphs. Vertex of this class of graphs are connected using the DirectedEdge class.
    """
    def __init__(self):
        super().__init__()

class UndirectedGraph(Graph):

    """
    Class for undirected graphs. Vertex of this class of graphs are connected using the UndirectedEdge class.
    """

    def __init__(self):
        super().__init__()