import numpy as np
import random
import numpy as np
from common.utils import *
import common.bouncer
import pygame

class Asteroid(common.bouncer.Bouncer):
    velocity_constant = 180
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.pos = self.screen_dims[0]/4+(self.screen_dims[0]/4 * random.uniform(0,1)), 
        self.screen_dims[1]/4+(self.screen_dims[1]/4 * random.uniform(0,1))
        angle = random.uniform(0,360)
        self.vel = np.array([self.velocity_constant*np.cos(degrees_to_radians(angle)), self.velocity_constant*np.sin(degrees_to_radians(angle))])
        self.radius = 10
        self.rect = None

    def move(self, time_passed_seconds):
        self.pos+=self.vel*time_passed_seconds
        self.check_bounds()

        self.rect= pygame.draw.circle(self.screen, (0, 255, 0), self.pos, self.radius)
        
    

    def __repr__(self):
        return f'{self.pos, self.vel}'



