#! /usr/bin/env python

"""
Matplotlib users guide:
  https://matplotlib.org/users/index.html

"""


import numpy as np
import matplotlib.pyplot as plt

RED = (1.0, 0, 0)
GREEN = (0, 1.0, 0)
BLUE = (0, 0, 1.0)

x = np.arange(0, 5, 0.1)
y = np.sin(x)
#plt.plot(x, y)

def add_shape(points, color):
    polygon = plt.Polygon(points, color=RED, fill=0)
    plt.gca().add_patch(polygon)
    
square_points = [(3,3), (3, -3), (-3, -3), (-3, 3)]
add_shape(square_points, RED)
plt.show()
