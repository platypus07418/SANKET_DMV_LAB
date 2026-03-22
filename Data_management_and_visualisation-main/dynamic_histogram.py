import matplotlib.pyplot as plt
x_input = input("Enter x values (e.g., 1 2 3 4): ")
x_values = x_input.split() 
y_input = input("Enter y values (e.g., 23 45 56 12): ")
y_values = [float(i) for i in y_input.split()]
plt.figure(figsize=(8, 5)) 
plt.hist(x_values, y_values, color='skyblue', edgecolor='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Company/Category Data')
plt.show()