#!/usr/bin/env python

import pygame
import numpy as np

screen_dims  = np.array([1920,1080])

screen = pygame.display.set_mode(screen_dims, 0, 32)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    screen.fill((255,255,255))

    centre = screen_dims//2
    ship_length = 50
    ship = pygame.draw.polygon(screen, (255, 0,0),
        [
            (centre),
            (centre+np.array([ship_length, 0])), 
            (centre+np.array([ship_length, ship_length])),
            (centre+np.array([0, ship_length])), 
            
        ]
    )

    # screen.blit(ship, (100,100))

    
    
    pygame.display.update()