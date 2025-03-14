# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()
direction = "right"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if direction == "right":
        x += velocity
        if velocity > 0 and x+robot.get_width() >= 640:
            direction = "bottom"
    if direction == "bottom":
        y += velocity
        if velocity > 0 and y+ robot.get_height() >= 480:
            direction = "left"
    if direction == "left":
        x -= velocity
        if velocity > 0 and x <= 0:
            direction = "up"
    if direction == "up":
        y -= velocity
        if velocity > 0 and y <= 0:
            direction= "right"

    clock.tick(60)