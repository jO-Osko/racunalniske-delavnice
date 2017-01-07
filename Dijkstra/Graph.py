# -*- coding: utf-8 -*-
from typing import Iterable, Optional, Union, Any, NewType


class GraphItems:
    def __init__(self, vertexes: Iterable["Vertex"]) -> None:
        self._vertexes = {v.name: v for v in vertexes}

    def __getattr__(self, item: str) -> "Vertex":
        try:
            return self._vertexes[item]
        except KeyError:
            pass
        raise AttributeError("'{klass}' object has no attribute '{attr_name}'".format(klass=self.__class__.__name__,
                                                                                      attr_name=item))


class Graph:
    __slots__ = (
        "vertexes",
        "items",
    )

    def __init__(self, vertexes: Iterable["Vertex"]) -> None:
        if isinstance(vertexes, list):
            self.vertexes = vertexes
        else:
            self.vertexes = list(vertexes)
        self.items = GraphItems(self.vertexes)


class Vertex:
    __slots__ = (
        "vertex_uid",
        "name",
        "edges",
    )

    VertexUid = NewType("VertexUid", int)

    def __init__(self, vertex_uid: VertexUid, name: str, edges: Optional[Iterable["Edge"]] = None) -> None:
        self.vertex_uid = vertex_uid  # type: Vertex.VertexUid
        self.name = name
        self.edges = edges or []  # type: Iterable[Edge]

    def __lt__(self, other: "Vertex") -> bool:
        return self.name < other.name

    def __repr__(self) -> str:
        return self.name


class Edge:
    __slots__ = (
        "_weight",
        "start",
        "end",
    )

    def __init__(self, weight: float, start: Vertex, end: Vertex) -> None:
        self._weight = weight
        self.start = start
        self.end = end

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: Union[int, float]) -> None:
        if isinstance(new_weight, int) or isinstance(new_weight, float):
            if new_weight < 0:
                raise ValueError("Weight can't be negative")
            self._weight = float(new_weight)
        else:
            raise TypeError("Weight must be a number")

    # Or

    # def __setattr__(self, key: str, value: Any):
    #     if key == "weight":
    #         if isinstance(value, int) or isinstance(value, float):
    #             if value < 0:
    #                 raise ValueError("Weight can't be negative")
    #             self._weight = float(value)
    #         else:
    #             raise TypeError("Weight must be a number")
    #     super().__setattr__(key, value)
