from .vertex import Vertex
from .graph import Graph

class GraphTools():

    @staticmethod
    def depth_first(graph : Graph, start_vertex_key : int, end_vertex_key : int = None):  
        
        """
        Static method for searching a graph depth first, starting from the specified vertex.
        If no end vertex is specified, searches the whole graph and returns the entire path,
        if an end vertex is specified, returns only the path leading to that vertex.
        """

        complete = set()
        path = []
        start_vertex = next((v for v in graph.vertices if v.key == start_vertex_key), None)
        end_vertex = next((v for v in graph.vertices if v.key == end_vertex_key), "0")

        def dfs_recursive(vertex : Vertex):             #recursively searches the whole graph using DFS
            complete.add(vertex)
            path.append(vertex.key)

            for neighbor in vertex.get_neighbors():
                if neighbor not in complete:
                    dfs_recursive(neighbor)

        def dfs_recursive_search(vertex : Vertex):      #searches for a specified vertex, if found returns the path
            
            complete.add(vertex)
            path.append(vertex.key)
            
            if vertex.key == end_vertex_key:
                print("Path found!")
                return True
            
            for neighbor in vertex.get_neighbors():
                if neighbor not in complete:
                    if dfs_recursive_search(neighbor):
                        return True
                    
            path.pop()
            return False
        
        if not end_vertex:                              #if no end vertex specified
            dfs_recursive(start_vertex)

        elif end_vertex != "0":
            if not dfs_recursive_search(start_vertex):  #returns path and prints "Path found!" if path found, this takes care of the other possibility
                print("Path not found")

        elif end_vertex == "0":
            print("No vertex with this key")

        return path
    
    @staticmethod

    def breadth_first(graph : Graph, start_vertex_key : int, end_vertex_key : int = None):  
        
        """
        Static method for searching a graph breadth first, starting from the specified vertex.
        If no end vertex is specified, searches the whole graph and returns the entire path,
        if an end vertex is specified, returns only the path leading to that vertex.
        """
        
        path = []
        queue = []              #stores the queue of searching, works FIFO
        complete = set()    
        start_vertex = next((v for v in graph.vertices if v.key == start_vertex_key), None)
        end_vertex = next((v for v in graph.vertices if v.key == end_vertex_key), None)

        queue.append(start_vertex)
        complete.add(start_vertex)

        if not end_vertex:      #searches the whole graph, works when no end vertex is specified
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                for v in vertex.get_neighbors():
                    if v not in complete:
                        complete.add(v)
                        queue.append(v)
            
            return path
        
        elif end_vertex:        #searches the graph for a specific vertex
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                for v in vertex.get_neighbors():
                    if v.key not in complete and v != end_vertex:
                        complete.add(v.key)
                        queue.append(v)

                    elif v.key not in complete and v == end_vertex:
                        path.append(v.key) 
                        print("Path found!")
                        return path

            print("Path not found.")
            return path
        

    @staticmethod
    
    def dijkstra(graph : Graph, start_vertex_key : int, end_vertex_key : int = None):
        """
        Uses Dijkstras algorithm to search most optimal paths to other vertices. If end vertex is specified,
        returns the shortest path to it, if not returns shortest path to each vertex.
        """

        start_vertex = graph.vertices[start_vertex_key]
        end_vertex = graph.vertices[end_vertex_key]

        A = {}      #dictionary VERTEX : COST
        path = {}   #dictionary VERTEX : PREVIOUS VERTEX

        complete = set()
        for n in graph.vertices:
            if n is start_vertex_key:
                A[n] = 0
            else:
                A[n] = float('inf') 
        
        def dijkstra_recursive(vertex : Vertex):  
            complete.add(vertex)

            if vertex == end_vertex:        #base case
                return

            for neighbor in vertex.get_neighbors():
                if neighbor not in complete:
                    new_distance = vertex.get_weight(neighbor) + A[vertex]
                    if new_distance < A[neighbor]:
                        A[neighbor] = new_distance
                        path[neighbor] = vertex

                    dijkstra_recursive(neighbor)

        dijkstra_recursive(start_vertex)

        if end_vertex_key is not None:

            # Reconstruct the path to the end vertex

            shortest_path = []
            current_vertex_key = end_vertex_key
            while current_vertex_key is not None:
                shortest_path.append(current_vertex_key)
                current_vertex_key = path.get(current_vertex_key)
            shortest_path.reverse()
            return shortest_path
        else:
            return {vertex: path.get(vertex, None) for vertex in graph.vertices}
                

    @staticmethod
    def connect_all(graph : Graph):

        """
        Static method used for connecting all vertices in a graph, works for both undirected and directed graphs.
        """

        for v in graph.vertices:
            for u in graph.vertices:
                v.add_neighbor(u.key)