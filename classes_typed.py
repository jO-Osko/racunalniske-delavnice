# -*- coding: utf-8 -*-

"""Types with classes"""
from typing import List, Optional


class Person:
    __slots__ = (
        "first_name",
        "last_name",
        "children",
        "__number_of_grandchildren"
    )

    def __init__(self, first: str, last: str, children: Optional[List["Person"]] = None) -> None:
        self.first_name = first
        self.last_name = last
        # PyCharm has problems
        # self.children = children or []
        if children is None:
            self.children = []  # type: List[Person]
        else:
            self.children = children  # type: List[Person]
        self.__number_of_grandchildren = None  # type: Optional[int]

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name

    @property
    def full_name(self) -> str:
        return self.get_full_name()

    @property
    def number_of_children(self) -> int:
        return len(self.children)

    @property
    def number_of_grandchildren(self) -> int:
        if self.__number_of_grandchildren is None:
            # Problems...
            # grandchildren = self.calculate_number_of_grandchildren()
            # self.__number_of_grandchildren = grandchildren
            # return grandchildren
            self.__number_of_grandchildren = self.calculate_number_of_grandchildren()
        return self.__number_of_grandchildren

    def calculate_number_of_grandchildren(self) -> int:
        return sum(child.number_of_children for child in self.children)


class Employee(Person):
    __slots__ = (
        "uid",
    )

    def __init__(self, first: str, last: str, children: Optional[List["Person"]] = None,
                 uid: Optional[int] = 0) -> None:
        super().__init__(first, last, children)
        self.uid = uid or 0

    def get_employee(self) -> str:
        return self.get_full_name() + ", " + str(self.uid)


A = Employee("a", "b")
A1 = Employee("a", "b")
A2 = Person("a", "b")
B = Person("a", "b", [A, A1, A2])
C = Employee("a", "b", [B, B, A])
print(C.number_of_grandchildren)
