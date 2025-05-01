import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y, edgecolors='black')
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния случайных данных")

plt.grid(True)
plt.show()