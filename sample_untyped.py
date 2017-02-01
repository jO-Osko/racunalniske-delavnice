# -*- coding: utf-8 -*-

"""Sample stuff without types"""

# Vsem spremenljivkam dopisi primerne tipe

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

# S pomocjo anotacij poskrbi da se mypy kljub napaki ne bo pritozeval

try:
    error = number_str + a
except TypeError:
    print("Cant sum int and  str :(")
    correct = int(number_str) + a
    # Thanks javascript
    correct = number_str + str(a)


# Dopolni funkcijo greet, da bo vrnila pozdrav uporabniku, dopisi ji tudi tipe
def greet(name, greeting_start="Hello: ", greeting_end="!"):
    ...

print(greet(another_string))


# Dopisi tipe
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

# Funkcija multiply naj sprejme dve realni stevili in vrne njun produkt
def multiply(x, y=1.0):
    ...


# Z uporabo funkcije multiply definiraj novo funkcijo, ki sprejme eno stevilko in jo pomnozi z 10**6, kaksen bo njen tip?
up_by_mil = lambda x: ...

# Kaksen pa je tip miltiply ?
multiply2 = multiply


# Ce si vse naredil ok bi to moralo pravilno prikazati stevilo ljudi v posamezni drzavi
for city, pop in populations.items():
    populations[city] = int(up_by_mil(pop))

print(populations)

# Napisi funkcijo my_sum, ki sprejmne seznam celih stevil in vrne njihovo vsoto (ali 0, ce je seznam prazen), bodi pazljiv, saj se mypy in pycharm razlikujeta pri pregledu tipov
def my_sum(*nums):
    ...


print(my_sum(*gaps))


# Dopolni funkcijo, tako, da bo sprejela funkcijo iz celih v cela stevila in seznam, in vrnila seznam vrednosti te funkcije
def my_int_map(fun, items):
    ...

print(my_int_map(up_by_mil, gaps))


# Parametriziraj my_map, da bo sprejel funkcijo A -> B, seznam elementov tipa A in vrnil seznam elementov tipa B
def my_map(fun, items):
    ...

# Definiraj nov tip Stevilo, ki je lahko ali celo stevilo, ali pa realno stevilo

# Definiraj tip Vektor, kot iterabilni objekt Stevil

# Defniraj skalarni produkt za dva Vektorja (predpostavis lahko, da sta enakih dimenzij), ne pozabi na tipe, bodi kar se da univerzalen
def dot_product(v1, v2):
    """Bonus: naredi to v eni vrstici"""
    ...


vector_a = [17, 11, 15]
vector_b = [5, -12, -3]

print(dot_product(vector_a, vector_b))


# Naredi izboljsano funkcijo(generator) map, ki namesto seznamov lahko dela z iterabilnimi objekti
def my_proper_map(fun, items):
    ...


# Dopolni funkcijo fib, da bo kot generator vracala zaporedna fibonaccijeva stevila
def fib(f1=0, f2=1):
    ...


fib_num = fib()

# Kaj pravi mypy?
print(",".join([next(fib_num) for _ in range(10)]))


# Napisi funkcijo, ki sprejme indeksa i in j ter generator/iterator g in vraca elemente od i-tega do j-tega (ce je j None, naj to pocne v nedogled)
def from_ith_to_jth(i=0, j=None, generator=range):
    ...

# izpisi fibonaccijeva stevila od 5 do 50


# Napisi bolj zapleten generator, ki generira fibonaccijeva stevila, a preskakuje za skip, hkrati pa mu lahko posljemo poravek za skip, ce pa mu posljemo skip, ki je manjsi od 0 naj neha in vrne vsa stevila, ki jih je preskocil
def fib_improved(f1=0, f2=1, skip=0):
    ...


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
