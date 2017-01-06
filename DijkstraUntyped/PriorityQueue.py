# -*- coding: utf-8 -*-

import heapq


class PriorityQueue:
    def __init__(self, init=None):
        if init:
            self.heap = [j for j in init]
        else:
            self.heap = []
        heapq.heapify(self.heap)
        self.insertions = 0
        self.pops = 0

    def insert(self, priority, element):
        self.insertions += 1
        heapq.heappush(self.heap, (priority, element))

    def peek(self):
        if not self.heap:
            raise IndexError("Queue is empty")
        return self.heap[0]

    def pop(self):
        self.pops += 1
        return heapq.heappop(self.heap)

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def get_size(self) -> int:
        return len(self.heap)
