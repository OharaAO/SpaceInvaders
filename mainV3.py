import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('images/background.png')

# Player
playerImg = pygame.image.load('images/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6  # Number of enemies

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(30)

# Bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletY_change = 10
bullets = []  # List to store multiple bullets

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)  # Default font and size
textX = 10
textY = 10

GameOver_Font = pygame.font.Font('freesansbold.ttf', 50)
GameOver_X = 320
GameOver_Y = 320

# Clock for controlling frame rate
clock = pygame.time.Clock()

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    bullets.append([x, y])  # Add a new bullet to the list

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

def show_score(x, y):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
    screen.blit(score_text, (x, y))

def show_gameOver(x,y):
    GameOvertxt= font.render("Game Over",True ,(255,255,255))
    screen.blit(GameOvertxt,(x,y))

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
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, playerY)  # Fire a new bullet

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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= 736:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Game Over condition
        if enemyY[i] > 440:
            show_gameOver(GameOver_X,GameOver_Y)
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move all enemies off-screen

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    for bullet in bullets:
        bullet[1] -= bulletY_change  # Move the bullet up
        screen.blit(bulletImg, (bullet[0] + 16, bullet[1] + 10))  # Draw the bullet
        if bullet[1] <= 0:
            bullets.remove(bullet)  # Remove the bullet if it goes off-screen

    # Collision detection
    for bullet in bullets:
        for i in range(num_of_enemies):
            if is_collision(enemyX[i], enemyY[i], bullet[0], bullet[1]):
                bullets.remove(bullet)  # Remove the bullet on collision
                score += 1  # Increment score
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)
                break

    player(playerX, playerY)
    show_score(textX, textY)  # Display the score
    pygame.display.update()

    # Frame rate cap
    clock.tick(60)