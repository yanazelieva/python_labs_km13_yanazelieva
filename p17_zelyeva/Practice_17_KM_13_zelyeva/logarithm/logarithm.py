import math


def log(n, base):
    a = math.log(n, base)
    print(f'Logarithm {n, base} is ', a)


def ln(n):
    a = math.exp(n)
    print(f'Natural logarithm {n} is', a)


def lg(n):
    a = math.log10(n)
    print(f'Logarithm with base 10 number of {n} is ', a)
