import matplotlib.pyplot as plt
import numpy as np
from functools import partial
import random
from scipy.optimize import fsolve


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


def print_log(log):
    """Takes log and print it"""
    print("-" * 55)
    print('|' + "№ iteration".center(15) + '|'
          + 'x'.center(11) + '|'
          + 'y'.center(12) + '|'
          + 'Δ'.center(12) + '|')
    print("-" * 55)
    for i in range(len(log)):
        print('|' + str(i).center(15) + '|'
              + '{:.5f}'.format(log[i][0][0]).center(11) + '|'
              + '{:.5f}'.format(log[i][0][1]).center(12) + '|'
              + '{:.6f}'.format(log[i][1]).center(12) + '|')
        print("-" * 55)


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
print_log(history)
print("Solution of system is:", tuple(map(r5, solution)))

# Calculating solution with random initial approximation
print("\nRandom initial approximation")
for i in range(5):
    approx = random.uniform(-50, 50), random.uniform(-50, 50)
    solution, history = simple_iterations(approx, 0.00001, (x1, y1))
    print(f"Attempt №{i + 1}: initial approx - {approx} root is {solution}, iterations - {len(history)}")

# Calculating solution via SciPy
print("\nVia SciPy")
print("Root is", fsolve((lambda x: (np.cos(x[1] - 2)+x[0], np.sin(x[0] + 0.5) - x[1] - 1)), (0.5, -0.1)))
