from .edge import UnorderedEdge
from .edge import OrderedEdge
from .graph import(Graph, UnorderedGraph, OrderedGraph)

class Vertex():

    """
    Class for representing individual vertexes of a graph. Also contains method for connecting and disconnecting
    neighbors as well as some utility methods (like get_degree()). Object ID is implemented through a counter
    in the Graph object, referred to as the .key attribute.
    """

    def __init__(self, graph : Graph):
        self.graph = graph 
        self.neighbors = {}
        self.graph.vertexes.append(self)
        self.key = self.graph.counter
        self.graph.counter += 1

    def __repr__(self):
        return f"(Vertex with key {self.key})"

    def add_neighbor(self, neighbor_key : int, weight : int = 1):

        """
        Method for adding a neighbor to a vertex. Works for both unordered and ordered graphs.
        As an input parameter, takes the neighbors .key, not the object itself.
        """

        neighbor = next((v for v in self.graph.vertexes if v.key == neighbor_key), None)
        if neighbor != self:
            if (type(self.graph) is UnorderedGraph):
                edge = UnorderedEdge(self, self.graph, neighbor, weight)
                self.neighbors[neighbor] = edge
                neighbor.neighbors[self] = edge

            elif (type(self.graph) is OrderedGraph):
                edge = OrderedEdge(self, self.graph, neighbor, weight)
                self.neighbors[neighbor] = edge


    def remove_neighbor(self, neighbor_key : int):

        """
        Method for removing neighbors of a vertex. If ordered, only removes the self -> neighbor edge.
        As an input parameter, takes the neighbors .key, not the object itself.
        """

        neighbor = next((v for v in self.graph.vertexes if v.key == neighbor_key), None)
        self.graph.edges = {{key:val for key, val in self.graph.edges.items() if (val != (self, self.graph.vertexes[neighbor_key]) and val != {self, self.graph.vertexes[neighbor_key]})}}
        self.neighbors.pop(neighbor)
        if (type(self.graph) is UnorderedGraph):    #also removes the connection from the other vertex if edge is unordered
            neighbor.neighbors.pop(self)

    def get_weight(self, neighbor : 'Vertex'):      
        
        """
        Returns weight of edge connecting node and its neighbor
        """

        return self.neighbors[neighbor].weight
    
    def get_neighbors(self):          
        
        """
        Returns a list of neighbors
        """

        return self.neighbors.keys()

    def get_degree(self):                           
        
        """
        Returns the degree of a vertex (how many outgoing edges it has)
        """

        return len(self.get_neighbors())
    
    def print_neighbors(self):           
        
        """
        Augmented .get_neigbhors() for printing into console
        """
        
        for n in self.neighbors:
            print(n)