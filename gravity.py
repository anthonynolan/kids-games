import sys, pygame
from Particle import Particle

screen_size = width, height = 800, 600
black = 0,0,0
delay = 0

pygame.init()
screen = pygame.display.set_mode(screen_size, 0)
font = pygame.font.Font('freesansbold.ttf', 32)

particle =  Particle( screen_size)

color = (0,0,255)

now = pygame.time.get_ticks()

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
			if event.key==pygame.K_LEFT:
				particle.rotate_left()
			if event.key==pygame.K_RIGHT:
				particle.rotate_right()


	if pygame.key.get_pressed()[pygame.K_UP]: 
		# calc the move
		pass
	
	screen.fill(black)


	dt = now - pygame.time.get_ticks()
	now = pygame.time.get_ticks()
	
	particle.move(dt)
	
	pygame.draw.circle(screen, color, (particle.x, particle.y), 10)

	
	velocity_text = font.render(str([int(particle.vx), int(particle.vy)]), True, (255,255,255))
	screen.blit(velocity_text, (20,20)) 

	pygame.display.flip()					
	
	# pygame.time.wait(delay)

