# -*- coding: utf-8 -*-
from Dijkstra.Graph import Graph, Vertex, Edge
from Dijkstra.dijkstra import dijkstra


def test_dijkstra() -> None:
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    E = Vertex("E")
    F = Vertex("F")

    A.edges = [
        Edge(7, A, B),
        Edge(9, A, C),
        Edge(14, A, D),
    ]

    B.edges = [
        Edge(7, B, A),
        Edge(10, B, C),
        Edge(15, B, E),
    ]

    C.edges = [
        Edge(9, C, A),
        Edge(10, C, B),
        Edge(2, C, D),
        Edge(11, C, E),
    ]

    D.edges = [
        Edge(14, D, A),
        Edge(2, D, C),
        Edge(9, D, F),
    ]

    E.edges = [
        Edge(15, E, B),
        Edge(11, E, C),
        Edge(6, E, F),
    ]

    F.edges = [
        Edge(9, F, D),
        Edge(6, F, E),
    ]

    F.edges[0].weight = 2
    g = Graph([A, B, C, D, E, F])

    print(g.items.A.edges)

    print(dijkstra(A))


def main() -> None:
    test_dijkstra()


if __name__ == '__main__':
    main()
