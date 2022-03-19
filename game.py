import sys, pygame
from Particle import Particle

screen_size = width, height = 800, 600
black = 0,0,0
delay = 0

pygame.init()
screen = pygame.display.set_mode(screen_size)

particle =  Particle((width//2, height//2), screen_size, screen)

while True:
	accel = False
	for event in pygame.event.get():
		if event.type ==pygame.QUIT: sys.exit()
		elif event.type==pygame.KEYDOWN:	
			if event.key==1073741906:
				# accelerate
				accel = True

	screen.fill(black)

	particle.move(accel)
	particle.display()
	
	pygame.display.flip()					
	
	pygame.time.wait(delay)

