# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

robots = []
clock = pygame.time.Clock()

def spawn_robot():
    x = random.randint(0, 640 - robot.get_width())
    y = -robot.get_height()
    velocity_y = random.randint(2, 5)
    velocity_x = random.choice([-2, 2])
    return [x, y, velocity_x, velocity_y, False]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    if random.random() < 0.02:
        robots.append(spawn_robot())
    
    window.fill((0, 0, 0))
    
    for robot_data in robots[:]:
        x, y, velocity_x, velocity_y, grounded = robot_data
        
        if not grounded:
            y += velocity_y
            if y + robot.get_height() >= 480:
                y = 480 - robot.get_height()
                grounded = True
        else:
            x += velocity_x
        
        if x < -robot.get_width() or x > 640:
            robots.remove(robot_data)
        else:
            robot_data[0], robot_data[1], robot_data[4] = x, y, grounded
            window.blit(robot, (x, y))
    
    pygame.display.flip()
    clock.tick(60)