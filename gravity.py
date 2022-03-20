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

	if pygame.key.get_pressed()[pygame.K_UP]: 
		accel = True 
	else: 
		accel = False

	screen.fill(black)

	particle.move(accel)
	particle.display()
	
	pygame.display.flip()					
	
	pygame.time.wait(delay)

