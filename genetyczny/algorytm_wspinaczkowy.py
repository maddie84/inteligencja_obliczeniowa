import random
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def sphere_function(*args):
    return sum(x ** 2 for x in args)

def ackley_function(*args):
    d = len(args)
    sum1 = sum(x**2 for x in args)
    sum2 = sum(np.cos(2 * np.pi * x) for x in args)
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * sum1)) - np.exp(0.5 * sum2) + np.e + 20

def schwefel_function(x):
    return -np.sum(x * np.sin(np.sqrt(np.abs(x))))

def sum_squares_function(x):
    return np.sum([(i+1) * x**2 for i in range(int(x))])

def perm_function(*args, beta=10):
    result = sum((i * (x**2)**beta) for i, x in enumerate(args, start=1))
    return result

seed = 123
random.seed(seed)

def hill_climbing(max_iter=1000, step_size=0.1):
    # Initialize a random starting point
    current_point = random.uniform(-10, 10)
    current_value = ackley_function(current_point)

    # Perform iterations
    for _ in range(max_iter):
        # Generate a new candidate solution by perturbing the current point
        new_point = current_point + random.uniform(-step_size, step_size)
        new_value = ackley_function(new_point)

        # If the new solution is better, update the current solution
        if new_value < current_value:
            current_point = new_point
            current_value = new_value

    return current_point, current_value

best_solution, best_value = hill_climbing()
print("Best solution:", best_solution)
print("Best value:", best_value)

