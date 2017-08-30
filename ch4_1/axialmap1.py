from math import *
from functools import reduce
import networkx as nx


def AxialMapAnalysis(graph):
    global k, TD, MD, RA, RRA, IntV
    d = nx.all_pairs_dijkstra_path_length(graph)
    k = len(d)
    TD = {i: reduce(lambda x, y: x + y, d[i].values()) for i in d}
    MD = {i: TD[i] / (k - 1) for i in TD}
    RA = {i: 2 * (MD[i] - 1) / (k - 2) for i in MD}
    Dk = 2 * (k * (log((k + 2) / 3, 2) - 1) + 1) / ((k - 1) * (k - 2))
    RRA = {i: RA[i] / Dk for i in RA}
    IntV = {i: 1 / RRA[i] for i in RRA}


def AxialMapAnalysis_from_adjlist(filename):
    G = nx.read_adjlist(filename, nodetype=int)
    AxialMapAnalysis(G)
    for i in IntV:
        print(i, round(MD[i], 3), round(RA[i], 3), round(IntV[i], 3))


AxialMapAnalysis_from_adjlist('barnsbury_adjlist.txt')
