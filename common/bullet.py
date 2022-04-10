import numpy as np
import numpy as np

import sys
sys.path.insert(0, '../')
import common.utils

class Bullet:
    def __init__(self, starting_pos, ship_rotation_angle, velocity_constant):
        self.pos = starting_pos.copy()
        self.vel = np.array([np.sin(common.utils.degrees_to_radians(ship_rotation_angle-120)), np.cos(common.utils.degrees_to_radians(ship_rotation_angle-120))])*velocity_constant
        self.radius = 3
        self.rect = None

    def move(self, time_passed_seconds):
        self.pos+=self.vel*time_passed_seconds

    def __repr__(self):
        return f'{self.pos, self.vel}'



