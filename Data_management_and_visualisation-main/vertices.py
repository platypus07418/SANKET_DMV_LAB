import networkx as nx
import matplotlib.pyplot as plt
n = int(input("Enter number of vertices: "))
if n > 3:
    G = nx.complete_graph(n)
    nx.draw(G, node_color='blue', node_size=1500, with_labels=True)
    plt.title(f"Complete Graph with {n} Nodes")
    plt.show()
else:
    print("Min Vertices should be more than 3")