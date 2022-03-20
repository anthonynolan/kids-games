import random
import pygame

const_accel = 20

class Particle:

	def __init__(self, pos, screen_dims, screen):
		self.x, self.y = pos
		self.width, self.height = screen_dims
		self.screen = screen

		self.color = (0,0,255)
		self.vx = random.randint(0,100)
		self.vy = random.randint(0,100)
		self.ticks = pygame.time.get_ticks()

	def display(self):
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), 10)

	def move(self, acceleration):
		now = pygame.time.get_ticks()
		dt = now - self.ticks
		self.ticks = now

		if acceleration:
			self.vx +=const_accel*dt/1000
			self.vy +=const_accel*dt/1000

		# print(self.vx, self.vy)
		self.x +=(self.vx*dt/1000)
		self.y +=(self.vy*dt/1000)
		if self.x>self.width: self.x = 0
		if self.y>self.height: self.y = 0
		if self.x<0: self.x = self.width
		if self.y<0: self.y = self.height

