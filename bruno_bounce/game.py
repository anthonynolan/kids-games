#!/usr/bin/env python3

import sys, pygame
import pickle

import os

# os.chdir(f"{os.getcwd()}/bruno_bounce")
pygame.init()

size = width, height = 1480, 700

speed = [1, 1]
speed2 = [2, -2]

black = 0, 0, 0

screen = pygame.display.set_mode(size)


hound = pygame.image.load("resources/little-hound.jpg")
ball = pygame.image.load("resources/little-hound.jpg")

hound = pygame.transform.scale(hound, (50, 50))
houndrect = hound.get_rect()
ballrect = ball.get_rect()
ballrect.center = (150, 100)

font = pygame.font.Font("freesansbold.ttf", 32)

houndrect.center = (400, 400)

begin = pygame.time.get_ticks()

score = 0
delay = 5

bg = pygame.image.load("resources/family.png")

import os

filename = "scoreboard.pkl"
if os.path.isfile(filename):
    scoreboard = pickle.load(open(filename, "rb"))
    print(sorted(scoreboard, reverse=True))
else:
    scoreboard = []

# from tkinter import *
# from tkinter import messagebox


def end_game():

    print("GAME OVER")
    speed_change()
    scoreboard.append(score)
    scoreboard.sort(reverse=True)

    pickle.dump(scoreboard, open(filename, "wb"))

    # Tk().wm_withdraw()  # to hide the main window
    # messagebox.showinfo(
    #     "You are brutal",
    #     f"you are in position {scoreboard.index(score)} out of {len(scoreboard)}. final score {score:,}",
    # )

    sys.exit()


def speed_change():
    pygame.mixer.Sound("resources/dog.mp3").play()
    global speed
    global delay
    delay = delay - 1
    speed[0] = speed[0] * 1.1
    speed[1] = speed[1] * 1.1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == "p" or event.key == 1073741903:
                # righto
                speed[0] = 1
            elif event.unicode == "o" or event.key == 1073741904:
                # left
                speed[0] = -1
            elif event.unicode == "q" or event.key == 1073741906:
                # up
                speed[1] = -1
            elif event.unicode == "a" or event.key == 1073741905:
                # down
                speed[1] = 1
            elif event.key == 32:
                speed_change()

    houndrect = houndrect.move(speed)
    if houndrect.left < 0 or houndrect.right > width:
        end_game()
    if houndrect.top < 0 or houndrect.bottom > height:
        end_game()

    ballrect = ballrect.move(speed2)
    if ballrect.left < 0 or ballrect.right > width:
        speed2[0] = -speed2[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(black)
    # screen.blit(bg, (0, 0))
    screen.blit(hound, houndrect)
    screen.blit(ball, ballrect)
    if houndrect.colliderect(ballrect):
        end_game()

    end = pygame.time.get_ticks()
    elapsed = end - begin
    score = elapsed * ((6 - delay) ** 2)

    sc = font.render(str(score), True, (255, 255, 255))
    screen.blit(sc, (20, 20))
    pygame.display.flip()

    pygame.time.wait(delay)
