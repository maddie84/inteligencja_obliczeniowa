import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1 funkcja Michalewicza
def michal(xx, m=10):
    ii = np.arange(1, len(xx) + 1)
    sin_part = np.sin(xx) * (np.sin(ii * xx**2 / np.pi))**(2 * m)
    summation = np.sum(sin_part)
    
    y = -summation
    return y

# Przygotowanie danych do wykresu
x1_values = np.linspace(0, np.pi, 100)
x2_values = np.linspace(0, np.pi, 100)
X1, X2 = np.meshgrid(x1_values, x2_values)
Z = np.zeros_like(X1)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i, j] = michal(np.array([X1[i, j], X2[i, j]]))

# Wykres 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Z, cmap='viridis')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('michal([X1, X2])')
ax.set_title('Michalewicz Function')

plt.show()
