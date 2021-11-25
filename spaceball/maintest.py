import pygame
import board
import ball

pygame.init()
pygame.display.set_caption("spaceball")
# pygame.mixer.init()
# pygame.mixer.pre_init(44100,-16,2,512)

voard = board.Board()  # board 모듈에 Board 클래스를 v(virtual)oard에 저장
vall = ball.Ball()     # ball 모듇에 Ball 클래스를 v(virtual)all에 저장

screen = pygame.display.set_mode([1280,720])                    # 게임화면 가로 세로

background_img = pygame.image.load('image/back_ground.jpg')     # 그냥 검정화면(화면을 초기화 하기 위한 검은색 화면, 덮는 용도임)
background = pygame.transform.scale(background_img, (1280, 720))#

space = pygame.image.load(voard.board_img[0])                   # 시작화면 SPACE
ball = pygame.image.load(voard.board_img[1])                    # 시작화면 BALL

earth = pygame.image.load(vall.earth_img)                       # class BAll에 있는 지구 이미지
earth = pygame.transform.scale(earth, (100, 100))               # 사이즈 조절 (지구)

meteor = pygame.image.load(vall.meteor_img)                     # class BALL에 있는 메테오 이미지
meteor = pygame.transform.scale(meteor, (140, 140))             # 사이즈 조절 (메테오)

earth_pos_x = -1                                                     
earth_pos_y = 555                                               


clock = pygame.time.Clock()                                     # 프레임 때문에 

pygame.mixer.init()
pygame.mixer.music.load(voard.sound[0])

while voard.board_level < 4:
    pygame.mixer.music.play()
    clock.tick(100)
    while voard.board_level == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:                          # 스페이스바를 누르면 게임시작(1)
                    voard.board_level = 1
                    pygame.mixer.music.stop()
                    
        screen.blit(space,(555,180))     
        screen.blit(ball,(555,360)) 
        pygame.display.update()
        
        if voard.board_level == 1:
            screen.blit(background, (0,0))
            pygame.display.flip()
        
        
    while voard.board_level == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_END:
                    voard.board_level = 4

        earth_pos_x += 60 * clock.get_time() / 1000
        screen.blit(earth,(earth_pos_x,earth_pos_y))

        pygame.display.update()
    


    while voard.board_level == 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_END:
                    voard.board_level = 4
 
    pygame.display.flip()

pygame.quit()