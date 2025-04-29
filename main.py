import Graph
import Edge
import Vertex
import GraphTools
def main():
    graph = Graph.Graph("Unordered")
    node0 = Vertex.Vertex(graph)
    node1 = Vertex.Vertex(graph)
    node2 = Vertex.Vertex(graph)
    node3 = Vertex.Vertex(graph)
    node4 = Vertex.Vertex(graph)
    node5 = Vertex.Vertex(graph)
    node6 = Vertex.Vertex(graph)

    node0.add_neighbor(1)
    node0.add_neighbor(2)
    node1.add_neighbor(3)
    node2.add_neighbor(4)
    node3.add_neighbor(5)
    node4.add_neighbor(6)
    node5.add_neighbor(0)

    dfsresult = GraphTools.GraphTools.depth_first(graph, 0, 2)
    print(dfsresult)

    bfsresult = GraphTools.GraphTools.breadth_first(graph, 0, 2)
    print(bfsresult)


main()

#TODO:
#   use vertex or vertex_key for adding edges? (probably vertex_key but its harder to implement) - done
#   depth first search - DOESNT RETURN CORRECT PATH WHEN SEARCHING FOR A VERTEX
#   breadth first search - done
#   dijkstra
#   detect cycles
#   make a Graph.grid(size_a, size_b) method for demonstrating pathfinding?
#   simple UI for visual demonstration
#   error handling, optimization, QOL and utility