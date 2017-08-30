import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(0, 1, 30), (1, 0, 30), (0, 2, 25), (2, 0, 20), (1, 2, 40),
             (2, 1, 35), (1, 3, 35), (2, 4, 15), (3, 1, 25), (3, 2, 20),
             (3, 5, 45), (4, 3, 10), (4, 5, 40), (5, 3, 50), (5, 4, 50)]

G = nx.DiGraph()
G.add_weighted_edges_from(edge_list)
pos = {0: (0, 1), 1: (2, 2), 2: (2, 0), 3: (5, 2), 4: (5, 0), 5: (7, 1)}
plt.figure(facecolor="w")
plt.axis('off')
nx.draw_networkx(G, pos, node_size=2500, node_color='w')
plt.show()
