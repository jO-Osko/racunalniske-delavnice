# -*- coding: utf-8 -*-


class Graph:
    def __init__(self, vertexes):
        if isinstance(vertexes, list):
            self.vertexes = vertexes
        else:
            self.vertexes = list(vertexes)


class Vertex:
    def __init__(self, vertex_uid, name: str, edges=None):
        self.vertex_uid = vertex_uid
        self.name = name
        self.edges = edges or []

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return self.name


class Edge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end
