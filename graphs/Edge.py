from abc import abstractmethod, ABC
from .graph import Graph
from .vertex import Vertex

class Edge(ABC):

    """
    Class not meant to be instantiated, serves as a parent to UndirectedEdge and DirectedEdge child classes
    """

    def __init__(self):
        raise TypeError("Cannot instantiate this class directly.")

    @abstractmethod
    def __repr__(self):
        pass


class UndirectedEdge(Edge):

    """
    Represents an undirected edge connecting two vertices. Instance is created when using the UndirectedGraph class.
    Stores the connected vertices as a set.
    """

    def __init__(self, graph : Graph, vertex1 : Vertex, vertex2 : Vertex, weight : int = 1):
        self.weight = weight
        self.vertices = {vertex1, vertex2}
        graph.edges[self] = self.vertices

    def __repr__(self):
        return f"(Undirected edge connecting {self.vertices} with weight {self.weight})"
    

class DirectedEdge(Edge):

    """
    Represents a directed (one-way) edge connecting two vertices. 
    Instance is created when using the DirectedGraph class. Stores the connected vertices as a tuple.
    """

    def __init__(self, graph: Graph, vertices: tuple[Vertex, Vertex], *, weight: int = 1):

        self.weight = weight
        self.vertices = vertices
        graph.edges[self] = self.vertices

    def __repr__(self):
        return f"(Directed edge connecting {self.vertices[0]} to {self.vertices[1]} with weight {self.weight})"