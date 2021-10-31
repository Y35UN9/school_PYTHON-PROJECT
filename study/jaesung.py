import pygame

pygame.init() #초기화

size = [1400, 800]  #가로 세로
screen = pygame.display.set_mode(size) #가로 세로 설정

title = "Space Ball"
pygame.display.set_caption(title) #제목 설정
# 게임 내 필요한 설정
clock = pygame.time.Clock() #시계
ss = pygame.image.load("apple.png").convert_alpha()
ss = pygame.transform.scale(ss, (200, 200))

color = (0,0,0)
SB = 0

while SB == 0:
    clock.tick(60) #프레임 설정
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1




    screen.fill(color)
    screen.blit(ss, (0,0))

    pygame.display.flip()
