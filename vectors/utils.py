import math
import numpy as np

def degrees_to_radians(degrees):
    return degrees/(180/math.pi)

def rotate_polygon(polygon, angle):
    centre = np.array([polygon.min(axis=0) - polygon.max(axis=0), polygon.min(axis=1) - polygon.max(axis=1)])

    return [rotate(point-centre, angle)+centre for point in polygon]

def rotate(vec, angle):
    matrix = np.array([np.cos(degrees_to_radians(angle)), -np.sin(degrees_to_radians(angle)), np.sin(degrees_to_radians(angle)), np.cos(degrees_to_radians(angle))]).reshape(2,2)
    return vec.dot(matrix)

print(rotate(np.array([1,2]), 10))