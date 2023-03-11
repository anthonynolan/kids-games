#!/usr/bin/env python

import pygame
import numpy as np

# from tkinter import *
# from tkinter import messagebox

import sys

sys.path.insert(0, "../")

import common.asteroid
import common.bullet

import ship

from common.utils import *


BLACK = (0, 0, 0)
RED = (255, 0, 0)

# screen_dims  = np.array([1440,900])
screen_dims = np.array([800, 600])

pygame.init()

screen = pygame.display.set_mode(screen_dims, 0, 32)
print(pygame.display.list_modes())


background = pygame.image.load("../resources/background.png")
clock = pygame.time.Clock()

font = pygame.font.Font("freesansbold.ttf", 32)

# ship = ship.Ship(screen, screen_dims, screen_dims / 2)


bullet_velocity_const = 250

asteroid_count = 20

accelerating = False
rotating = np.array([0, 0])

asteroids = [common.asteroid.Asteroid(screen) for _ in range(asteroid_count)]
bullets = []
score = 0
lives = 3

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
                rotating[1] = True
            if event.key == pygame.K_RIGHT:
                rotating[0] = True
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound("../resources/hq-explosion-6288.mp3").play()

                # bullet = common.bullet.Bullet(
                #     ship.gun, ship.rotation_angle, bullet_velocity_const
                # )
                # bullets.append(bullet)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                accelerating = False
            if event.key == pygame.K_LEFT:
                rotating[1] = False

            if event.key == pygame.K_RIGHT:
                rotating[0] = False

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000

    screen.blit(background, (0, 0))

    # ship.move(time_passed_seconds, rotating, accelerating)

    for asteroid in asteroids:
        asteroid.move(time_passed_seconds)
        asteroid.rect = pygame.draw.circle(
            screen, (0, 255, 0), asteroid.pos, asteroid.radius
        )

    for bullet in bullets:
        bullet.move(time_passed_seconds)
        bullet.rect = pygame.draw.circle(screen, (0, 0, 255), bullet.pos, bullet.radius)

    # collision detection

    # for asteroid in asteroids:
    #     if asteroid.rect.colliderect(ship.rect):
    #         asteroids.remove(asteroid)
    #         pygame.mixer.Sound("../resources/bad-explosion-6855.mp3").play()
    #         lives -= 1
    #         if lives == 0:
    #             # Tk().wm_withdraw() #to hide the main window
    #             # messagebox.showinfo('Game Over')
    #             sys.exit()

    #     for bullet in bullets:
    #         if asteroid.rect.colliderect(bullet.rect):
    #             pygame.mixer.Sound("../resources/bad-explosion-6855.mp3").play()
    #             asteroids.remove(asteroid)
    #             score += 10

    # sc = font.render(f"Score: {str(score)} lives: {lives}", True, (255, 255, 255))
    # screen.blit(sc, (20, 20))

    pygame.display.update()
