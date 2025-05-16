from graphs import (vertex, edge, graph, graph_tools)

def main():
    graph1 = graph.UnorderedGraph()
    node0 = vertex.Vertex(graph1)
    node1 = vertex.Vertex(graph1)
    node2 = vertex.Vertex(graph1)
    node3 = vertex.Vertex(graph1)
    node4 = vertex.Vertex(graph1)
    node5 = vertex.Vertex(graph1)

    node0.add_neighbor(1)
    node0.add_neighbor(3)
    node1.add_neighbor(2)
    node2.add_neighbor(3)
    node3.add_neighbor(4)
    node4.add_neighbor(0)
    node5.add_neighbor(0)

    dfsresult = graph_tools.GraphTools.depth_first(graph1, 0, 4)
    print(dfsresult)

    bfsresult = graph_tools.GraphTools.breadth_first(graph1, 0)
    print(bfsresult)

    node0.remove_neighbor(1)
    node0.print_neighbors()

    dijkstraresult = graph_tools.GraphTools.dijkstra(graph1, 0, 4)

#if __name__ == "test":
main()

#TODO:
#   use vertex or vertex_key for adding edges? (probably vertex_key but its harder to implement) - done
#   depth first search - done
#   breadth first search - done
#   dijkstra
#   detect cycles
#   make a Graph.grid(size_a, size_b) method for demonstrating pathfinding?
#   simple UI for visual demonstration
#   error handling, optimization, QOL and utility