#!/usr/bin/env python3
import pygame
import sys


def main():
    # Initialize Pygame
    pygame.init()

    # Set the size of the window
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 1000
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Set the color of the background
    BACKGROUND_COLOR = (0, 0, 0)

    # Set the speed of the players
    PLAYER_SPEED = 5

    # Set the size of the players
    PLAYER_SIZE = (10, 10)

    screen = pygame.display.set_mode(SCREEN_SIZE)

    # Create the clock to regulate the frame rate
    clock = pygame.time.Clock()

    # Create the surface for the player trails
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    surface.set_colorkey((0, 0, 0))

    image = pygame.image.load("smalley2.jpg")
    background = pygame.image.load("lick.jpg")
    # Main game loop
    running = True

    start_xpos = SCREEN_WIDTH // 2
    start_ypos = 0

    xpos = start_xpos
    ypos = start_ypos
    # how many pixels we move our smiley each frame
    step_x = 1
    step_y = 0.1

    # s = ut + 1/2 at**2
    # initial u for us is 0, so reduces to 1/2at^2

    begin = pygame.time.get_ticks()

    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if xpos > SCREEN_WIDTH - image.get_width() or xpos < 0:
            step_x = -step_x
        if ypos > SCREEN_HEIGHT - image.get_height() or ypos < 0:
            step_y = -step_y
        # update the position of the smiley
        # xpos += step_x  # move it to the right
        update = 0.5 * 9.81 * (((begin - pygame.time.get_ticks()) / 1000) ** 2)
        if update > 100:
            begin = pygame.time.get_ticks()
            xpos = start_xpos
            ypos = start_ypos

        print(update)
        ypos += update * step_y  # move it down

        screen.blit(background, (0, 0))
        screen.blit(image, (xpos, ypos))
        pygame.display.flip()


if __name__ == "__main__":
    main()
