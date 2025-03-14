# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
robot_width, robot_height = robot.get_width(), robot.get_height()

x, y = 320, 240
velocity = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 640 - robot_width:
        x += velocity
    if keys[pygame.K_UP] and y > 0:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 480 - robot_height:
        y += velocity
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
