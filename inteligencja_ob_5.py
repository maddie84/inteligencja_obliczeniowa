import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def levy(xx):
    """
    LEVY FUNCTION
    
    Parameters:
    - xx: numpy array, input vector [x1, x2]
    
    Returns:
    - y: float, result of the Levy function
    """
    x1, x2 = xx[0], xx[1]
    term1 = (np.sin(3 * np.pi * x1))**2
    term2 = (x1 - 1)**2 * (1 + (np.sin(3 * np.pi * x2))**2)
    term3 = (x2 - 1)**2 * (1 + (np.sin(2 * np.pi * x2))**2)

    y = term1 + term2 + term3
    return y

# Przygotowanie danych do wykresu
x1_values = np.linspace(-10, 10, 100)
x2_values = np.linspace(-10, 10, 100)
X1, X2 = np.meshgrid(x1_values, x2_values)
Z = np.zeros_like(X1)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i, j] = levy(np.array([X1[i, j], X2[i, j]]))

# Wykres 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Z, cmap='viridis', linewidth=0, antialiased=False)

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('levy([X1, X2])')
ax.set_title('Levy Function')

# Dodanie paska kolorów
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()
