from abc import abstractmethod, ABC

#LM: included ABC class inheritance
class Edge(ABC):

    def __init__(self):
        raise TypeError("Cannot instantiate this class directly.")

    @abstractmethod
    def __repr__(self):
        #LM: once inheriting from ABC, every `@abstractmethod`-wrapped method must be implemented before instantiating
        pass

class UnorderedEdge(Edge):      #used exclusively with graph type Unordered
    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertexes = {vertex1, vertex2} #stored as a set

    def __repr__(self):
        return f"(Unordered edge connecting {self.vertexes} with weight {self.weight})"

class OrderedEdge(Edge):        #used exclusively with graph type Ordered
    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertexes = (vertex1, vertex2) #stored as a tuple

    def __repr__(self):
        return f"(Ordered edge connecting {self.vertexes[0]} to {self.vertexes[1]} with weight {self.weight})"