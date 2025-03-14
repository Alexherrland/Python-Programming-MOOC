# WRITE YOUR SOLUTION HERE:
import pygame
import time
import math

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

center_x, center_y = 200, 200
radius = 100

def draw_hand(angle, length, color, thickness):
    end_x = center_x + length * math.cos(math.radians(angle))
    end_y = center_y - length * math.sin(math.radians(angle))
    pygame.draw.line(window, color, (center_x, center_y), (end_x, end_y), thickness)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    hour_angle = 90 - (hours * 30 + minutes * 0.5)
    minute_angle = 90 - (minutes * 6)
    second_angle = 90 - (seconds * 6)

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), (center_x, center_y), radius, 2)

    draw_hand(hour_angle, 50, (0, 0, 255), 6)
    draw_hand(minute_angle, 70, (0, 0, 255), 4)
    draw_hand(second_angle, 80, (0, 0, 255), 2)


    pygame.display.flip()
    clock.tick(1)
