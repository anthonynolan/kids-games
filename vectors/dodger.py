#!/usr/bin/env python

import pygame
import numpy as np

screen_dims  = np.array([1920,1080])

screen = pygame.display.set_mode(screen_dims, 0, 32)

clock = pygame.time.Clock()

from Asteroid import Asteroid
from SpriteShip import SpriteShip

asteroid_count = 100

asteroids = [Asteroid(screen) for _ in range(asteroid_count)]
spriteShip = SpriteShip(screen)

direction = np.array([0,0])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                direction = np.array([-1,0])
            
            if event.key == pygame.K_LEFT:
                direction = np.array([1,0])
            
            if event.key == pygame.K_DOWN:
                direction = np.array([0,1])
            if event.key == pygame.K_UP:
                direction = np.array([0,-1])
        if event.type == pygame.KEYUP:
            direction = np.array([0,0])

    screen.fill((0,0,0))
    
    time_elapsed_seconds = clock.tick()/1000

    for asteroid in asteroids:
        asteroid.move(time_elapsed_seconds)
    spriteShip.move(time_elapsed_seconds, direction)
    pygame.display.update()
    