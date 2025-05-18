from .vertex import Vertex
from .graph import Graph

class GraphTools():

    @staticmethod
    def depth_first(graph: Graph, start_vertex_key: int, end_vertex_key: int = None):

        """
        Static method for searching a graph depth first, starting from the specified vertex.
        If no end vertex is specified, searches the whole graph and returns the entire path,
        if an end vertex is specified, returns only the path leading to that vertex.
        """
        complete = set()
        path = []

        start_vertex = Vertex.vertex_keys.get(start_vertex_key, None)
        end_vertex = Vertex.vertex_keys.get(end_vertex_key, None)

        def dfs_recursive(vertex: Vertex):
            complete.add(vertex)
            path.append(vertex.key)
            for neighbor in vertex.get_neighbors(graph):
                if neighbor not in complete:
                    dfs_recursive(neighbor)

        def dfs_recursive_search(vertex: Vertex):
            complete.add(vertex)
            path.append(vertex.key)
            if vertex.key == end_vertex_key:
                return True
            for neighbor in vertex.get_neighbors(graph):
                if neighbor not in complete:
                    if dfs_recursive_search(neighbor):
                        return True
            path.pop()
            return False

        if end_vertex_key is None:
            dfs_recursive(start_vertex)
        elif end_vertex is not None:
            dfs_recursive_search(start_vertex)
        else:
            print("No vertex with this key")

        return path


    @staticmethod

    def breadth_first(graph : Graph, start_vertex_key : int, end_vertex_key : int = None):  
        
        """
        Static method for searching a graph breadth first, starting from the specified vertex.
        If no end vertex is specified, searches the whole graph and returns the entire path,
        if an end vertex is specified, returns only the path leading to that vertex (returns [] when no path found).
        """
        
        path = []
        queue = []              #stores the queue of searching, works FIFO
        complete = set()    
        start_vertex = Vertex.vertex_keys.get(start_vertex_key, None)
        end_vertex = Vertex.vertex_keys.get(end_vertex_key, None)

        queue.append(start_vertex)
        complete.add(start_vertex)

        if not end_vertex:      #searches the whole graph, works when no end vertex is specified
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                for v in vertex.get_neighbors(graph):
                    if v not in complete:
                        complete.add(v)
                        queue.append(v)
            
            return path
        
        elif end_vertex:        #searches the graph for a specific vertex
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                for v in vertex.get_neighbors(graph):
                    if v.key not in complete and v != end_vertex:
                        complete.add(v.key)
                        queue.append(v)

                    elif v.key not in complete and v == end_vertex:
                        path.append(v.key) 
                        return path

            return path
        

    @staticmethod
    def dijkstra(graph: Graph, start_vertex_key: int, end_vertex_key: int = None):
        """
        Uses Dijkstra's algorithm to search most optimal paths to other vertices. If end vertex is specified,
        returns the shortest path to it (if no path found returns []), if no end specified returns shortest path to each vertex. 
        """
        
        import heapq

        distances = {v.key: float('inf') for v in graph.vertices}
        previous = {v.key: None for v in graph.vertices}
        distances[start_vertex_key] = 0

        heap = [(0, start_vertex_key)]      #min-heap priority queue

        visited = set()

        while heap:
            current_distance, current_key = heapq.heappop(heap)
            if current_key in visited:
                continue
            visited.add(current_key)
            current_vertex = next((v for v in graph.vertices if v.key == current_key), None)
            if current_vertex is None:
                continue
            for neighbor in current_vertex.get_neighbors(graph):
                weight = current_vertex.get_weight(neighbor)
                distance = current_distance + weight
                if distance < distances[neighbor.key]:
                    distances[neighbor.key] = distance
                    previous[neighbor.key] = current_key
                    heapq.heappush(heap, (distance, neighbor.key))

        if end_vertex_key is not None:
            # Reconstruct the path to the end vertex
            shortest_path = []
            current = end_vertex_key
            if distances[current] == float('inf'):
                return []
            while current is not None:
                shortest_path.append(current)
                current = previous[current]
            shortest_path.reverse()
            return shortest_path
        else:
            # Return shortest paths to all vertices
            return {key: previous[key] for key in distances}
        

    @staticmethod

    def detect_cycle(graph: Graph):

        """
        Detects cycles in a graph using depth-first search. Returns True if a cycle is found, False otherwise.
        """
        from .graph import DirectedGraph, UndirectedGraph

        visited = set()

        if isinstance(graph, DirectedGraph):
            # Directed graph: use recursion stack
            rec_stack = set()

            def dfs(vertex):
                visited.add(vertex)
                rec_stack.add(vertex)
                for neighbor in vertex.get_neighbors(graph):
                    if neighbor not in visited:
                        if dfs(neighbor):
                            return True
                    elif neighbor in rec_stack:
                        # Found a cycle
                        return True
                rec_stack.remove(vertex)
                return False

            for vertex in graph.vertices:
                if vertex not in visited:
                    if dfs(vertex):
                        return True
            return False

        else:
            # Undirected graph: use parent tracking
            def dfs(vertex, parent):
                visited.add(vertex)
                for neighbor in vertex.get_neighbors(graph):
                    if neighbor not in visited:
                        if dfs(neighbor, vertex):
                            return True
                    elif neighbor != parent:
                        # Found a back edge (cycle)
                        return True
                return False

            for vertex in graph.vertices:
                if vertex not in visited:
                    if dfs(vertex, None):
                        return True
            return False

    @staticmethod
    def connect_all(graph : Graph):

        """
        Static method used for connecting all vertices in a graph, works for both undirected and directed graphs.
        """

        for v in graph.vertices:
            for u in graph.vertices:
                v.add_neighbor(u.key)

    @staticmethod
    def disconnect_all(graph : Graph):

        """
        Static method used for disconnecting all vertices in a graph, works for both undirected and directed graphs.
        """

        for v in graph.vertices:
            for u in graph.vertices:
                v.remove_neighbor(u.key)

    @staticmethod
    def grid(graph: Graph, size_a: int, size_b: int):
        """
        Creates a grid of vertices in the specified graph. The grid is created by adding neighbors to each vertex. 
        The grid is represented as a 2D list of vertices, which is returned after the grid is created.
        """
        for i in range(size_a):
            for j in range(size_b):
                vertex = Vertex()
                vertex.add_to_graph(graph)
                if i > 0:
                    vertex.add_neighbor((i - 1) * size_b + j)
                if j > 0:
                    vertex.add_neighbor(i * size_b + (j - 1))

                # Store vertices in a 2D list
                if i == 0 and j == 0:
                    grid_vertices = [[vertex]]
                elif j == 0:
                    grid_vertices.append([vertex])
                else:
                    grid_vertices[i].append(vertex)

                # After grid creation, return 2D list of vertices resembling the grid
                if i == size_a - 1 and j == size_b - 1:
                    return grid_vertices
    
    @staticmethod
    def generate_vertices(count):
        """
        Returns a dict of Vertex objects, accessible by key: dict_vertices[0], dict_vertices[1], etc.
        """
        nodes = {}
        for i in range(count):
            v = Vertex()
            nodes[v.key] = v
            i -=1
        return nodes
