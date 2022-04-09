from Roller import Roller
import numpy as np
import pygame 
from pygame import Rect

class SpriteShip(Roller):
    velocity_const = 240
    ship_width = 30
    ship_length = 40

    def __init__(self, screen):
        super().__init__()
        self.screen_dims = np.array(pygame.display.get_window_size())
        self.pos = np.array([0,self.screen_dims[1]-(2*self.ship_length)], np.float32)
        self.screen = screen
        self.rect = None
        self.direction = np.array([0,0])
        self.velocity = np.array([0,0], np.float32)

    def move(self, time_passed_seconds, direction):
        
        self.direction = direction 
        self.velocity += self.direction*self.velocity_const*time_passed_seconds
        self.pos += self.velocity*time_passed_seconds
        self.check_bounds()

        self.rect = pygame.draw.rect(self.screen, (0, 255,255),
                Rect(*self.pos, self.ship_width, self.ship_length)
        )

    def __repr__(self):
        return f'{self.pos}'


