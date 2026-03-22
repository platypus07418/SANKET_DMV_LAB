import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4]
y_values = [23, 45, 56, 12]
plt.figure(figsize=(8, 5)) 
plt.hist(x_values, y_values, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.show()