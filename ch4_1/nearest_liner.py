from math import sqrt


def sq_dist(p, q):
    return((p[0] - q[0])**2 + (p[1] - q[1])**2)


def linear_search(points, query):
    sqd = float("inf")
    for point in points:
        d = sq_dist(point, query)
        if d < sqd:
            nearest = point
            sqd = d
    return(nearest, sqd)

point_list = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
n = linear_search(point_list, (9, 2))
print('nearest:', n[0], 'dist:', sqrt(n[1]))
# nearest: (8, 1) dist: 1.4142135623730951
