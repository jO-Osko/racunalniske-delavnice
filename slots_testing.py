# -*- coding: utf-8 -*-

"""Usage of slots"""
from time import time
import sys


class Parent:
    __slots__ = (
        "a"
    )

    def __init__(self, a):
        self.a = a


class WithoutSlots(Parent):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


class WithSlots(Parent):
    __slots__ = (
        "b",
    )

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


N = 10 ** 7

with_s = time()
for j in range(N):
    temp = WithSlots(j, j)

tot_no_s = time() - with_s

print(tot_no_s)

no_s = time()
for j in range(N):
    temp = WithoutSlots(j, j)

tot_s = time() - no_s
print(tot_s)

print(1 - tot_no_s / tot_s)

# Simple size difference
no_slots = WithoutSlots(1, 2)

no_slots_size = sys.getsizeof(no_slots) + sys.getsizeof(no_slots.__dict__)

with_slots = WithSlots(1, 2)

with_slots_site = sys.getsizeof(with_slots)

print(no_slots_size - with_slots_site)
