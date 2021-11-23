import pygame
import board

pygame.init()
pygame.display.set_caption("spaceball")
width = 1280
height = 720
voard = board.Board()
screen = pygame.display.set_mode([1280,720])
background_img = pygame.image.load('back_ground.jpg')
background = pygame.transform.scale(background_img, (1280, 720))
space = pygame.image.load(voard.board_img[0])
ball = pygame.image.load(voard.board_img[1])

clock = pygame.time.Clock()

# pygame.mixer.init()
# pygame.mixer.music.load(voard.sound[0])

while voard.board_level < 4:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_END:
                voard.board_level = 4
    
    while voard.board_level == 0:                                        # 게임 시작화면 (0)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:                          # 스페이스바를 누르면 게임시작(1)
                    voard.board_level = 1
                    
        screen.blit(space,(555,360))     
        screen.blit(ball,(555,180)) 
        pygame.display.update()
        
        if voard.board_level == 1:
            screen.blit(background, (0,0))
            pygame.display.flip()
        
        
    while voard.board_level == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_END:
                    voard.board_level = 4
 
    pygame.display.flip()

pygame.quit()