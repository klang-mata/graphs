class GraphTools():

    @staticmethod
    def depth_first(graph, start_vertex_key, end_vertex_key = None):  #if no end vertex specified, searches the whole graph
        complete = set()
        path = []
        start_vertex = next((v for v in graph.vertexes if v.key == start_vertex_key), None)
        end_vertex = next((v for v in graph.vertexes if v.key == end_vertex_key), None)

        def dfs_recursive(vertex):    #recursively searches the whole graph using DFS
            complete.add(vertex)
            path.append(vertex.key)

            for neighbor in vertex.get_neighbors():
                if neighbor not in complete:
                    dfs_recursive(neighbor)

        def dfs_recursive_search(vertex):   #searches for a specified vertex, if found returns the path, if not returns the whole path walked
            complete.add(vertex)
            path.append(vertex.key)
            
            if vertex.key == end_vertex_key:
                return True
            
            for neighbor in vertex.get_neighbors():
                if neighbor not in complete:
                    if dfs_recursive_search(neighbor):
                        return True
                    
            path.pop()
            return False
        
        if end_vertex == None:
            dfs_recursive(start_vertex)

        else:
            if not dfs_recursive_search(start_vertex):
                print("Path not found")

        return path
    


    @staticmethod
    def breadth_first(graph, start_vertex_key, end_vertex_key = None):
        path = []
        queue = []
        complete = set()
        start_vertex = next((v for v in graph.vertexes if v.key == start_vertex_key), None)
        end_vertex = next((v for v in graph.vertexes if v.key == end_vertex_key), None)


        queue.append(start_vertex)
        complete.add(start_vertex)

        if end_vertex == None:
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                for v in vertex.get_neighbors():
                    if v not in complete:
                        complete.add(v)
                        queue.append(v)
            
            return path
        
        elif end_vertex != None:
            while queue:
                vertex = queue.pop(0)
                path.append(vertex.key)

                if vertex.key == end_vertex_key:
                    print("Path found!")
                    return path

                for v in vertex.get_neighbors():
                    if v not in complete:
                        complete.add(v)
                        queue.append(v)

            print("Path not found.")
            return path

    @staticmethod
    def connect_all(graph):
        for v in graph.vertexes:
            for u in graph.vertexes:
                v.add_neighbor(u.key)