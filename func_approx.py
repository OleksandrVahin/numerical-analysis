import math
import numpy as np
from functools import reduce


def chebyshev_nodes(a, b, n):
    """Takes segment and number of nodes, returns nodes"""
    nodes = []
    for i in range(n + 1):
        nodes.append((b + a) / 2 - (b - a) / 2 * np.cos((2 * i + 1) / (2 * n + 2) * np.pi))
    return nodes


def func1(x):
    """Returns value of function from first task"""
    return 2 * x - x ** 2 - 2 * np.cos(x - 1)


def finite_differences(func_values):
    """Takes values of function in nodes, returns list of finite differences all orders"""
    n = len(func_values)
    diffs = [func_values]
    while n > 1:
        diffs.append(tuple(diffs[-1][i + 1] - diffs[-1][i] for i in range(n - 1)))
        n -= 1
    del diffs[0]
    return diffs


def lagrange(x):
    """Returns value of lagrange interpolation polynom for first task"""
    return -0.61743 * x ** 2 + 1.23486 * x + 1.0806


def first_newton_polynom(x, nodes, diffs):
    """Returns value of first newton interpolation polynom"""
    h = nodes[1] - nodes[0]
    q = (x - nodes[0]) / h
    result = func1(nodes[0])
    k = 1
    for i in range(len(diffs) - 1):
        k *= (q - i) / (i + 1)
        result += k * diffs[i][0]
    return result


def second_newton_polynom(x, nodes, diffs):
    """Returns value of second newton interpolation polynom"""
    h = nodes[1] - nodes[0]
    q = (x - nodes[-1]) / h
    result = func1(nodes[-1])
    k = 1
    for i in range(len(diffs) - 1):
        k *= (q + i) / (i + 1)
        result += k * diffs[i][-1]
    return result


# First Task

# Calculating values in nodes
nodes = (-2, 0, 2, 4)
values = tuple(func1(node) for node in nodes)
print("Function value in nodes:")
for node in values:
    print('{:.5f}'.format(node), end=' ')

# Calculating finite differences
differences = finite_differences(values)
print("\n\nFinite differences:")
print(*differences, sep='\n')
for node in nodes:
    print('{:.5f}'.format(second_newton_polynom(node, nodes, differences)), end=' ')