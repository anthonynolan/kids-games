import numpy as np

def field(pos):
    black_hole_loc = np.array([640,480])/4
    distance = np.linalg.norm(pos - black_hole_loc)
    print(distance)
    f = 1/distance
    print(f)
    return

field(np.array([640,480]))
field(np.array([340,480]))
