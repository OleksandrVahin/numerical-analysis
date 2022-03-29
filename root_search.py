from functools import reduce
from decimal import Decimal
from decimal import *
from math import log10, log


def generate_polynom(*args):
    """"Takes coefficients, returns polynomial function"""

    def function(x):
        return reduce(lambda t, y: t + x ** y[0] * y[1], enumerate(args[::-1]), 0)

    return function


def derivative_of_polynomial(*args):
    """Takes coefficients of polynomial function, returns coefficients of derivative as tuple"""
    return tuple(map(lambda x: x[0] * x[1], enumerate(args[::-1])))[-1:-len(args): -1]


def tabulation(start, end, step, function):
    """Takes segment [start;end], step and function, returns values of function and her 2 first derivatives"""
    p = start
    while p <= end + step:
        value = [Decimal(function[j](p)).quantize(Decimal('1.00000')) for j in range(3)]
        print(
            f"x = {Decimal(p).quantize(Decimal('1.00'))}\tf(x) = {value[0]} \tf'(x) = {value[1]}\tf''(x) = {value[2]}")
        p += step


def binary_search(start, end, epsilon, function):
    """Takes [start;end], precision and function, returns root on this segment using binary search"""
    middle = (start + end) / 2
    i = 1
    while abs(start - end) >= epsilon or abs(function[0](middle)) >= epsilon:
        print(f'Iteration {i} (a,f(a)) = ({r5(start)};{r5(function[0](start))})	(b,f(b)) = ({r5(end)};{r5(function[0](end))})')
        i += 1
        if abs(function[0](middle)) < epsilon:
            return middle
        elif (function[0](start) * function[0](middle)) / abs(function[0](start)) < 0:
            end = middle
        else:
            start = middle
        middle = (start + end) / 2
    return r5(middle)


def chord_search(start, end, epsilon, function):
    """Takes [start;end], precision and function, returns root on this segment using chord method"""
    if function[2](start) * function[0](start) > 0:
        x1, n = end, start
    else:
        x1, n = start, end
    x2 = x1 - (function[0](x1) / (function[0](x1) - function[0](n))) * (x1 - n)
    i = 1
    while abs(x2 - x1) >= epsilon or abs(function[0](x2)) >= epsilon:
        if n == start:
            print(f'Iteration {i} (a,f(a)) = ({r5(start)};{r5(function[0](start))}) (x,f(x)) = ({r5(x2)};{r5(function[0](x2))})')
        else:
            print(f'Iteration {i} (x,f(x)) = ({r5(x2)};{r5(function[0](x2))})   (b,f(b)) = ({r5(end)};{r5(function[0](end))})')
        i += 1
        x1 = x2
        x2 = x1 - (function[0](x1) / (function[0](x1) - function[0](n))) * (x1 - n)
    return r5(x2)


def newton_search(start, end, epsilon, function):
    """Takes [start;end], precision and function, returns root on this segment using Newton's method"""
    if function[0](start) * function[2](start) > 0:
        x1 = start
    else:
        x1 = end
    x2 = x1 - function[0](x1) / function[1](x1)
    i = 1
    while abs(x2 - x1) >= epsilon or abs(function[0](x2)) >= epsilon:
        print(f'Iteration {i} (x,f(x)) = ({r5(x2)};{r5(function[0](x2))})')
        i += 1
        x1 = x2
        x2 = x1 - function[0](x1) / function[1](x1)
    return r5(x2)


r5 = (lambda x: round(x, 5))

coefficients = (74, 789, 840, -907, -730, 348, 50, -19)
coefficients_d1 = derivative_of_polynomial(*coefficients)
coefficients_d2 = derivative_of_polynomial(*coefficients_d1)

polynom = {0: generate_polynom(*coefficients),
           1: generate_polynom(*coefficients_d1),
           2: generate_polynom(*coefficients_d2)}

transcendent = {0: lambda x: log10(x) - 7 / (2 * x + 6),
                1: lambda x: 1 / (log(10) * x) + 14 / ((2 * x + 6) ** 2),
                2: lambda x: -1 / (log(10) * (x ** 2)) - 56 / ((2 * x + 6) ** 3)}


