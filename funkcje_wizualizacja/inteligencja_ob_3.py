import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# RASTRIGIN FUNCTION 3

def rastrigin(xx):
    """
    RASTRIGIN FUNCTION
    
    Parameters:
    - xx: numpy array, input vector [x1, x2, ..., xd]
    
    Returns:
    - y: float, result of the Rastrigin function
    """
    d = len(xx)
    summation = np.sum(xx**2 - 10 * np.cos(2 * np.pi * xx))
    
    y = 10 * d + summation
    return y

# Przygotowanie danych do wykresu
x_values = np.linspace(-5.12, 5.12, 100)
y_values = np.linspace(-5.12, 5.12, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = np.zeros_like(X)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i, j] = rastrigin(np.array([X[i, j], Y[i, j]]))

# Wykres 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('rastrigin([X, Y])')
ax.set_title('Rastrigin Function')

# Dodanie paska kolorów
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()
