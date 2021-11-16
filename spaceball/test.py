import pygame

pygame.init()
pygame.display.set_caption("spaceball")


isActive = True
SCREEN_WIDTH = 1200
SCEREN_HEIGH = 800
clock = pygame.time.Clock()
scereen = pygame.display.set_mode((SCREEN_WIDTH,SCEREN_HEIGH))



def eventProcess():
    global isActive
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                isActive = False
            if event.key == pygame.K_ESCAPE:
                isActive = False
            if event.key == pygame.K_SPACE:
                pass




while(isActive):
    scereen.fill((0,0,0))
    eventProcess()
    pygame.display.update()
    clock.tick(400)