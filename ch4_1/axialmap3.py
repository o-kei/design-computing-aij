from math import *
from functools import reduce
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt


def GlobalAxialMapAnalysis(graph):
    global k, TD, MD, RA, RRA, IntV
    d = nx.all_pairs_dijkstra_path_length(graph)
    k = len(d)
    TD = {i: reduce(lambda x, y: x + y, d[i].values()) for i in d}
    MD = {i: TD[i] / (k - 1) for i in TD}
    RA = {i: 2 * (MD[i] - 1) / (k - 2) for i in MD}
    Dk = 2 * (k * (log((k + 2) / 3, 2) - 1) + 1) / ((k - 1) * (k - 2))
    RRA = {i: RA[i] / Dk for i in RA}
    IntV = {i: 1 / RRA[i] for i in RRA}


def AxialMapAnalysis(graph, radius):
    global k, TD, MD, RA, RRA, IntV
    d = dict(nx.all_pairs_dijkstra_path_length(graph))
    r = {i: list(filter(lambda n: n <= radius, d[i].values())) for i in d}
    k = {i: len(r[i]) for i in d}
    TD = {i: reduce(lambda x, y: x + y, r[i]) for i in d}
    MD = {i: TD[i] / (k[i] - 1) for i in TD}
    RA = {i: 2 * (MD[i] - 1) / (k[i] - 2) for i in MD}
    Dk = {i: 2 * (k[i] * (log((k[i] + 2) / 3, 2) - 1) + 1) /
          ((k[i] - 1) * (k[i] - 2)) for i in d}
    RRA = {i: RA[i] / Dk[i] for i in RA}
    IntV = {i: 1 / RRA[i] for i in RRA}


def AxialMapAnalysis_from_adjlist(filename, radius=float('inf')):
    G = nx.read_adjlist(filename, nodetype=int)
    AxialMapAnalysis(G, radius)
#    GlobalAxialMapAnalysis(G)
    for i in IntV:
        print(i, TD[i], round(MD[i], 3), round(RA[i], 3), round(IntV[i], 3))


def AxialMapAnalysis_from_axiallines(filename, index, radius=float('inf')):
    S = {}
    G = nx.Graph()
    i = 0
    for line in open(filename):
        cs = line.split(",")
        S[i] = (float(cs[0]), float(cs[1]), float(cs[2]), float(cs[3]))
        i += 1
    for i in S:
        xa = S[i][0]
        ya = S[i][1]
        xb = S[i][2]
        yb = S[i][3]
        for j in S:
            xc = S[j][0]
            yc = S[j][1]
            xd = S[j][2]
            yd = S[j][3]
            fc = (xa - xb) * (yc - ya) + (ya - yb) * (xa - xc)
            fd = (xa - xb) * (yd - ya) + (ya - yb) * (xa - xd)
            if fc * fd < 0.0:
                fa = (xc - xd) * (ya - yc) + (yc - yd) * (xc - xa)
                fb = (xc - xd) * (yb - yc) + (yc - yd) * (xc - xb)
                if fa * fb < 0.0:
                    G.add_edge(i, j)

    AxialMapAnalysis(G, radius)

    v = list(globals()[index].values())
    v_min = reduce(min, v)
    v_max = reduce(max, v)
    cmap = mpl.cm.rainbow
    norm = mpl.colors.Normalize(vmin=v_min, vmax=v_max)
    fig = plt.figure(facecolor="w")
    plt.subplots_adjust(top=1.0, bottom=0.12, left=0.0, right=1.0)
    for i in S:
        # n = (v[i] - v_min) / (v_max - v_min)
        n = (globals()[index][i] - v_min) / (v_max - v_min)
        plt.plot([S[i][0], S[i][2]], [S[i][1], S[i][3]],
                 color=cmap(n), linewidth=2)
    plt.axis('equal')
    plt.axis('off')
    ax = fig.add_axes([0.05, 0.1, 0.9, 0.02])
    cb = mpl.colorbar.ColorbarBase(
        ax, cmap=cmap, norm=norm, orientation='horizontal')
    cb.set_label(index)
    plt.show()


AxialMapAnalysis_from_axiallines('axiallines.txt', 'IntV', 3)
