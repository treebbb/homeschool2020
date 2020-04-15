#! /usr/bin/env python

"""
Matplotlib users guide:
  https://matplotlib.org/users/index.html

"""


import numpy as np
import matplotlib.pyplot as plt

BLACK = (0, 0, 0)
LIGHT_GREY = (0.75, 0.75, 0.75)
DARK_GREY = (0.25, 0.25, 0.25)
RED = (1.0, 0, 0)
GREEN = (0, 1.0, 0)
BLUE = (0, 0, 1.0)

def add_shape(ax, points, color=BLACK):
    polygon = plt.Polygon(points, color=color, fill=0)
    ax.add_patch(polygon)

def add_bounding_box(ax, llx, lly, urx, ury):
    bounding_box = [(llx, lly), (llx, ury), (urx, ury), (urx, lly)]
    print(bounding_box)
    bb = plt.Polygon(bounding_box, color=BLACK, linewidth=0.2, fill=False)
    ax.add_patch(bb)
    

fig, ax = plt.subplots()
add_bounding_box(ax, -10, -10, 10, 10)
#square_points = [(3,3), (3, -3), (-3, -3), (-3, 3)]
#add_shape(ax, square_points, RED)
M = np.array( [(1, 1), (5, 1), (1, 2)] )
print('M', M)
add_shape(ax, M, LIGHT_GREY)
M2 = M * 2
print('M2', M2)
add_shape(ax, M2, DARK_GREY)
ax.plot()
plt.show()
