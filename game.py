import sys, pygame

pygame.init()

size = width, height = 800, 600

speed = [1, 1]
black = 0,0,0

screen = pygame.display.set_mode(size)


ball = pygame.image.load('little-hound.jpg')
ballrect = ball.get_rect()

begin = pygame.time.get_ticks()

score = 0
delay = 5

bg = pygame.image.load('family.png')

def end_game():
	
	print('GAME OVER')
	speed_change()
	print(f'final score {score:,}')
	sys.exit()        

def speed_change():
	pygame.mixer.Sound('dog.mp3').play()   
	global begin
	global score
	global delay
	end = pygame.time.get_ticks()
	elapsed = end-begin
	score = score+(elapsed*((10-delay)**2))
	delay = delay-1
	begin = end
	print(f'speed is {10-delay}')


while True:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT: sys.exit()
		if event.type ==pygame.KEYDOWN:
			if event.unicode=='p':
				# righto
				speed[0] = 1
			elif event.unicode=='o':
				# left
				speed[0] = -1
			elif event.unicode=='q':
				# up
				speed[1] = -1
			elif event.unicode=='a':
				# down
				speed[1] = 1
			elif event.key==32:
				speed_change()
				

	ballrect = ballrect.move(speed)
	if ballrect.left<0 or ballrect.right > width:
		speed[0] = -speed[0]
		end_game()
	if ballrect.top < 0 or ballrect.bottom> height:
		speed[1] = -speed[1]
		end_game()

	screen.fill(black)
	screen.blit(bg, (0, 0))
	screen.blit(ball, ballrect)

	pygame.display.flip()
	pygame.time.wait(delay)

