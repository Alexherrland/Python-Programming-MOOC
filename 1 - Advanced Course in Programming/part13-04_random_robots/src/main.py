# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
robot_width, robot_height = robot.get_size()

window.fill((0, 0, 0))

for _ in range(1000):
    x = random.randint(0, 640 - robot_width)
    y = random.randint(0, 480 - robot_height)
    window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
