from abc import abstractmethod, ABC

#LM: included ABC class inheritance
class Edge(ABC):

    """
    Class not meant to be instantiated, serves as a parent to UnorderedEdge and OrderedEdge child classes
    """


    def __init__(self):
        raise TypeError("Cannot instantiate this class directly.")

    @abstractmethod
    def __repr__(self):
        #LM: once inheriting from ABC, every `@abstractmethod`-wrapped method must be implemented before instantiating
        pass



class UnorderedEdge(Edge):

    """
    Represents an unordered edge connecting two vertexes. Instance is created when using the UnorderedGraph class.
    Stores the connected vertexes as a set.
    """

    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertexes = {vertex1, vertex2}

    def __repr__(self):
        return f"(Unordered edge connecting {self.vertexes} with weight {self.weight})"
    


class OrderedEdge(Edge):

    """
    Represents an ordered (one-way) edge connecting two vertexes. 
    Instance is created when using the OrderedGraph class. Stores the connected vertexes as a tuple.
    """

    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertexes = (vertex1, vertex2) #stored as a tuple

    def __repr__(self):
        return f"(Ordered edge connecting {self.vertexes[0]} to {self.vertexes[1]} with weight {self.weight})"