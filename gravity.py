import sys, pygame
from Particle import Particle

screen_size = width, height = 800, 600
black = 0,0,0
delay = 0

pygame.init()
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
font = pygame.font.Font('freesansbold.ttf', 32)

particle =  Particle((width//2, height//2), screen_size, screen)

running = True
while running:
	accel = False

	for event in pygame.event.get():
		if event.type ==pygame.QUIT: 
			pygame.quit()
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				running = False

	if pygame.key.get_pressed()[pygame.K_UP]: 
		accel = True 
	else: 
		accel = False

	screen.fill(black)

	particle.move(accel)
	particle.display()
	
	velocity_text = font.render(str([int(particle.vx), int(particle.vy)]), True, (255,255,255))
	screen.blit(velocity_text, (20,20)) 

	pygame.display.flip()					
	
	pygame.time.wait(delay)

