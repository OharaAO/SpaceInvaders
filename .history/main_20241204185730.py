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
playerY = 

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # red, green, blue
    screen.fill((0,0,0))
    pygame.display.update()