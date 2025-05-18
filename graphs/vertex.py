from .graph import Graph, UndirectedGraph, DirectedGraph

class Vertex:
    """
    Class for representing individual vertices of a graph. Also contains methods for connecting and disconnecting
    neighbors as well as some utility methods (like get_degree()). Object ID is implemented through a counter
    in the Graph object, referred to as the .key attribute.
    """
    _id_counter = 0     #class variable
    vertex_keys = {}    # dict ID:vertex, succeeds the former generator expressions

    def __init__(self, key : int = None):
        if key is not None:
            if key in Vertex.vertex_keys:
                raise ValueError(f"Vertex with key {key} already exists.")
            self.key = key
        else:
            self.key = Vertex._id_counter
            Vertex._id_counter += 1
        self.neighbors = {}
        self.graphs = set()
        Vertex.vertex_keys[self.key] = self
    
    def __str__(self):
        return f"(Vertex with ID {self.key})"
    
    def __repr__(self):
        return f"(ID: {self.key}, neighbors: {self.neighbors}, part of graph(s): {self.graphs})"
    

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
        self.remove_all(graph)

        if graph.type == DirectedGraph:             #also takes care of removing the inbound edges
            for edge in list(graph.edges.keys()):
                if self in graph.edges[edge]:
                    vertex = [v for v in graph.edges[edge] if vertex != self]
                    vertex.neighbors.pop(self)
                    del graph.edges[edge]

        self.graphs.remove(graph)
        graph.vertices.remove(self)
        self.remove_all(graph)
        del Vertex.vertex_keys[self.key]


    def add_neighbor(self, neighbor_key: int, *,weight: int = 1):

        """
        Method for adding a neighbor to a vertex. Works for both undirected and directed graphs.
        As an input parameter, takes the neighbors .key, not the object itself. If vertex is a part of multiple graphs,
        the method will add the neighbor to all of them.
        """

        from .edge import UndirectedEdge, DirectedEdge          #avoids circular import

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
        Method for removing all neighbors (in a specified graph) of a vertex. If directed, only removes the self -> neighbor edge.
        """
        for vertex in graph.vertices:
            self.remove_neighbor(vertex.key)


    def get_weight(self, neighbor: 'Vertex'):
        """
        Returns weight of edge connecting vertex and its neighbor
        """
        return self.neighbors[neighbor].weight

    def get_neighbors(self, graph: Graph = None):
        """
        Returns a list of neighbors. If a grapg is specified, returns only the neighbors in that graph.
        """

        if graph is not None:
            if graph not in self.graphs:
                raise ValueError(f"Vertex {self.key} is not part of the specified graph.")
            return [n for n in self.neighbors if n.graphs == graph]
        
        else:
            return list(self.neighbors.keys())

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
