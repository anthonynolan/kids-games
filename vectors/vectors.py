#!/usr/bin/env python

import pygame
import numpy as np
import random

from Ball import Ball

BLACK = (0,0,0)
RED = (255,0,0)
h = '3bfafa'
PALE_BLUE =  tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

screen_dims  = np.array([640,480])

pygame.init()

screen = pygame.display.set_mode(screen_dims, 0, 32)
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

def field(pos):
    black_hole_loc = np.array([640,480])/4
    distance = np.linalg.norm(pos - black_hole_loc)
    f = (black_hole_loc-pos)/distance
    print(f)
    return f, black_hole_loc

g = np.array([0, -9.81]) 
factor = 10000

balls = [Ball(np.array([screen_dims[0]/(2*random.uniform(0,2)),screen_dims[1]/(2*random.uniform(0,2))]) , np.array([0., 0.]), 10) for _ in range(20)]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    time_passed = clock.tick()
    time_passed_seconds = time_passed/10000

    screen.fill(BLACK)

    for ball in balls:
        if ball.pos[0] >= (screen_dims[0]-ball.radius):
            ball.pos[0] = screen_dims[0]-ball.radius
            ball.vel[0] = -ball.vel[0]*.9

        if ball.pos[0]<= ball.radius:
            ball.pos[0] = ball.radius
            ball.vel[0] = -ball.vel[0]*.9

        if ball.pos[1] >= (screen_dims[1]-ball.radius):
            ball.pos[1] = screen_dims[1]-ball.radius
            ball.vel[1] = -ball.vel[1]*.9

        if ball.pos[1]<= ball.radius: 
            ball.pos[1] = ball.radius
            ball.vel[1] = -ball.vel[1]*.9

        # ball.vel = ball.vel - g*time_passed_seconds
        field_strength, black_hole_loc = field(ball.pos)

        ball.vel = ball.vel - time_passed_seconds*field_strength*factor
        ball.pos += time_passed_seconds*ball.vel

        

        pygame.draw.circle(screen, RED, ball.pos, ball.radius, 1)
        pygame.draw.circle(screen, PALE_BLUE, black_hole_loc, 5)

    # velocity_text = font.render(str(ball.pos.astype(int)), True, (255,255,255))
    # screen.blit(velocity_text, (20,20)) 

    pygame.display.update()