'''
tabulation(-1, 0, 0.05, polynom, polynom1, polynom2)
print("\n \n")
tabulation(0, 1, 0.05, polynom, polynom1, polynom2)
'''

print(binary_search(-10, -9, 0.0001, polynom))
print(chord_search(-9.35, -9.30, 0.0001, polynom))
print(newton_search(-9.35, -9.30, 0.0001, polynom))
'''
print("2) Root on the [-2;-1] is %.5f" % binsearch(-2, -1, 0.0001, polynom))
print("3) Root on the [-1;-0.95] is %.5f" % binsearch(-1, -0.95, 0.0001, polynom))
print("4) Root on the [-0.3;-0.25] is %.5f" % binsearch(-0.3, -0.25, 0.0001, polynom))
print("5) Root on the [0.2;0.25] is %.5f" % binsearch(0.2, 0.25, 0.0001, polynom))
print("6) Root on the [0.35;0.4] is %.5f" % binsearch(0.35, 0.4, 0.0001, polynom))
print("7) Root on the [0.8;0.85] is %.5f" % binsearch(0.8, 0.85, 0.0001, polynom))
'''

'''
# tabulation(-10, -9, 0.05, polynom, polynom1, polynom2)
# tabulation(-2, -1, 0.05, polynom, polynom1, polynom2)
# tabulation(-1, -0.95, 0.01, polynom, polynom1, polynom2)
# tabulation(-0.3, -0.25, 0.01, polynom, polynom1, polynom2)
# tabulation(0.2, 0.25, 0.01, polynom, polynom1, polynom2)
# tabulation(0.35, 0.4, 0.01, polynom, polynom1, polynom2)
# tabulation(0.8, 0.85, 0.01, polynom, polynom1, polynom2)
'''

# print("1) Root on the [-9.35;-9.30] is %.5f" % chord_search(-9.35, -9.30, 0.0001, polynom[0], polynom[2]))
'''
print("2) Root on the [-1.55;-1.5] is %.5f" % chord_search(-1.55, -1.5, 0.0001, polynom, polynom2))
print("3) Root on the [-0.97;-0.96] is %.5f" % chord_search(-0.97, -0.96, 0.0001, polynom, polynom2))
print("4) Root on the [-0.27;-0.26] is %.5f" % chord_search(-0.27, -0.26, 0.0001, polynom, polynom2))
print("5) Root on the [0.22;0.23] is %.5f" % chord_search(0.22, 0.23, 0.0001, polynom, polynom2))
print("6) Root on the [0.38;0.39] is %.5f" % chord_search(0.38, 0.39, 0.0001, polynom, polynom2))
print("7) Root on the [0.8;0.81] is %.5f" % chord_search(0.8, 0.81, 0.0001, polynom, polynom2))
'''

'''
print("1) Root on the [-9.35;-9.30] is %.5f" % newton_search(-9.35, -9.30, 0.0001, polynom, polynom1, polynom2))
print("2) Root on the [-1.55;-1.5] is %.5f" % newton_search(-1.55, -1.5, 0.0001, polynom, polynom1, polynom2))
print("3) Root on the [-0.97;-0.96] is %.5f" % newton_search(-0.97, -0.96, 0.0001, polynom, polynom1, polynom2))
print("4) Root on the [-0.27;-0.26] is %.5f" % newton_search(-0.27, -0.26, 0.0001, polynom, polynom1, polynom2))
print("5) Root on the [0.22;0.23] is %.5f" % newton_search(0.22, 0.23, 0.0001, polynom, polynom1, polynom2))
print("6) Root on the [0.38;0.39] is %.5f" % newton_search(0.38, 0.39, 0.0001, polynom, polynom1, polynom2))
print("7) Root on the [0.8;0.81] is %.5f" % newton_search(0.8, 0.81, 0.0001, polynom, polynom1, polynom2))
'''

print("Root of the equation is %.5f" % binary_search(3, 4, 0.0001, transcendent))

'''
tabulation(3, 4, 0.05, trans, trans1, trans2)
'''

print("Root of the equation is %.5f" % chord_search(3, 4, 0.0001, transcendent))
print("Root of the equation is %.5f" % newton_search(3, 4, 0.0001, transcendent))
