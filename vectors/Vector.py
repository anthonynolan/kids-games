import numpy as np

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def from_points(P1, P2):
        return np.array(P2)-np.array(P1)

v = Vector(23, 3)
print(v)
print(Vector.from_points((2,16), (23,2)))

T = np.array([2,3])
print(np.sqrt(T.dot(T)))
def magnitude(vec):
    return np.sqrt(vec.dot(vec))
# unit vector
print(magnitude(T))
print(magnitude(T/magnitude(T)))
A = np.array([1,2])
B = np.array([3,5])
print(A+B)