import numpy as np
import pygame
from Roller import Roller
from utils import rotate

class Ship(Roller):
    def __init__(self, screen, screen_dims, pos = np.array([0.,0.]), vel =np.array([0.,0.]), acc=np.array([0.,0.]), radius=5):
        super().__init__(screen_dims)
        
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
        self.rotation_angle = 0
        graphic_type = 'image'
        if graphic_type == 'image':
            im = pygame.image.load('../resources/ship.png')
            self.image = pygame.transform.rotate(im, -90)
        else:
            im = pygame.draw.circle(screen, (0,255,0), self.pos, 5)
            self.image = rotate(im, -90)

    def __repr__(self):
        return f'{self.pos, self.vel, self.acc, self.rotation_angle}'


