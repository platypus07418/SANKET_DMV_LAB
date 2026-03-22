import matplotlib.pyplot as plt
names_input = input("Enter company names separated by spaces: ")
mylabels = names_input.split()  
values_input = input("Enter their values separated by spaces: ")
y = [float(val) for val in values_input.split()]
plt.pie(y, labels=mylabels, autopct='%1.1f%%')
plt.title("Company Share")
plt.show()