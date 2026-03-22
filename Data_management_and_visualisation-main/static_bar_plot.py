import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4]
y_values = [23, 45, 56, 12]
plt.figure(figsize=(8, 5)) 
plt.bar(x_values, y_values, color='green')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('Sample Bar Graph of Categories and Values')
plt.grid("True")
plt.show()
