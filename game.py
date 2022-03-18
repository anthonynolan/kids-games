import sys, pygame
import random
import math

pygame.init()

screen_size = width, height = 800, 600

black = 0,0,0

screen = pygame.display.set_mode(screen_size)

delay = 10
class Particle:
	def __init__(self, pos, size):
		self.x, self.y = pos
		self.size = size
		self.color = (0,0,255)
		self.thickness = 3
		# self.speed = 0.1
		# self.angle = 0
		self.vx = random.randint(0,10)
		self.vy = random.randint(0,10)

	def display(self):
		# print(screen, self.color, (self.x, self.y), self.size)
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

	def move(self):
		millis = pygame.time.get_ticks()
		print(millis)

		self.x +=(self.vx*millis/1000)
		self.y +=(self.vy*millis/1000)
		if self.x>width: self.x = 0
		if self.y>height: self.y = 0
		if self.x<0: self.x = width
		if self.y<0: self.y = height

	
size = random.randint(20, 30)
x = random.randint(size, width-size)
y = random.randint(size, height-size)

particle =  Particle((x, y), size)


while True:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT: sys.exit()

	screen.fill(black)
	particle.move()
	particle.display()
	pygame.display.flip()					
	

	pygame.time.wait(delay)

