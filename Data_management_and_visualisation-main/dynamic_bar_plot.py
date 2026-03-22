import matplotlib.pyplot as plt
x_input = input("Enter x values (separated by space): ")
x_values = x_input.split()
y_input = input("Enter y values (separated by space): ")
y_values = [float(i) for i in y_input.split()]
plt.figure(figsize=(8, 5)) 
plt.bar(x_values, y_values, color='green')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('Sample Bar Graph of Categories and Values')
plt.grid(True)
plt.show()