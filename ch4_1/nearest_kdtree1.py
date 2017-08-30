from operator import itemgetter


def kdtree(points, axis):
    if not points:
        return None

    median = len(points) // 2
    points.sort(key=itemgetter(axis))
    axis = (axis + 1) % 2

    return [points[median],
            kdtree(points[0:median], axis),
            kdtree(points[median + 1:], axis)]


point_list = [(2, 5), (5, 7), (10, 2), (3, 3), (8, 9), (1, 1)]
tree = kdtree(point_list, 0)
print(tree)
