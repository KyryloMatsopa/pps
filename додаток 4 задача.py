import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import time

points = np.random.rand(10000, 2)

start = time.time()
tri = Delaunay(points)
end = time.time()

print(f"Тріангуляція виконана за {end - start:.2f} сек")

# Збереження без показу
plt.figure(figsize=(10, 10))
plt.triplot(points[:, 0], points[:, 1], tri.simplices, linewidth=0.3)
plt.axis('off')
plt.savefig("triangulation_10000.png", dpi=300)
