# -*- coding: utf-8 -*-
from typing import Iterable, Optional


class Graph:
    __slots__ = (
        "vertexes",
    )

    def __init__(self, vertexes: Iterable["Vertex"]) -> None:
        if isinstance(vertexes, list):
            self.vertexes = vertexes
        else:
            self.vertexes = list(vertexes)


class Vertex:
    __slots__ = (
        "name",
        "edges",
    )

    def __init__(self, name: str, edges: Optional[Iterable["Edge"]] = None) -> None:
        self.name = name
        self.edges = edges or []  # type: Iterable[Edge]

    def __lt__(self, other: "Vertex") -> bool:
        return self.name < other.name

    def __repr__(self) -> str:
        return self.name


class Edge:
    __slots__ = (
        "weight",
        "start",
        "end",
    )

    def __init__(self, weight: float, start: Vertex, end: Vertex) -> None:
        self.weight = weight
        self.start = start
        self.end = end
