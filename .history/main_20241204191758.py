import pygame 

#initialiser pygame
pygame.init()

# créer la fenetre
screen = pygame.display.set_mode((800, 600))

#Titre et icone de la fenetre
pygame.display.set_caption("Space Inviders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerImg, (x, y))

#Game loop
running = True
while running:
    # red, green, blue
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.
    

    player(playerX, playerY)
    pygame.display.update()