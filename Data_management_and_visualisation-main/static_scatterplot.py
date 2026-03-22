import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_data = np.array([5, 7, 4, 9, 2, 8, 1, 6])

plt.figure(figsize=(8, 5))
plt.scatter(x_data, y_data, color='blue', s=100, edgecolor='black', alpha=0.7)

plt.title("Static Scatter Plot (Pre-defined Array)")
plt.xlabel("X-Axis Values")
plt.ylabel("Y-Axis Values")
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()