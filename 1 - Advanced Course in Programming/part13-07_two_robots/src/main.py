# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

x1, y1 = 100, 100
x2, y2 = 100, 300
velocity1 = 2
velocity2 = 4
direction1 = 1
direction2 = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    
    x1 += velocity1 * direction1
    x2 += velocity2 * direction2
    
    if x1 + robot.get_width() >= 640 or x1 <= 0:
        direction1 *= -1
    if x2 + robot.get_width() >= 640 or x2 <= 0:
        direction2 *= -1
    
    clock.tick(60)
