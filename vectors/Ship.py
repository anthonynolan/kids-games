import numpy as np
import pygame
from Roller import Roller

class Ship(Roller):
    def __init__(self, screen_dims, pos = np.array([0.,0.]), vel =np.array([0.,0.]), acc=np.array([0.,0.]), radius=5):
        super().__init__(screen_dims)
        
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
        self.rotation_angle = 0
        self.image = pygame.transform.rotate(pygame.image.load('../resources/ship.png'), -90)

    def __repr__(self):
        return f'{self.pos, self.vel, self.acc, self.rotation_angle}'


