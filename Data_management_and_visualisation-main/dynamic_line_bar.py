import matplotlib.pyplot as plt
x_input = input("Enter X values separated by spaces: ")
y_input = input("Enter Y values separated by spaces: ")
x = [int(i) for i in x_input.split()]
y = [int(i) for i in y_input.split()]
plt.plot(x, y, color='black', linestyle='-', marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()