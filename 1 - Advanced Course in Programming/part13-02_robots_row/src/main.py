import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")
robot_width, robot_height = robot.get_size()

window.fill((0, 0, 0))

spacing = (640 - (10 * robot_width)) // 11

for i in range(10):
    x = spacing + i * (robot_width + spacing)
    window.blit(robot, (x, (480 - robot_height) // 2))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
