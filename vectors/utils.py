import math
import numpy as np

def degrees_to_radians(degrees):
    return degrees/(180/math.pi)

def rotate(vec, angle):
    matrix = np.array([np.cos(degrees_to_radians(angle)), -np.sin(degrees_to_radians(angle)), np.sin(degrees_to_radians(angle)), np.cos(degrees_to_radians(angle))]).reshape(2,2)
    print(vec.dot(matrix))

rotate(np.array([1,2]), 90)