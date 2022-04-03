import numpy as np
import random
import numpy as np
from utils import degrees_to_radians

class Bullet:
    def __init__(self, pos, ship_rotation_angle, velocity_constant):
        print(ship_rotation_angle)
        self.pos = pos.copy()
        self.vel = np.array([np.cos(degrees_to_radians(ship_rotation_angle)), np.sin(degrees_to_radians(ship_rotation_angle))])*velocity_constant
        self.radius = 3
        self.rect = None
        print(self)

    def move(self, time_passed_seconds):
        self.pos+=self.vel*time_passed_seconds

    def __repr__(self):
        return f'{self.pos, self.vel}'



