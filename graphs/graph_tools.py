class GraphTools():

    @staticmethod
    def depth_first(graph, start_vertex_key, end_vertex_key = None):  #if no end vertex specified, searches the whole graph
        complete = set()
        path = []
        start_vertex = next((v for v in graph.vertexes if v.key == start_vertex_key), None)
        end_vertex = next((v for v in graph.vertexes if v.key == end_vertex_key), "0")

        def dfs_recursive(vertex):    #recursively searches the whole graph using DFS
            complete.add(vertex)
            path.append(vertex.key)

            for neighbor in vertex.get_neighbors():
                if neighbor not in complete:
                    dfs_recursive(neighbor)

        def dfs_recursive_search(vertex):   #searches for a specified vertex, if found returns the path
            
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
        
        if not end_vertex:                      #if no end vertex specified
            dfs_recursive(start_vertex)

        elif end_vertex != "0":
            if not dfs_recursive_search(start_vertex): #returns path and prints "Path found!" if path found, this takes care of the other possibility
                print("Path not found")

        elif end_vertex == "0":
            print("No vertex with this key")

        return path
    


    @staticmethod
    def breadth_first(graph, start_vertex_key, end_vertex_key = None):  #if no end vertex specified, searches the whole graph
        path = []
        queue = []  #stores the queue of searching, works FIFO
        complete = set()    
        start_vertex = next((v for v in graph.vertexes if v.key == start_vertex_key), None)
        end_vertex = next((v for v in graph.vertexes if v.key == end_vertex_key), None)

        queue.append(start_vertex)
        complete.add(start_vertex)

        if not end_vertex:  #searches the whole graph, works when no end vertex is specified
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                for v in vertex.get_neighbors():
                    if v not in complete:
                        complete.add(v)
                        queue.append(v)
            
            return path
        
        elif end_vertex:    #searches the graph for a specific vertex
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                # if vertex.key == end_vertex_key: 
                #     print("Path found!")
                #     return path

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
    def connect_all(graph):
        for v in graph.vertexes:
            for u in graph.vertexes:
                v.add_neighbor(u.key)