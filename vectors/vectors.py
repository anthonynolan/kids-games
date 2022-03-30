import pygame


BLACK = (0,0,0)
RED = (255,0,0)
SHIP_RADIUS = 15
WIDTH, HEIGHT = (640, 480)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

clock = pygame.time.Clock()

x, y = WIDTH//2, HEIGHT//2
speed_x = 2000
speed_y = 150

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()

    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000

    x+=speed_x*time_passed_seconds
    y+=speed_y*time_passed_seconds

    if x > WIDTH-SHIP_RADIUS or x< 0+SHIP_RADIUS:
        speed_x = -speed_x

    if y > HEIGHT-SHIP_RADIUS or y< 0+SHIP_RADIUS: 
        speed_y = -speed_y

    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, (x, y), SHIP_RADIUS)

    pygame.display.update()