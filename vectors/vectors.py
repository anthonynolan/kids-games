#!/usr/bin/env python

import pygame
import numpy as np
from Asteroid import Asteroid
from Ship import Ship
from utils import degrees_to_radians

BLACK = (0,0,0)
RED = (255,0,0)

screen_dims  = np.array([640,480])

pygame.init()

screen = pygame.display.set_mode(screen_dims, 0, 32)
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

ship = Ship(screen_dims, screen_dims/2)

acc_const = 3

accelerating = False
rotating = np.array([0,0])

asteroids = [Asteroid(screen_dims) for _ in range(5)]

print(asteroids)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                accelerating = True
            if event.key == pygame.K_LEFT:
                rotating[0] = True
            if event.key == pygame.K_RIGHT:
                rotating[1] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                accelerating = False
            if event.key == pygame.K_LEFT:
                rotating[0] = False
            
            if event.key == pygame.K_RIGHT:
                rotating[1] = False
                
    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000

    if rotating[0]:
        ship.rotation_angle -=degrees_to_radians(10)
    if rotating[1]:
        ship.rotation_angle +=degrees_to_radians(10)

    if accelerating:
        ship.acc[0] += acc_const * np.cos(degrees_to_radians(ship.rotation_angle))
        ship.acc[1] += acc_const * np.sin(degrees_to_radians(ship.rotation_angle))
    else:
        ship.acc = np.array([0,0])

    # velocity
    ship.vel +=ship.acc*time_passed_seconds
    ship.pos+=ship.vel*time_passed_seconds

    ship.check_bounds()

    screen.fill(BLACK)

    screen.blit(pygame.transform.rotate(ship.image, -ship.rotation_angle), ship.pos)

    for asteroid in asteroids:
        asteroid.move(time_passed_seconds)
        pygame.draw.circle(screen, (0, 255, 0), asteroid.pos, asteroid.radius)

    pygame.display.update()