#! /usr/bin/env python

"""
Matplotlib users guide:
  https://matplotlib.org/users/index.html

"""

import math
import numpy as np
import matplotlib.pyplot as plt

BLACK = (0, 0, 0)
LIGHT_GREY = (0.75, 0.75, 0.75)
DARK_GREY = (0.25, 0.25, 0.25)
RED = (1.0, 0, 0)
GREEN = (0, 1.0, 0)
BLUE = (0, 0, 1.0)

def add_shape(ax, points, color=BLACK):
    if hasattr(points, 'shape') and points.shape[1] != 2:
        points = np.swapaxes(points, 0, 1)
    polygon = plt.Polygon(points, color=color, fill=0)
    ax.add_patch(polygon)

def add_bounding_box(ax, llx, lly, urx, ury):
    bounding_box = [(llx, lly), (llx, ury), (urx, ury), (urx, lly)]
    print(bounding_box)
    bb = plt.Polygon(bounding_box, color=BLACK, linewidth=0.2, fill=False)
    ax.add_patch(bb)

def rotate_array(arr1, degrees):
    rad = degrees / 360 * 2 * math.pi
    rad2 = rad + math.pi / 2
    T = np.array( [(math.cos(rad), math.cos(rad2)), (math.sin(rad), math.sin(rad2))] )
    arr2 = np.matmul(T, arr1)
    return arr2
    
    

fig, ax = plt.subplots()
add_bounding_box(ax, -10, -10, 10, 10)
M = np.array( [(1, 5, 1), (1, 1, 2)] )
add_shape(ax, M, LIGHT_GREY)
darkness = 0.0
degrees_step = 15
for deg in range(45, 360, degrees_step):
    color = (darkness, darkness, darkness)
    darkness = darkness + (degrees_step/360.)
    M2 = rotate_array(M, deg)
    add_shape(ax, M2, color)
ax.plot()
plt.show()
