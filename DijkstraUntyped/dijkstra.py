# -*- coding: utf-8 -*-
from collections import defaultdict

from .PriorityQueue import PriorityQueue


def dijkstra(start):

    out = [(start, 0)]

    visited = defaultdict(bool)

    current = start
    visited[current] = True

    neigh = [(edge.end, edge.weight) for edge in start.edges]

    queue = PriorityQueue(neigh)

    def add_neighbours_to_queue(vertex, pre_cost):
        for edge in vertex.edges:
            if not visited[edge]:
                queue.insert(pre_cost + edge.weight, edge.end)

    while not queue.is_empty():
        current_cost, current = queue.pop()

        if visited[current]:
            continue

        out.append((current, current_cost))
        add_neighbours_to_queue(current, current_cost)

        visited[current] = True

    return out
