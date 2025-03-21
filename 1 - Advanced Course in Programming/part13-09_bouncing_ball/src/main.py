# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("src/ball.png")

x, y = 320, 240
velocity_x, velocity_y = 3, 3
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    x += velocity_x
    y += velocity_y
    
    if x + ball.get_width() >= 640 or x <= 0:
        velocity_x *= -1
    if y + ball.get_height() >= 480 or y <= 0:
        velocity_y *= -1
    
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()
    clock.tick(60)