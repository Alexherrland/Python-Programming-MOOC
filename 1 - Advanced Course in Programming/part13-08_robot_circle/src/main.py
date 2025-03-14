# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

robots = 10
radius = 150
center_x, center_y = 320, 240
angle_step = 2 * math.pi / robots
angles = [i * angle_step for i in range(robots)]
speed = 0.02
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    
    for i in range(robots):
        x = center_x + radius * math.cos(angles[i]) - robot.get_width() / 2
        y = center_y + radius * math.sin(angles[i]) - robot.get_height() / 2
        window.blit(robot, (x, y))
        angles[i] += speed
    
    pygame.display.flip()
    clock.tick(60)