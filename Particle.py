import random
import pygame
import numpy as np

const_accel = 40

class Particle:

	def __init__(self, screen_dims):
		
		self.width, self.height = screen_dims
		self.x, self.y = self.width//2, self.height//2

		self.rotation_angle = 0

		self.vx = 0
		self.vy = 0
		self.ticks = pygame.time.get_ticks()

	def rotate_left(self):
		self.rotation_angle -=10
		print(self.rotation_angle)
	def rotate_right(self):
		self.rotation_angle +=10
		print(self.rotation_angle)

	def move(self, dt):

		ax = const_accel *np.cos(self.rotation_angle)
		ay = const_accel *np.sin(self.rotation_angle)

		self.vx +=ax*dt/1000
		self.vy +=ay*dt/1000

		self.x +=(self.vx*dt/1000)
		self.y +=(self.vy*dt/1000)
		if self.x>self.width: self.x = 0
		if self.y>self.height: self.y = 0
		if self.x<0: self.x = self.width
		if self.y<0: self.y = self.height


			
