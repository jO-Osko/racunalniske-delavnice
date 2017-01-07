# -*- coding: utf-8 -*-

"""Sample stuff without types"""

# Variables
x = 1
y = 2
z = 2 * 10 ** 9

# Sum numbers
a = x + y + z

string = "My name is"
another_string = "j00sko"

# Also with string

together = string + " " + another_string

number_str = "5"

# Problems

try:
    error = number_str + a
except TypeError:
    print("Cant sum int and  str :(")
    correct = int(number_str) + a
    # Thanks javascript
    correct = number_str + str(a)


# Language allows functions
def greet(name, greeting_start="Hello: ", greeting_end="!"):
    return greeting_start + name + greeting_end


print(greet(another_string))

# and lists
gaps = [j for j in range(2, 10)]

sq = [(k, k * k) for k in gaps]

# and also dicts
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# But in millions
populations = {
    'Oregon': 3.97,
    'Florida': 19.89,
    'California': 38.8,
    'New York': 8.406,
    'Michigan': 9.91,
}


def multiply(x, y=1.0):
    return x * y


up_by_mil = lambda x: multiply(x, 10 ** 6)

multiply2 = multiply

for city, pop in populations.items():
    populations[city] = int(up_by_mil(pop))


# Vararg
def my_sum(*nums):
    temp = 0
    for num in nums:
        temp += num
    return temp


print(my_sum(*gaps))


def my_map(fun, items):
    return [fun(item) for item in items]


def dot_product(v1, v2):
    return sum(i * j for i, j in zip(v1, v2))


def my_proper_map(fun, items):
    for item in items:
        yield fun(item)


def fib(f1=0, f2=1):
    yield f1
    yield f2
    while 1:
        f1, f2 = f2, f1 + f2
        yield f2


fib_num = fib()

# Catch error
print(",".join([next(fib_num) for _ in range(10)]))


def fib_improved(f1=0, f2=1, skip=0):
    missed = []
    fib_gen = fib(f1, f2)
    while skip >= 0:

        for _ in range(skip):
            missed.append(next(fib_gen))

        new_skip = yield next(fib_gen)

        if new_skip is None:
            continue
        skip = new_skip

    return missed


f = fib_improved()

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
