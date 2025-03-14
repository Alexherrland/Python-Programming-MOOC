import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Alex Herrerias - Part 14")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_img = pygame.image.load("src/robot.png")
coin_img = pygame.image.load("src/coin.png")
enemy_img = pygame.image.load("src/monster.png")

player = pygame.Rect(400, 500, 50, 50)
coins = [pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30) for _ in range(5)]
enemies = [pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30) for _ in range(3)]

score = 0
speed = 5
lives = 3
running = True

def move_player(keys):
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y < HEIGHT - player.height:
        player.y += speed

def move_enemies():
    for enemy in enemies:
        enemy.y += 3
        if enemy.y > HEIGHT:
            enemy.y = -30
            enemy.x = random.randint(0, WIDTH-30)

def check_collisions():
    global score, lives
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            coins.append(pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30))
            score += 1
    for enemy in enemies:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            lives -= 1
            if lives == 0:
                return False
    return True

def draw():
    screen.fill((30, 30, 30))
    screen.blit(player_img, (player.x, player.y))
    for coin in coins:
        screen.blit(coin_img, (coin.x, coin.y))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.x, enemy.y))
    score_text = pygame.font.Font(None, 36).render(f"Score: {score}", True, (255, 255, 255))
    lives_text = pygame.font.Font(None, 36).render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    pygame.display.flip()

def game_over():
    screen.fill((0, 0, 0))
    text = pygame.font.Font(None, 50).render("Game Over", True, (255, 0, 0))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(2000)

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    move_player(pygame.key.get_pressed())
    move_enemies()
    running = check_collisions()
    draw()

    if not running:
        game_over()

pygame.quit()