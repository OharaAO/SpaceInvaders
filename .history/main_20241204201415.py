import pygame 
import random 


#initialiser pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((800, 600))


#background
background = pygame.image.load('background.png') 
#Titre et icone de la fenetre
pygame.display.set_caption("Space Inviders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('background.png')

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 30

def player(x,y):
    screen.blit(playerImg, (x, y))


def enemy(x,y):
    screen.blit(enemyImg, (x, y))

#Game loop
running = True
while running:
    # red, green, blue
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#action sur appui de touche
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0


    # empecher le joueur et les ennemis de sortir du champ
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerX += playerX_change

    # mouvement des ennemis
    if enemyX <=0:
        enemyX_change = 0.15
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.15
        enemyY += enemyY_change
    
    enemyX += enemyX_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()