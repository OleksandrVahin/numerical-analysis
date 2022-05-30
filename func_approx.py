import numpy as np


def chebyshev_nodes(a, b, n):
    """Takes segment and number of nodes, returns nodes"""
    nodes = []
    for i in range(n + 1):
        nodes.append((b + a) / 2 - (b - a) / 2 * np.cos((2 * i + 1) / (2 * n + 2) * np.pi))
    return nodes
