import matplotlib.pyplot as plt
import numpy as np


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


def norm_max(vector):
    """Takes vector, returns its Chebyshev's norm"""
    return max(map(abs, vector))


def vector_difference(a, b):
    """Takes two vectors, returns their difference"""
    return tuple(t - s for t, s in zip(a, b))


# Looking graphically for first initial approximation
print_intersection(x1, y1)