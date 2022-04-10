import math
import numpy as np

def degrees_to_radians(degrees):
    return degrees/(180/math.pi)

def rotate_polygon(polygon, angle):
    centre = np.array([polygon.min(axis=0) - polygon.max(axis=0), polygon.min(axis=1) - polygon.max(axis=1)])

    return [rotate(point-centre, angle)+centre for point in polygon]

def rotate(vec, angle):
    matrix = np.array([np.cos(degrees_to_radians(-angle)), -np.sin(degrees_to_radians(-angle)), np.sin(degrees_to_radians(-angle)), np.cos(degrees_to_radians(-angle))]).reshape(2,2)
    return vec.dot(matrix)


# 10% of width
screen_dims = np.array([800, 600])
scaling_factor = screen_dims[0]*.1

# takes a 2d vector and returns its unit vector     
def normalize(vec):
    if np.linalg.norm(vec) ==0:
        return np.array([0,0])
    unit_vector = vec/np.linalg.norm(vec)
    return unit_vector*scaling_factor

def degrees_to_cartesian(angle):
    vec = np.array([np.cos(degrees_to_radians(angle)), np.sin(degrees_to_radians(angle))])
    return vec/np.linalg.norm(vec)*scaling_factor

# print(normalize(np.array([100,10])))
# print(degrees_to_cartesian(-40))

vec = np.array([2,2])
print(rotate(vec, 45))


