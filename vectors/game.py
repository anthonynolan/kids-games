#!/usr/bin/env python

import pygame
import numpy as np
from Asteroid import Asteroid
from Ship import Ship
from Bullet import Bullet
from utils import degrees_to_radians

BLACK = (0,0,0)
RED = (255,0,0)

screen_dims  = np.array([1920,1080])

pygame.init()

screen = pygame.display.set_mode(screen_dims, 0, 32)
print(pygame.display.list_modes())

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

ship = Ship(screen, screen_dims, screen_dims/2)

acc_const = 3
rotation_const = 100
bullet_velocity_const = 150

asteroid_count = 10

accelerating = False
rotating = np.array([0,0])

asteroids = [Asteroid(screen_dims) for _ in range(asteroid_count)]
bullets = []
score = 0
# print(asteroids)

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
            if event.key==pygame.K_SPACE:
                pygame.mixer.Sound('../resources/hq-explosion-6288.mp3').play()   

                bullet = Bullet(ship.pos, ship.rotation_angle, bullet_velocity_const)
                bullets.append(bullet)
                

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
        ship.rotation_angle -=rotation_const*time_passed_seconds
    if rotating[1]:
        ship.rotation_angle +=rotation_const*time_passed_seconds

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
        asteroid.rect= pygame.draw.circle(screen, (0, 255, 0), asteroid.pos, asteroid.radius)

    for bullet in bullets:
        bullet.move(time_passed_seconds)
        bullet.rect = pygame.draw.circle(screen, (0, 0, 255), bullet.pos, bullet.radius)

    # collision detection

    for asteroid in asteroids:
        for bullet in bullets:
            if asteroid.rect.colliderect(bullet.rect):
                pygame.mixer.Sound('../resources/bad-explosion-6855.mp3').play()   
                asteroids.remove(asteroid)
                score+=10


    sc = font.render(f'Score: {str(score)}', True, (255,255,255))
    screen.blit(sc, (20,20)) 

    pygame.display.update()