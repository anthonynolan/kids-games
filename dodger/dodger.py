#!/usr/bin/env python

import pygame
import pygame.camera

import numpy as np
from tkinter import *
from tkinter import messagebox
import sys
sys.path.insert(0,'../')
import common.asteroid
import spriteship


screen_dims  = np.array([800, 600])
asteroid_count = 0
lives = 3

pygame.init()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

pygame.camera.init()
backends = pygame.camera.get_backends()
print(backends)



screen = pygame.display.set_mode(screen_dims, 0, 32)


cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (640, 480))
cam.start()

clock = pygame.time.Clock()


font = pygame.font.Font('freesansbold.ttf', 32)


asteroids = [common.asteroid.Asteroid(screen) for _ in range(asteroid_count)]
spriteShip = spriteship.SpriteShip(screen)

direction = np.array([0,0])

def left():
    return np.array([-1,0])
def right():
     return np.array([1,0])
def up():
    return np.array([0,-1])
def down():
    return np.array([0,1])


import tensorflow as tf
new_model = tf.keras.models.load_model('../model')

# Check its architecture
new_model.summary()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RIGHT:
                direction =right()
            
            if event.key == pygame.K_LEFT:
                direction = left()
            
            if event.key == pygame.K_DOWN:
                direction = down()

            if event.key == pygame.K_UP:
                direction = up()

        if event.type == pygame.KEYUP:
            direction = np.array([0,0])

        direction = np.array([0,0])
        if event.type == pygame.JOYAXISMOTION:
            print(event)
            if (event.axis == 0) & (event.value>.1):
                direction = right()
            elif (event.axis == 0) & (event.value<-.1):
                direction = left()

            elif (event.axis == 1) & (event.value>.1):
                direction = down()
            elif (event.axis == 1) & (event.value<-.1):
                direction = up()

        elif event.type == pygame.JOYBUTTONDOWN:
            print(event)
    image = cam.get_image()
    # print(image)
    image_array = pygame.surfarray.array3d(image)
    # print(image_array.shape)
    
    print("aoife" if np.argmax(new_model.predict(tf.expand_dims(tf.image.resize(image_array, (224,224)), 0)))==0 else "cathal")


    # screen.fill((0,0,0))
    screen.blit(image, (0,0))

    
    time_elapsed_seconds = clock.tick()/1000

    # spriteShip.move(time_elapsed_seconds, direction)
    # for asteroid in asteroids:
    #     asteroid.move(time_elapsed_seconds)
    #     if asteroid.rect.colliderect(spriteShip.rect):
    #         asteroids.remove(asteroid)
    #         pygame.mixer.Sound('../resources/hq-explosion-6288.mp3').play()   
    #         lives -=1
    #         if lives==0:
    #             Tk().wm_withdraw() #to hide the main window
    #             messagebox.showinfo('Game Over')
    #             sys.exit()     
    
    # sc = font.render(f'lives: {lives}, time: {(pygame.time.get_ticks()/1000):.1f} seconds', True, (255,255,255))
    # screen.blit(sc, (20,20)) 

    pygame.display.update()
    