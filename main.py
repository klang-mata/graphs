import Graph
import Edge
import Vertex
import GraphTools
def main():
    graph = Graph.Graph("Ordered")
    node0 = Vertex.Vertex(graph)
    node1 = Vertex.Vertex(graph)
    node2 = Vertex.Vertex(graph)
    node3 = Vertex.Vertex(graph)
    node4 = Vertex.Vertex(graph)
    node5 = Vertex.Vertex(graph)

    node0.add_neighbor(1)
    node1.add_neighbor(2)
    node2.add_neighbor(3)
    node0.add_neighbor(4)
    node4.add_neighbor(5)

    dfsresult = GraphTools.GraphTools.depth_first(graph, 0, 5)
    print(dfsresult)

    bfsresult = GraphTools.GraphTools.breadth_first(graph, 0, 5)
    print(bfsresult)


main()

#TODO:
#   use vertex or vertex_key for adding edges? (probably vertex_key but its harder to implement) - done
#   depth first search - done
#   breadth first search - FIX RETURNING ONLY CORRECT PATH WHEN TARGET FOUND
#   dijkstra
#   detect cycles
#   make a Graph.grid(size_a, size_b) method for demonstrating pathfinding?
#   simple UI for visual demonstration
#   error handling, simplification, QOL features