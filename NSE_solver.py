import matplotlib.pyplot as plt
import numpy as np
from functools import partial


# First task initial data
def y1(x):
    """Returns first equation of system"""
    return np.sin(x + 0.5) - 1


def x1(y):
    """Returns second equation of system"""
    return -np.cos(y - 2)


def print_intersection(f1, f2):
    """Builds graphic of two equations on the one plot"""
    plt.subplots()
    ls = np.linspace(-3, 3, 100)
    plt.plot(ls, f2(ls))
    plt.plot(f1(ls), ls)
    plt.show()


r5 = partial(round, ndigits=5)


def norm_max(vector):
    """Takes vector, returns its Chebyshev's norm"""
    return max(map(abs, vector))


def vector_difference(a, b):
    """Takes two vectors, returns their difference"""
    return tuple(t - s for t, s in zip(a, b))


def simple_iterations(x_0, eps, equations):
    """
    Solves system of nonlinear equations
    Takes:
        x_0 - initial approximation
        eps - precision
        equations - equations of system
    Returns:
        x_1 - vector of approximate solutions
        log - history of iterations
    """
    equations = equations[::-1]
    log = [(x_0, 0)]
    while True:
        x_1 = tuple(equations[i](x_0[i]) for i in range(len(x_0)))[::-1]
        delta = norm_max(vector_difference(x_1, x_0))
        log.append((x_1, delta))
        if delta <= eps:
            return x_1, log
        x_0 = x_1


# First task

# Looking graphically for first initial approximation
print_intersection(x1, y1)

# Calculating solution
solution, history = simple_iterations((0.5, -0.1), 0.00001, (x1, y1))
print("Solution of system is:", tuple(map(r5, solution)))
