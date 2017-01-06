# -*- coding: utf-8 -*-
from collections import defaultdict

from typing import Dict, List, TypeVar
from typing import Tuple

from .Graph import Vertex
from .PriorityQueue import PriorityQueue


def dijkstra(start: Vertex) -> List[Tuple[Vertex, float]]:

    out = [(start, 0)]  # type: List[Tuple[Vertex, float]]

    visited = defaultdict(bool)  # type: Dict[Vertex, bool]

    current = start
    visited[current] = True

    neigh = [(edge.weight, edge.end) for edge in start.edges]

    # neigh_wrong = [(edge.end, 0) for edge in start.edges]
    # queue2 = PriorityQueue(neigh_wrong)

    # Does not infer type :(
    queue = PriorityQueue(neigh)  # type: PriorityQueue[Vertex]

    def add_neighbours_to_queue(vertex: Vertex, pre_cost: float = 0) -> None:
        for edge in vertex.edges:
            # Error: visited[edge]
            if not visited[edge.end]:
                queue.insert(pre_cost + edge.weight, edge.end)

    while not queue.empty:
        current_cost, current = queue.pop()

        if visited[current]:
            continue

        out.append((current, current_cost))
        add_neighbours_to_queue(current, current_cost)

        visited[current] = True

    return out
