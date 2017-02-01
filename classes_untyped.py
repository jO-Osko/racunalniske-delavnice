# -*- coding: utf-8 -*-

"""Types with classes"""


class Person:
    def __init__(self, first, last, children=None):
        self.first_name = first
        self.last_name = last
        self.children = children or []

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_number_of_children(self):
        return len(self.children)

    def get_number_of_grandchildren(self):
        return self.calculate_number_of_grandchildren()

    def calculate_number_of_grandchildren(self):
        return sum(child.get_number_of_children() for child in self.children)


class Employee(Person):
    def __init__(self, first, last, children=None, uid=0):
        super().__init__(first, last, children)
        self.uid = uid or 0

    def get_employee(self):
        return self.get_full_name() + ", " + str(self.uid)


A = Employee("a", "b")
A1 = Employee("a", "b")
A2 = Person("a", "b")
B = Person("a", "b", [A, A1, A2])
C = Employee("a", "b", [B, B, A])
print(C.get_number_of_grandchildren())
