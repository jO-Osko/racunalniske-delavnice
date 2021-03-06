# -*- coding: utf-8 -*-
from DijkstraUntyped.Graph import Vertex, Edge
from DijkstraUntyped.dijkstra import dijkstra


def test_dijkstra():
    A = Vertex(1, "A")
    B = Vertex(2, "B")
    C = Vertex(3, "C")
    D = Vertex(4, "D")
    E = Vertex(5, "E")
    F = Vertex(6, "F")

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

    print(dijkstra(A))


def main():
    test_dijkstra()


if __name__ == '__main__':
    main()
