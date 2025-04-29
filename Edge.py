class UnorderedEdge():      #used exclusively with graph type Unordered
    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertexes = {vertex1, vertex2} #stored as a set

    def __repr__(self):
        return f"(Unordered edge connecting {self.vertexes} with weight {self.weight})"

class OrderedEdge():        #used exclusively with graph type Ordered
    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertexes = (vertex1, vertex2) #stored as a tuple

    def __repr__(self):
        return f"(Ordered edge connecting {self.vertexes[0]} to {self.vertexes[1]} with weight {self.weight})"