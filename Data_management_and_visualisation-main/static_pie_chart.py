import matplotlib.pyplot as plt
mylabels = ["Apple", "Tesla", "IBM", "Nvidia"]
y = [35, 25, 25, 15] 
plt.pie(y, labels=mylabels, autopct='%1.1f%%')
plt.title("Company Share")
plt.show()