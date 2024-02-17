import numpy as np

from matplotlib import pyplot as plt

x = np.array([0.5, 1, 1.5, 2, 2.5, 3.5, 3.75, 4.25])
y = x ** 2

plt.scatter(x, y, color='red', s=150, marker="*")
plt.plot(x, y)
plt.show()
