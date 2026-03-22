import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
x_input = input("Enter X-axis values (separated by spaces): ")
y_input = input("Enter Y-axis values (separated by spaces): ")

x_data = np.array([float(val) for val in x_input.split()])
y_data = np.array([float(val) for val in y_input.split()])

if len(x_data) != len(y_data):
    print("Error: X and Y must have the same number of points.")
else:
    
    fig, ax = plt.subplots()
    
    ax.set_xlim(min(x_data) - 1, max(x_data) + 1)
    ax.set_ylim(min(y_data) - 1, max(y_data) + 1)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    
    line, = ax.plot([], [], lw=2)
    def update(frame):
        line.set_data(x_data[:frame], y_data[:frame])
        return line,
    ani = animation.FuncAnimation(fig, update, frames=len(x_data) + 1, interval=300, blit=True, repeat=False)

    plt.show()