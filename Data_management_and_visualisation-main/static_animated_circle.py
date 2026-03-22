import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
x_coords = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_coords = np.array([0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9])

fig, ax = plt.subplots()
ax.set_xlim(min(x_coords) - 1, max(x_coords) + 1)
ax.set_ylim(min(y_coords) - 1, max(y_coords) + 1)
ax.set_aspect('equal') 

circle = plt.Circle((x_coords[0], y_coords[0]), 0.4, color='crimson')
ax.add_patch(circle)

def update(frame):
    
    circle.set_center((x_coords[frame], y_coords[frame]))
    return circle,

ani = animation.FuncAnimation(fig, update, frames=len(x_coords), interval=500, blit=True)

plt.title("Circle Moving")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()