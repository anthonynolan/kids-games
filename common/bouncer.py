import pygame

class Bouncer:
    bounce_dirs = [0, 0]
    def __init__(self):
        self.screen_dims = pygame.display.get_window_size()

    def check_bounds(self):
        bounce = False
        for dim in [0, 1]:
            if (self.pos[dim] > self.screen_dims[dim]-self.radius):
                #  & (self.bounce_dirs[dim]<1) :
                self.vel[dim] = -self.vel[dim]
                self.bounce_dirs[dim] = 1
                bounce = True

            if (self.pos[dim] < 0+self.radius):
                #  & (self.bounce_dirs[dim]>-1) :
                self.vel[dim] = -self.vel[dim]
                self.bounce_dirs[dim] = -1
                bounce = True
            
        return bounce
