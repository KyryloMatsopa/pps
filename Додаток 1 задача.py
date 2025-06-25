import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay

def plot_sub(ax, points, title):
    tri = Delaunay(points)
    ax.triplot(points[:, 0], points[:, 1], tri.simplices)
    ax.plot(points[:, 0], points[:, 1], 'ro')
    for i, (x, y) in enumerate(points):
        ax.text(x + 0.1, y + 0.1, f'{chr(65 + i)}', fontsize=10)
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.grid(True)

# Кроки
points_0 = np.array([[2, 2], [6, 2], [4, 5]])                 # A B C
points_1 = np.vstack([points_0, [4, 3]])                      # +D
points_2 = np.vstack([points_1, [1, 4]])                      # +E
points_3 = np.vstack([points_2, [7, 4]])                      # +F

# Малюємо 4 підграфіки
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plot_sub(axs[0, 0], points_0, "Крок 0: A, B, C")
plot_sub(axs[0, 1], points_1, "Крок 1: +D")
plot_sub(axs[1, 0], points_2, "Крок 2: +E")
plot_sub(axs[1, 1], points_3, "Крок 3: +F")

plt.tight_layout()
plt.show()
