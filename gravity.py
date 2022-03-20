import sys, pygame
from Particle import Particle

screen_size = width, height = 800, 600
black = 0,0,0
delay = 0

pygame.init()
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font('freesansbold.ttf', 32)

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
	
	velocity_text = font.render(str([particle.vx, particle.vy]), True, (255,255,255))
	screen.blit(velocity_text, (20,20)) 

	pygame.display.flip()					
	
	pygame.time.wait(delay)

