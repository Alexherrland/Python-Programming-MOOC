# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("src/robot.png")
robot2 = pygame.image.load("src/robot.png")
robot1_width, robot1_height = robot1.get_width(), robot1.get_height()
robot2_width, robot2_height = robot2.get_width(), robot2.get_height()

x1, y1 = 100, 240
x2, y2 = 540, 240
velocity = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x1 > 0:
        x1 -= velocity
    if keys[pygame.K_RIGHT] and x1 < 640 - robot1_width:
        x1 += velocity
    if keys[pygame.K_UP] and y1 > 0:
        y1 -= velocity
    if keys[pygame.K_DOWN] and y1 < 480 - robot1_height:
        y1 += velocity
    
    if keys[pygame.K_a] and x2 > 0:
        x2 -= velocity
    if keys[pygame.K_d] and x2 < 640 - robot2_width:
        x2 += velocity
    if keys[pygame.K_w] and y2 > 0:
        y2 -= velocity
    if keys[pygame.K_s] and y2 < 480 - robot2_height:
        y2 += velocity
    
    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()
    clock.tick(60)
