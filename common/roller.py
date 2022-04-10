import pygame

class Roller:
    def __init__(self):
        self.screen_dims = pygame.display.get_window_size()

    def check_bounds(self):
        for dim in [0, 1]:
            if self.pos[dim] > self.screen_dims[dim]:
                self.pos[dim] = 0

            if self.pos[dim] < 0:
                self.pos[dim] = self.screen_dims[dim] 
