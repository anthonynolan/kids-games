from random import randint, uniform
from math import pi
import pygame
import numpy as np
import sys


class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.rotation_angle = 0
        self.x = 0
        self.y = 0

    def to_pixels(self, screen_size):
        width, height = screen_size
        return width/2 + width * self.x/ 20, height/2 - height * self.y / 20

    def __repr__(self):
        return str(f'{self.points, self.x, self.y}')

class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(.5, 0), (-.25,.25), (-.25, -.25)])


def to_cartesian(length, angle):
    return length*np.cos(angle), length*np.sin(angle)

class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        vs = [to_cartesian(uniform(.5, 1), 2*pi*i/sides ) for i in range(sides)]
        super().__init__(vs)

asteriod_count = 3

asteroids = [Asteroid() for _ in range(asteriod_count)]
for ast in asteroids:
    ast.x = randint(-9, 9)
    ast.y = randint(-9,9)

screen_size =(800, 600)
screen = pygame.display.set_mode(screen_size, 0)


running = True
while running:
    for event in pygame.event.get():
	    if event.type ==pygame.QUIT: 
		    pygame.quit()
            # sys.exit()
	
    screen.fill((0,0,0))

    pixel_points = [ast.to_pixels(screen_size) for ast in asteroids]
    
    pygame.draw.aalines(screen, (0, 255, 0), True, pixel_points, 10)

    pygame.display.flip()					
