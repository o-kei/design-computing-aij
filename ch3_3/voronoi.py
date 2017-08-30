import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

points = np.random.rand(30, 2)
vor = Voronoi(points)
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.tick_params(labelbottom="off", labelleft="off")
voronoi_plot_2d(vor, ax=ax)
plt.show()
