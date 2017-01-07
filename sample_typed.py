# -*- coding: utf-8 -*-

"""Sample stuff without types"""
from typing import Any, TypeVar, Iterable, Iterator, Generator, Union
from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple

"""Learn python from beginning, but with types"""

# Variables
x = 1  # type: int
y = 2  # type: int
z = 2 * 10 ** 9  # type: int
# Mypy uses type inference

# Sum numbers
a = x + y + z  # type: int

string = "My name is"  # type: str
another_string = "j00sko"  # type: str

# Also with string

together = string + " " + another_string  # type: str

number_str = "5"  # type: str

# Problems

try:
    error = number_str + a  # type: ignore
    # error = number_str + a  # type: TypeError
    # error: Incompatible types in assignment (expression has type "int", variable has type "TypeError")
except TypeError:
    print("Cant sum int and  str :(")
    correct = int(number_str) + a  # type: Any
    # Thanks javascript
    correct = number_str + str(a)


# Language allows functions
def greet(name: str, greeting_start: str = "Hello: ", greeting_end: str = "!") -> str:
    return greeting_start + name + greeting_end


print(greet(another_string))

# and lists
gaps = [j for j in range(2, 10)]  # type: List[int]

sq = [(k, k * k) for k in gaps]  # type: List[Tuple[int, int]]

# and also dicts
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}  # type: Dict[str, str]

# But in millions
populations = {
    'Oregon': 3.97,
    'Florida': 19.89,
    'California': 38.8,
    'New York': 8.406,
    'Michigan': 9.91,
}  # type: Dict[str, float]


# https://github.com/python/mypy/issues/2128
def multiply(x: float, y: float = 1.0) -> float:
    return x * y


up_by_mil = lambda x: multiply(x, 10 ** 6)  # type: Callable[[float], float]

multiply2 = multiply  # type: Callable[[float, float], float]

for city, pop in populations.items():
    populations[city] = int(up_by_mil(pop))


# Vararg
def my_sum(*nums: int) -> int:
    temp = 0
    for num in nums:
        temp += num
    return temp


print(my_sum(*gaps))

# Parametrized

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def my_map(fun: Callable[[T1], T2], items: Iterable[T1]) -> List[T2]:
    return [fun(item) for item in items]


# Aliases

T = TypeVar("T", int, float)

# Vector = Union[List[T], Tuple[T, ...]]
Vector = Iterable[T]


def dot_product(v1: Vector, v2: Vector) -> T:
    return sum(i * j for i, j in zip(v1, v2))


# Pycharm still has problems
# noinspection PyTypeChecker
def my_proper_map(fun: Callable[[T1], T2], items: Iterable[T1]) -> Iterator[T2]:
    for item in items:
        yield fun(item)


# Pycharm still has problems
# noinspection PyTypeChecker
def fib(f1: int = 0, f2: int = 1) -> Iterator[int]:
    yield f1
    yield f2
    while 1:
        f1, f2 = f2, f1 + f2
        yield f2


fib_num = fib()  # type: Iterator[int]

# Catch error
# print(",".join([next(fib_num) for _ in range(10)]))
print(",".join([str(next(fib_num)) for _ in range(20)]))


def fib_improved(f1: int = 0, f2: int = 1, skip: int = 0) -> Generator[int, int, List[int]]:
    missed = []  # type: List[int]
    fib_gen = fib(f1, f2)
    while skip >= 0:

        for _ in range(skip):
            missed.append(next(fib_gen))

        new_skip = yield next(fib_gen)

        if new_skip is None:
            continue
        skip = new_skip

    return missed


f = fib_improved()  # type: Generator[int, int, List[int]]

print(next(f))
print(next(f))
print(next(f))
print(f.send(1))
print(next(f))
print(next(f))
print(next(f))

try:
    f.send(-1)
except StopIteration as e:
    print("Missed: ", e.value)
