import matplotlib.pyplot as plt

# Шлях до файлу з датасетом
DATASET_FILE = r"C:\Users\HOME\Desktop\Новая папка (2)\DS8.txt"


# Розмір полотна у пікселях
WIDTH = 960
HEIGHT = 540
DPI = 100  # 960/100 = 9.6 дюйма, 540/100 = 5.4 дюйма

# Зчитування координат з файлу
x_coords = []
y_coords = []

with open(DATASET_FILE, "r") as file:
    for line in file:
        x, y = map(int, line.split())
        x_coords.append(x)
        y_coords.append(y)

# Створення графіка
plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI)

# Відображення точок
plt.scatter(x_coords, y_coords, s=1)

# Налаштування осей координат
plt.xlim(0, WIDTH)
plt.ylim(0, HEIGHT)
plt.gca().set_aspect('equal', adjustable='box')

# Початок координат у нижньому лівому куті
plt.gca().invert_yaxis()
plt.gca().invert_yaxis()  # подвійна інверсія повертає вісь Y догори

# Сітка (опціонально)
plt.grid(True, linewidth=0.3)

# Збереження результату
plt.savefig("result.png", bbox_inches="tight")
plt.close()

print("Графік успішно збережено у файл result.png")
