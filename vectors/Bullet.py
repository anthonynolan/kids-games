import numpy as np
import numpy as np
from utils import degrees_to_radians

class Bullet:
    def __init__(self, starting_pos, ship_rotation_angle, velocity_constant):
        self.pos = starting_pos.copy()
        self.vel = np.array([np.sin(degrees_to_radians(ship_rotation_angle-120)), np.cos(degrees_to_radians(ship_rotation_angle-120))])*velocity_constant
        self.radius = 3
        self.rect = None

    def move(self, time_passed_seconds):
        self.pos+=self.vel*time_passed_seconds

    def __repr__(self):
        return f'{self.pos, self.vel}'



