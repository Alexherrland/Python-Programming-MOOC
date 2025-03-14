# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
robot_width, robot_height = robot.get_width(), robot.get_height()

x = random.randint(0, 640 - robot_width)
y = random.randint(0, 480 - robot_height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if x <= mouse_x <= x + robot_width and y <= mouse_y <= y + robot_height:
                x = random.randint(0, 640 - robot_width)
                y = random.randint(0, 480 - robot_height)

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
