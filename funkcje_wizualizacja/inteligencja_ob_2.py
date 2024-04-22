import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ackley(xx, a=20, b=0.2, c=2 * np.pi):
    d = len(xx)
    sum1 = np.sum(xx**2)
    sum2 = np.sum(np.cos(c * xx))

    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)

    y = term1 + term2 + a + np.exp(1)
    return y

# Przygotowanie danych do wykresu
x_values = np.linspace(-5, 5, 100)
y_values = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = np.zeros_like(X)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i, j] = ackley(np.array([X[i, j], Y[i, j]]))

# Wykres 3D z dostosowaną paletą kolorów
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0, antialiased=False)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('ackley([X, Y])')
ax.set_title('Ackley Function')

# Dodanie paska kolorów
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.show()
