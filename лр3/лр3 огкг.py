import matplotlib.pyplot as plt

# ---------- Зчитування датасету ----------
def read_points(filename):
    points = []
    with open(filename, "r") as f:
        for line in f:
            x, y = map(int, line.split())
            points.append((x, y))
    return points


# ---------- Алгоритм опуклої оболонки (Monotone Chain) ----------
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


# ---------- Основна частина ----------
points = read_points(r"C:\Users\HOME\Desktop\labs_graphic\лр3\DS8.txt")
hull = convex_hull(points)

# Збереження опуклої оболонки у файл
with open("convex_hull.txt", "w") as f:
    for x, y in hull:
        f.write(f"{x} {y}\n")

# ---------- Візуалізація ----------
plt.figure(figsize=(9.6, 5.4))  # 960x540 px

# Всі точки
x_all, y_all = zip(*points)
plt.scatter(x_all, y_all, s=5, color="black")

# Опукла оболонка
hull_closed = hull + [hull[0]]
x_h, y_h = zip(*hull_closed)
plt.plot(x_h, y_h, color="blue", linewidth=2)

plt.title("Опукла оболонка множини точок")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Збереження зображення
plt.savefig("convex_hull.png", dpi=100)
plt.show()
