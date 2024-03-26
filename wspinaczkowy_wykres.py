import random
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def ackley_function(x, y):
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

def perm_function(*args, beta=10):
    result = sum((i * (x**2)**beta) for i, x in enumerate(args, start=1))
    return result

seed = 123
random.seed(seed)

def hill_climbing(max_iter=1000, step_size=0.1):
    # Initialize a random starting point
    current_point = [random.uniform(-10, 10), random.uniform(-10, 10)]
    current_value = perm_function(*current_point)
    
    # Lists to store the path of the algorithm
    path_points = [current_point]
    path_values = [current_value]

    # Perform iterations
    for _ in range(max_iter):
        # Generate a new candidate solution by perturbing the current point
        new_point = [current_point[0] + random.uniform(-step_size, step_size), current_point[1] + random.uniform(-step_size, step_size)]
        new_value = perm_function(*new_point)

        # If the new solution is better, update the current solution
        if new_value < current_value:
            current_point = new_point
            current_value = new_value
        
        # Append the current point and value to the path
        path_points.append(current_point)
        path_values.append(current_value)

    return path_points, path_values

# Run hill climbing algorithm
path_points, path_values = hill_climbing()

# Generate data for the surface plot
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = perm_function(X, Y)

# Plot the surface and the path of the algorithm
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
path_points = np.array(path_points)
ax.plot(path_points[:,0], path_points[:,1], path_values, color='red', marker='o', linestyle='-')
ax.set_title('Path of Hill Climbing Algorithm in 3D perm_function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
plt.show()
