import numpy as np
import random
import numpy as np
from utils import degrees_to_radians
from Roller import Roller
import pygame

class Asteroid(Roller):
    velocity_constant = 180
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.pos = self.screen_dims[0] * random.uniform(0,1), self.screen_dims[1] * random.uniform(0,1)
        angle = random.uniform(0,360)
        self.vel = np.array([self.velocity_constant*np.cos(degrees_to_radians(angle)), self.velocity_constant*np.sin(degrees_to_radians(angle))])
        self.radius = 20
        self.rect = None

    def move(self, time_passed_seconds):
        self.pos+=self.vel*time_passed_seconds
        self.check_bounds()
        self.rect= pygame.draw.circle(self.screen, (0, 255, 0), self.pos, self.radius)
    

    def __repr__(self):
        return f'{self.pos, self.vel}'



