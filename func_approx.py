import numpy as np
import matplotlib.pyplot as plt


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


def comparison_table(points):
    print("-" * 71)
    print('|' + "x".center(9) + '|'
          + 'ƒ(x)'.center(12) + '|'
          + 'Lagrange'.center(12) + '|'
          + 'First Newton'.center(16) + '|'
          + 'Second Newton'.center(16) + '|')
    print("-" * 71)
    for x in points:
        print('|' + str(x).center(9) + '|'
              + '{:.5f}'.format(func1(x)).center(12) + '|'
              + '{:.5f}'.format(lagrange(x)).center(12) + '|'
              + '{:.5f}'.format(first_newton_polynom(x, nodes, differences)).center(16) + '|'
              + '{:.5f}'.format(second_newton_polynom(x, nodes, differences)).center(16) + '|')
        print("-" * 71)


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

# Comparing values
xs = (-1.5, -1, 0.1, 3.9)
comparison_table(xs)

# Drawing newtons
plt.subplots()
ls = np.linspace(-4, 6, 1000)
plt.plot(ls, func1(ls), label='ƒ(x)')
plt.plot(ls, first_newton_polynom(ls, nodes, differences), label='First Newton')
plt.plot(ls, second_newton_polynom(ls, nodes, differences), label='Second Newton')
plt.legend(loc='best')
plt.show()
