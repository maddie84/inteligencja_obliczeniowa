import random
import numpy as np

def ackley_function(x):
    d = len(x)
    sum1 = sum(x**2 for x in x)
    sum2 = sum(np.cos(2 * np.pi * x) for x in x)
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * sum1)) - np.exp(0.5 * sum2) + np.e + 20

def sphere_function(x):
    return sum([xi**2 for xi in x])

def schwefel_function(x):
    return -np.sum(x * np.sin(np.sqrt(np.abs(x))))

def levy_function(x):
    d = len(x)
    w = [1 + (x[i] - 1) / 4 for i in range(d)]
    term1 = (np.sin(np.pi * w[0])) ** 2
    term2 = sum([(w[i] - 1) ** 2 * (1 + 10 * (np.sin(np.pi * w[i] + 1)) ** 2) for i in range(d - 1)])
    term3 = (w[d - 1] - 1) ** 2 * (1 + (np.sin(2 * np.pi * w[d - 1])) ** 2)
    return term1 + term2 + term3

def perm_function(x, beta=10):
    result = sum((i * (arg ** 2) ** beta) for i, arg in enumerate(x, start=1))
    return result