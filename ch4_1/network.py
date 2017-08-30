import networkx as nx

edge_list = [(0, 1, 30), (1, 0, 30), (0, 2, 25), (2, 0, 20), (1, 2, 40),
             (2, 1, 35), (1, 3, 35), (2, 4, 15), (3, 1, 25), (3, 2, 20),
             (3, 5, 45), (4, 3, 10), (4, 5, 40), (5, 3, 50), (5, 4, 50)]

G = nx.DiGraph()
G.add_weighted_edges_from(edge_list)
print('dist:', nx.dijkstra_path_length(G, 0, 5), end='')
print(' path:', nx.dijkstra_path(G, 0, 5))
