
def main():
    graph = Graph()
    node0 = Vertex(graph)
    node1 = Vertex(graph)
    node2 = Vertex(graph)
    node3 = Vertex(graph)
    node4 = Vertex(graph)
    node5 = Vertex(graph)

    node0.add_neighbor(1)
    node0.add_neighbor(3)
    node1.add_neighbor(2)
    node2.add_neighbor(3)
    node3.add_neighbor(4)
    node4.add_neighbor(0)
    node5.add_neighbor(0)

    dfsresult = GraphTools.GraphTools.depth_first(graph, 0, 4)
    print(dfsresult)

    bfsresult = GraphTools.GraphTools.breadth_first(graph, 0)
    print(bfsresult)


if __name__ == "main":
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