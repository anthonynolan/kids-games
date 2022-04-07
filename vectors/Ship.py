import numpy as np
import pygame
from Roller import Roller
from utils import rotate, degrees_to_radians, normalize, degrees_to_cartesian

rotation_const = 100
acc_const = 3

class Ship(Roller):
    def __init__(self, screen, screen_dims, pos = np.array([0.,0.]), vel =np.array([0.,0.]), acc=np.array([0.,0.]), radius=5):
        super().__init__(screen_dims)
        
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
        self.rotation_angle = 0
        self.screen = screen

        self.origin = np.array([0,0])
        self.gun = self.screen_dims/2
        self.rect = None

    def move(self, time_passed_seconds, rotating, accelerating):


        if rotating[1]:
            self.rotation_angle -=rotation_const*time_passed_seconds
        if rotating[0]:
            self.rotation_angle +=rotation_const*time_passed_seconds

        if accelerating:
            self.acc[0] += acc_const * np.cos(degrees_to_radians(self.rotation_angle-120))
            self.acc[1] += acc_const * np.sin(degrees_to_radians(self.rotation_angle-120))
            print(f'acceleration {self.acc}')
        else:
            self.acc = np.array([0,0])

        # velocity
        self.vel +=self.acc*time_passed_seconds
        self.pos+=self.vel*time_passed_seconds

        self.check_bounds()

        ship_length = 50

        centre = np.array([ship_length/2,ship_length/2])

        hull_angle = 60
        points = np.array([self.origin,
                np.array([ship_length, self.origin[1]]), 
                np.array([ship_length*np.cos(degrees_to_radians(hull_angle)), ship_length*np.sin(degrees_to_radians(hull_angle))])])

        points = [(rotate(point-centre, self.rotation_angle)+centre)+self.screen_dims/2 for point in points]
        self.gun = points[0]
        
        self.rect = pygame.draw.polygon(self.screen, (0, 255,0),
                points+self.pos-self.screen_dims/2, 1
        )
        pygame.draw.circle(self.screen, (255,0,0), points[0]+self.pos-self.screen_dims/2, 1)

        pygame.draw.line(self.screen, (255, 0, 0), self.screen_dims/2, self.screen_dims/2+normalize(self.acc), width=10)
        pygame.draw.line(self.screen, (255, 0, 255), self.screen_dims/2, self.screen_dims/2+normalize(self.vel), width=5)
        pygame.draw.line(self.screen, (0, 0, 255), self.screen_dims/2, self.screen_dims/2+degrees_to_cartesian(self.rotation_angle), width=5)

    def __repr__(self):
        return f'{self.pos, self.vel, self.acc, self.rotation_angle}'


