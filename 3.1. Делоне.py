import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Координати 10 заданих точок
points = np.array([
    [1, 1], [2, 3], [3, 1], [4, 4], [5, 2],
    [6, 5], [7, 3], [8, 1], [9, 4], [10, 2]
])

# Побудова тріангуляції Делоне
tri = Delaunay(points)

# Візуалізація
plt.figure(figsize=(8, 5))
plt.triplot(points[:, 0], points[:, 1], tri.simplices)
plt.plot(points[:, 0], points[:, 1], 'ro')  # точки
for i, (x, y) in enumerate(points):
    plt.text(x + 0.1, y + 0.1, str(i + 1), fontsize=9)
plt.title("Тріангуляція Делоне для 10 точок")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
