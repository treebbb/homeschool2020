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

def points_2d(arr1):
    'return the first 2 rows of the array'
    return arr1[:2]

def degrees_to_radians(degrees):
    rad = degrees / 360 * 2 * math.pi
    return rad

fig, ax = plt.subplots()
add_bounding_box(ax, -8, -1, 8, 15)
M = np.array( [(2, 2, -2, -2), (0, 10, 10, 0), (1, 1, 1, 1)] )
Mx = points_2d(M)
rad1 = degrees_to_radians(3)
rad2 = degrees_to_radians(93)
A = np.array( [
(0.8 * math.cos(rad1), 0.8 * math.cos(rad2), 0),
(0.8 * math.sin(rad1), 0.8 * math.sin(rad2), 3),
(0, 0, 1)] )
AM  = np.matmul(A, M)
AMx = points_2d(AM)
add_shape(ax, Mx, BLACK)
add_shape(ax, AMx, BLACK)
for x in range(0,100,1):
    AM = np.matmul(A,AM)
    AMx = points_2d(AM)
    add_shape(ax, AMx, BLACK)
darkness = 0.0
degrees_step = 15
ax.plot()
plt.show()
