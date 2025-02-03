import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('background.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemys
enemy1Img = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 30

enemy2Img = pygame.image.load('enemy2.png')
enemy2X = random.randint(0, 736)
enemy2Y = random.randint(50, 150)
enemy2X_change = 3
enemy2Y_change = 30

enemy3Img = pygame.image.load('enemy3.png')
enemy3X = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 30

enemy4Img = pygame.image.load('enemy4.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Clock for controlling frame rate
clock = pygame.time.Clock()

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemy1Img, (x, y))
    screen.blit(enemy2Img, (x, y))
    screen.blit(enemy3Img, (x, y))
    screen.blit(enemy4Img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change
    if enemyX <= 0 or enemyX >= 736:
        enemyX_change *= -1
        enemyY += enemyY_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    # Collision detection
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

    # Frame rate cap
    clock.tick(60)
