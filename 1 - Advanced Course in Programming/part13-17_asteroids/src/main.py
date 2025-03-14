# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
asteroid = pygame.image.load("src/rock.png")

robot_width, robot_height = robot.get_width(), robot.get_height()
asteroid_width, asteroid_height = asteroid.get_width(), asteroid.get_height()

robot_x = 320
robot_y = 400
velocity = 5

asteroid_x = random.randint(0, 640 - asteroid_width)
asteroid_y = 0
asteroid_speed = 2

score = 0
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and robot_x > 0:
        robot_x -= velocity
    if keys[pygame.K_RIGHT] and robot_x < 640 - robot_width:
        robot_x += velocity

    asteroid_y += asteroid_speed

    if asteroid_y > 480:
        break

    if robot_x < asteroid_x + asteroid_width and robot_x + robot_width > asteroid_x and \
       robot_y < asteroid_y + asteroid_height and robot_y + robot_height > asteroid_y:
        score += 1
        asteroid_x = random.randint(0, 640 - asteroid_width)
        asteroid_y = 0

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    window.blit(asteroid, (asteroid_x, asteroid_y))
    
    score_text = font.render(f"Points: {score}", True, (255, 0, 0))
    window.blit(score_text, (640-(score_text.get_width()+10), 10))

    pygame.display.flip()
    clock.tick(60)
