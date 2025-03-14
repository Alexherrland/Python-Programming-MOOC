# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
robot_width, robot_height = robot.get_size()

window.fill((0, 0, 0))

spacing_y = 50 
spacing_x_increment = 10  

for row in range(10):
    for col in range(10):
        x = col * robot_width + row * spacing_x_increment 
        y = row * (robot_height - spacing_y) 
        window.blit(robot, (x, y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
