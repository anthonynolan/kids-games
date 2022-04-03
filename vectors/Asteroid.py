import numpy as np
import random
import numpy as np
from utils import degrees_to_radians
from Roller import Roller

class Asteroid(Roller):
    velocity_constant = 40
    def __init__(self, screen_dims):
        super().__init__(screen_dims)
        self.pos = screen_dims[0] * random.uniform(0,1), screen_dims[1] * random.uniform(0,1)
        angle = random.uniform(0,360)
        self.vel = np.array([self.velocity_constant*np.cos(degrees_to_radians(angle)), self.velocity_constant*np.sin(degrees_to_radians(angle))])
        self.radius = 10
        self.rect = None

    def move(self, time_passed_seconds):
        self.pos+=self.vel*time_passed_seconds
        self.check_bounds()
    

    def __repr__(self):
        return f'{self.pos, self.vel}'



