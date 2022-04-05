#!/usr/bin/env python

import pygame
import numpy as np
from utils import rotate, rotate_polygon, degrees_to_radians

screen_dims  = np.array([1920,1080])

screen = pygame.display.set_mode(screen_dims, 0, 32)

clock = pygame.time.Clock()

ship_length = 50

centre = np.array([ship_length/2,ship_length/2])
origin = np.array([0,0])

angle = 60
points = np.array([origin,
        np.array([ship_length, origin[1]]), 
        np.array([ship_length*np.cos(degrees_to_radians(angle)), ship_length*np.sin(degrees_to_radians(angle))])])

angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    screen.fill((255,255,255))

    points = [rotate(point-centre, angle)+centre for point in points]
    # points = rotate_polygon(points, angle)
    angle=clock.tick()/1000*100
    print(angle)
    
    temp=[point+np.array([500,500]) for point in points]
    print (temp)
    ship = pygame.draw.polygon(screen, (0, 255,0),
            temp, 1
    )

    pygame.display.update()
    