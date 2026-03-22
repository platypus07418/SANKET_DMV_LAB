import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
y_data = np.array([10, 25, 15, 40, 35, 60, 55, 80])
x_data = np.arange(len(y_data))
fig, ax = plt.subplots()
ax.set_xlim(0, len(y_data) - 1) 
ax.set_ylim(min(y_data) - 5, max(y_data) + 5) 
line, = ax.plot([], [], lw=2)
def update(i):
    line.set_data(x_data[:i], y_data[:i])
    return line,
ani = animation.FuncAnimation(fig, update, frames=len(y_data)+1, interval=300, blit=True)
plt.show()