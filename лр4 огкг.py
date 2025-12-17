import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from collections import deque

# === Зчитування датасету ===
points = np.loadtxt(
    r"C:\Users\HOME\Desktop\labs_graphic\лр4\DS8.txt"
)


# === Пошук зв'язаних областей (8-зв’язність) ===
points_set = set(map(tuple, points))
visited = set()
components = []

neighbors = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

for p in points_set:
    if p not in visited:
        queue = deque([p])
        component = []
        visited.add(p)

        while queue:
            x, y = queue.popleft()
            component.append((x, y))
            for dx, dy in neighbors:
                npnt = (x+dx, y+dy)
                if npnt in points_set and npnt not in visited:
                    visited.add(npnt)
                    queue.append(npnt)

        components.append(component)

# === Центри ваги ===
centroids = np.array([
    (np.mean([p[0] for p in c]), np.mean([p[1] for p in c]))
    for c in components
])

# === Діаграма Вороного ===
vor = Voronoi(centroids)

# === Візуалізація ===
plt.figure(figsize=(9.6, 5.4))
voronoi_plot_2d(vor, show_vertices=False, line_colors='blue',
                line_width=1, line_alpha=0.8)

plt.scatter(points[:,0], points[:,1], c='black', s=5, alpha=0.1)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s=25)

plt.xlim(0, 960)
plt.ylim(0, 540)
plt.gca().set_aspect('equal')
plt.title("Діаграма Вороного за центрами ваги")
plt.savefig("result_voronoi.png", dpi=300)
plt.show()
