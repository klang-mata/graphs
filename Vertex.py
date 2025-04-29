import Edge
class Vertex():
    def __init__(self, graph):
        self.graph = graph 
        self.neighbors = {}
        self.graph.vertexes.append(self)
        self.key = self.graph.counter
        self.graph.counter += 1

    def __repr__(self):
        return f"(Vertex with key {self.key})"

    def add_neighbor(self, neighbor_key, weight = 1):       #adds an edge between to vertices

        neighbor = next((v for v in self.graph.vertexes if v.key == neighbor_key), None)
        if neighbor != self:
            if self.graph.type == "Unordered":
                edge = Edge.UnorderedEdge(self, neighbor, weight)
                self.neighbors[neighbor] = edge
                neighbor.neighbors[self] = edge

            elif self.graph.type == "Ordered":
                edge = Edge.OrderedEdge(self, neighbor, weight)
                self.neighbors[neighbor] = edge


    def remove_neighbor(self, neighbor_key):    #disconnects two vertices
        neighbor = next((v for v in self.graph.vertexes if v.key == neighbor_key), None)
        self.neighbors.pop(neighbor)
        if self.graph.type == "Unordered":      #also removes the connection from the other vertex if edge is unordered
            neighbor.neighbors.pop(self)

    def get_weight(self, neighbor):             #returns weight of edge connecting node and its neighbor
        return self.neighbors[neighbor].weight
    
    def get_neighbors(self):                    #returns a list of neighbors
        return self.neighbors.keys()

    
    def get_degree(self):                       #returns the degree of a vertex (how many outgoing edges it has)
        return len(self.get_neighbors())
    
    def print_neighbors(self):                  #augmented .get_neigbhors() for printing into console
        for n in self.neighbors:
            print(n)