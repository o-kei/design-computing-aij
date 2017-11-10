import numpy as np
import matplotlib.pyplot as plt


points = np.random.rand(30, 2)
print(points)


def area(p, q, r):
    return ((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])) / 2.0


def scan(L):
    n = len(L)
    p = list(range(n))
    for i in range(1, n):  # x 座標最小の頂点をリストの先頭とする
        if L[p[i]][0] < L[p[0]][0]:
            p[i], p[0] = p[0], p[i]
    for i in range(2, n):  # x 座標最小の頂点との角度順に並べ替え
        j = i
        while j > 1 and (area(L[p[0]], L[p[j - 1]], L[p[j]]) < 0):
            p[j], p[j - 1] = p[j - 1], p[j]
            j -= 1
    S = [p[0], p[1]]
    for i in range(2, n):  # 凹部の頂点を削除
        while area(L[S[-2]], L[S[-1]], L[p[i]]) < 0:
            del S[-1]
        S.append(p[i])
    return S


A = scan(points)
l = []
for i in range(len(A)):
    l.append(points[A[i]])
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
plt.plot(points[:, 0], points[:, 1], 'o')
poly = plt.Polygon(l, facecolor='none', edgecolor='black')
ax.add_patch(poly)
ax.tick_params(labelbottom='off', labelleft='off')
plt.show()
