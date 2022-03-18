import sys, pygame
import random
import math

pygame.init()

screen_size = width, height = 800, 600

black = 0,0,0

screen = pygame.display.set_mode(screen_size)

delay = 0
class Particle:
	def __init__(self, pos, size):
		self.x, self.y = pos
		self.size = size
		self.color = (0,0,255)
		self.thickness = 3
		self.speed = 0.1
		self.angle = 0

	def display(self):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)

	def move(self):
		self.x +=math.sin(self.angle)*self.speed
		self.y -=math.cos(self.angle)*self.speed

	
size = random.randint(20, 30)
x = random.randint(size, width-size)
y = random.randint(size, height-size)

particle =  Particle((x, y), size)


while True:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT: sys.exit()

	# jump_size = 5
	# x = x+(jump_size if random.randint(0,10)>5 else -1*jump_size)
	# if x<0: x = 0
	# if x>width: x = width

	# y = y+(jump_size if random.randint(0,10)>5 else -1*jump_size)
	# if y<0: y = 0
	# if y>height: y = height
	# print(x)
	# particle.x = x
	# particle.y = y
	screen.fill(black)
	particle.move()
	particle.display()
	pygame.display.flip()					
	

	# pygame.time.wait(delay)

