N = 6
edge_list = [(0, 1, 30), (1, 0, 30), (0, 2, 25), (2, 0, 20), (1, 2, 40),
             (2, 1, 35), (1, 3, 35), (2, 4, 15), (3, 1, 25), (3, 2, 20),
             (3, 5, 45), (4, 3, 10), (4, 5, 40), (5, 3, 50), (5, 4, 50)]
dij = [[float('inf') for i in range(N)] for j in range(N)]
for i in range(N):
    dij[i][i] = 0.0
for e in edge_list:
    dij[e[0]][e[1]] = e[2]


def dijkstra(origin, dest):
    v = [float('inf') for i in range(N)]
    M = list(range(N))
    p = [None for i in range(N)]

    i = origin
    v[i] = 0
    M.remove(i)
    while len(M) > 0:
        for j in range(N):
            dist = v[i] + dij[i][j]
            if v[j] > dist:
                v[j] = dist
                p[j] = i
        min_v = float('inf')
        for j in M:
            if min_v > v[j]:
                min_v = v[j]
                i = j
        M.remove(i)

    path = [dest]
    while dest != origin:
        path.insert(0, p[dest])
        dest = p[dest]
    print('dist:', v[dest], ' path:', path)


dijkstra(0, 5)  # dist: 0  path: [0, 2, 4, 5]
