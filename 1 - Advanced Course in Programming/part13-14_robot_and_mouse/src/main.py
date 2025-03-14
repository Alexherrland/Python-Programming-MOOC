# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
robot_width, robot_height = robot.get_width(), robot.get_height()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    x = mouse_x - robot_width // 2
    y = mouse_y - robot_height // 2
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    clock.tick(60)
