# -*- coding: utf-8 -*-

import heapq

from typing import TypeVar, Generic, Iterable, Optional, Tuple, List

T = TypeVar("T")

HeapElement = Tuple[float, T]


class PriorityQueue(Generic[T]):
    __slots__ = (
        "heap",
        "insertions",
        "pops",
    )

    def __init__(self, init: Optional[Iterable[HeapElement]] = None) -> None:
        if init:
            self.heap = [j for j in init]  # type: List[HeapElement]
        else:
            self.heap = []  # type: List[HeapElement]
        heapq.heapify(self.heap)
        self.insertions = 0
        self.pops = 0

    def insert(self, priority: float, element: T) -> None:
        self.insertions += 1
        heapq.heappush(self.heap, (priority, element))

    def peek(self) -> HeapElement:
        if not self.heap:
            raise IndexError("Queue is empty")
        return self.heap[0]

    def pop(self) -> HeapElement:
        # Very smart :)
        # reveal_type(heapq.heappop(self.heap))
        self.pops += 1
        return heapq.heappop(self.heap)

    @property
    def empty(self) -> bool:
        return self.size == 0

    @property
    def size(self) -> int:
        return len(self.heap)
