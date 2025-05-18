class Graph():

    """
    Simple parent class used for child classes DirectedGraph and UndirectedGraph. Not meant to be instantiated.
    """
    #decided to use sets for the .vertices attribute, .edges is easier to implement as a dictionary

    def __init__(self):

        self.edges = {}         #stores edges and the connected vertices as a dictionary (key: edge, value: vertices)
        self.vertices = set()   #lists all created vertices


    def __iter__(self):
        """
        Allows iteration over vertices: for v in graph.
        """

        return iter(self.vertices)

    def __len__(self):
        """
        Allows len(graph) to return the number of vertices.
        """
        return len(self.vertices)

    def __getitem__(self, key):
        """
        Allows graph[key] to access a vertex.
        If key is an int, returns the vertex with that key (if you use integer keys).
        If key is a Vertex, returns the vertex if present.
        """
        # If vertices are stored as a set, convert to list for index access
        if isinstance(key, int):
            # Try to get by .key attribute
            for v in self.vertices:
                if v.key == key:
                    return v
            raise KeyError(f"No vertex with key {key}")
        
    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return f"Graph with {len(self.vertices)} vertices and {len(self.edges)} edges."
        

    def get_edges(self):
        """
        Returns the set of edges in the graph.
        """
        return list(self.edges.keys())
    
    def get_vertices(self):
        """
        Returns the set vertices of the graph.
        """
        return list(self.vertices)
    
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph. Comparable with Vertex.add_to_graph() method.
        """
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph. Comparable with Vertex.remove_from_graph() method.
        """
        vertex.remove_from_graph(self)
    
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
