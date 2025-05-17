from .graph import Graph, UndirectedGraph, DirectedGraph

class Vertex:
    """
    Class for representing individual vertices of a graph. Also contains methods for connecting and disconnecting
    neighbors as well as some utility methods (like get_degree()). Object ID is implemented through a counter
    in the Graph object, referred to as the .key attribute.
    """
    _id_counter = 0  # class variable
    vertex_keys = {}

    def __init__(self, key=None):
        if key is not None:
            self.key = key
        else:
            self.key = Vertex._id_counter
            Vertex._id_counter += 1
        self.neighbors = {}
        self.graphs = set()
        Vertex.vertex_keys[self.key] = self

    def __repr__(self):
        return f"(Vertex with key {self.key})"
    

    def add_to_graph(self, graph: Graph):
        """
        Add this vertex to a graph.
        """
        self.graphs.add(graph)
        graph.vertices.add(self)
        
    def remove_from_graph(self, graph: Graph):
        """
        Remove this vertex from a graph.
        """
        self.graphs.remove(graph)
        graph.vertices.remove(self)
        self.remove_all(graph)

    def add_neighbor(self, neighbor_key: int, *,weight: int = 1):

        """
        Method for adding a neighbor to a vertex. Works for both undirected and directed graphs.
        As an input parameter, takes the neighbors .key, not the object itself.
        """

        from .edge import UndirectedEdge, DirectedEdge

        for graph in self.graphs:
            neighbor = Vertex.vertex_keys.get(neighbor_key, None)
            if neighbor and neighbor != self:
                if isinstance(graph, UndirectedGraph):
                    edge = UndirectedEdge(graph, set([self, neighbor]), weight)
                    self.neighbors[neighbor] = edge
                    neighbor.neighbors[self] = edge
                elif isinstance(graph, DirectedGraph):
                    edge = DirectedEdge(graph, ((self, neighbor)), weight)
                    self.neighbors[neighbor] = edge


    def add_all(self, graph: Graph):
        """
        Method for adding all vertices in a graph as neighbors to this vertex.
        """
        for vertex in graph.vertices:
            self.add_neighbor(vertex.key)


    def remove_neighbor(self, neighbor_key: int):
        """
        Method for removing neighbors of a vertex. If directed, only removes the self -> neighbor edge.
        As an input parameter, takes the neighbors .key, not the object itself.
        """
        for graph in self.graphs:
            neighbor = Vertex.vertex_keys.get(neighbor_key, None)
            if neighbor in self.neighbors:
                graph.edges = {
                    key: val for key, val in graph.edges.items()
                    if val != (self, neighbor) and val != {self, neighbor}
                }
                self.neighbors.pop(neighbor)
                if isinstance(graph, UndirectedGraph):
                    neighbor.neighbors.pop(self)
                    

    def remove_all(self, graph: Graph):
        """
        Method for removing all neighbors of a vertex. If directed, only removes the self -> neighbor edge.
        """
        for vertex in graph.vertices:
            self.remove_neighbor(vertex.key)

    def get_weight(self, neighbor: 'Vertex'):
        """
        Returns weight of edge connecting vertex and its neighbor
        """
        return self.neighbors[neighbor].weight

    def get_neighbors(self):
        """
        Returns a list of neighbors
        """
        return set(self.neighbors.keys())

    def get_degree(self):
        """
        Returns the degree of a vertex (how many outgoing edges it has)
        """
        return len(self.get_neighbors())

    def print_neighbors(self):
        """
        Augmented .get_neighbors() for printing into console
        """
        for n in self.neighbors:
            print(n)

    def __str__(self):
        return f"(Vertex with ID {self.key})"