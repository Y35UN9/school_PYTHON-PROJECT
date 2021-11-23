import pygame

pygame.init() # 게임 초기화

size = [400, 900]
screen = pygame.display.set_mode(size)

title = "Space Ball"
pygame.display.set_caption(title)

clock = pygame.time.Clock()
color = (0, 0, 0)

SB = 0
while SB == 0:
    
    clock.tick(60)
    # 입력 감지
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             SB = 1

    screen.fill(color)

    pygame.display.flip()

pygame.quit()