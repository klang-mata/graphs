from graphs import (vertex, edge, graph, graph_tools)

def main():
    graph1 = graph.UndirectedGraph()
    node0 = vertex.Vertex()
    node1 = vertex.Vertex()
    node2 = vertex.Vertex()
    node3 = vertex.Vertex()
    node4 = vertex.Vertex()
    node5 = vertex.Vertex()

    print(graph1)

    node0.add_to_graph(graph1)
    node1.add_to_graph(graph1)
    node2.add_to_graph(graph1)
    node3.add_to_graph(graph1)
    node4.add_to_graph(graph1)
    node5.add_to_graph(graph1)

    print(graph1)

    node0.add_neighbor(1)
    node1.add_neighbor(2)
    node2.add_neighbor(3)
    node3.add_neighbor(4)
    node0.add_neighbor(4)

    print(graph1)

    dfsresult = graph_tools.GraphTools.depth_first(graph1, 0, 4)
    #print(dfsresult)

    bfsresult = graph_tools.GraphTools.breadth_first(graph1, 0)
    #print(bfsresult)

    dijkstraresult = graph_tools.GraphTools.dijkstra(graph1, 0, 2)
    #print(dijkstraresult)

    cycleresult = graph_tools.GraphTools.detect_cycle(graph1)
    #print(cycleresult)

    list_of_vertices = graph_tools.GraphTools.generate_vertices(10)

    for v in list_of_vertices.keys():
        list_of_vertices[v].add_to_graph(graph1)

    print(graph1)

    list_of_vertices[6].add_neighbor(0)
    
    grid_of_vertices = graph_tools.GraphTools.grid(graph1, 3, 3)

    print(graph1)


main()