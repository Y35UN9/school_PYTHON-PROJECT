import pygame
import board

pygame.init()
pygame.display.set_caption("spaceball")
width = 1280
height = 720
screen = pygame.display.set_mode([width, height])
voard = board.Board()
space = pygame.image.load(voard.board_img[0])
#num = .transform.scale(num,())
ball = pygame.image.load(voard.board_img[1])

t= True
while t:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_END:
                t = False
    screen.blit(space,(555,360))
    screen.blit(ball,(555,180))  # 가로 세로
    pygame.display.update()

    pygame.display.flip()

pygame.quit()