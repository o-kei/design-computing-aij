from math import *
from functools import reduce
import networkx as nx


def AxialMapAnalysis(graph, radius):
    global k, TD, MD, RA, RRA, IntV
    d = dict(nx.all_pairs_dijkstra_path_length(graph))
    r = {i: list(filter(lambda n: n <= radius, d[i].values())) for i in d}
    k = {i: len(r[i]) for i in d}
    TD = {i: reduce(lambda x, y: x + y, r[i]) for i in d}
    MD = {i: TD[i] / (k[i] - 1) for i in TD}
    RA = {i: 2 * (MD[i] - 1) / (k[i] - 2) for i in MD}
    Dk = {i: 2 * (k[i] * (log((k[i] + 2) / 3, 2) - 1) + 1) / ((k[i] - 1) * (k[i] - 2))
          for i in d}
    RRA = {i: RA[i] / Dk[i] for i in RA}
    IntV = {i: 1 / RRA[i] for i in RRA}


def AxialMapAnalysis_from_adjlist(filename, radius=float("inf")):
    G = nx.read_adjlist(filename, nodetype=int)
    AxialMapAnalysis(G, radius)
    for i in sorted(IntV):
        print(i, k[i], round(MD[i], 3), round(RA[i], 3), round(IntV[i], 3))


AxialMapAnalysis_from_adjlist('barnsbury_adjlist.txt', 3)
