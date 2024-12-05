import pygame 

#initialiser pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((800, 600))

#Titre et icone de la fenetre
pygame.display.set_caption("Space Inviders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = 370
enemyY = 480
enemyX_change = 0

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


    # empecher le joueur de sortir du champ
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    playerX += playerX_change
    player(playerX, playerY)
    enemy(playerX, playerY)
    pygame.display.update()