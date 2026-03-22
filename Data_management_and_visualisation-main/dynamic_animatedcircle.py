import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

print("Example input format: 1 2 3 4 5")
x_input = input("Enter X coordinates: ")
y_input = input("Enter Y coordinates: ")

x_coords = np.array([float(i) for i in x_input.split()])
y_coords = np.array([float(i) for i in y_input.split()])

if len(x_coords) != len(y_coords):
    print("Error: You must enter the same number of X and Y coordinates!")
else:
   
    fig, ax = plt.subplots()
    
    
    ax.set_xlim(min(x_coords) - 2, max(x_coords) + 2)
    ax.set_ylim(min(y_coords) - 2, max(y_coords) + 2)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.7)
    circle = plt.Circle((x_coords[0], y_coords[0]), 0.5, color='forestgreen')
    ax.add_patch(circle)
    def update(frame):
        
        circle.set_center((x_coords[frame], y_coords[frame]))
        return circle,
    ani = animation.FuncAnimation(fig, update, frames=len(x_coords), interval=400, blit=True, repeat=True)

    plt.title("Circle Path: " + str(list(zip(x_coords, y_coords))))
    plt.show()