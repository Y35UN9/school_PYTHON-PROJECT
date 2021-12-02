import pygame
import board
import ball
import checkline
import random
import time

pygame.init()
pygame.display.set_caption("spaceball")

voard = board.Board()  # board 모듈에 Board 클래스를 v(virtual)oard에 저장
vall = ball.Ball()     # ball 모듇에 Ball 클래스를 v(virtual)all에 저장
vheckline = checkline.Checkline(10, 5)

screen = pygame.display.set_mode([1280,720])                    # 게임화면 가로 세로

background_img = pygame.image.load('image/back_ground.jpg')     # 그냥 검정화면(화면을 초기화 하기 위한 검은색 화면, 덮는 용도임)
background = pygame.transform.scale(background_img, (1280, 720))#

space = pygame.image.load(voard.board_img[0])                   # 시작화면 SPACE
ball = pygame.image.load(voard.board_img[1])                    # 시작화면 BALL

earth = pygame.image.load(vall.earth_img)                       # class BAll에 있는 지구 이미지
earth = pygame.transform.scale(earth, (100, 100))               # 사이즈 조절 (지구)
earth2 = pygame.image.load(vall.earth_img)
earth2 = pygame.transform.scale(earth, (100, 100))
earth3 = pygame.image.load(vall.earth_img)
earth3 = pygame.transform.scale(earth, (100, 100))

meteor = pygame.image.load(vall.meteor_img)                     # class BALL에 있는 메테오 이미지
meteor = pygame.transform.scale(meteor, (140, 140))

checkline = pygame.image.load(vheckline.checkline_img)
checkline = pygame.transform.scale(checkline,(50,1200))

earth_pos_x = -1                                                     
earth_pos_y = 300                                              
earth2_pos_x = -1
earth2_pos_y = 300
earth3_pos_x = -1
earth3_pos_y = 300

game_time = pygame.time.get_ticks()

clock = pygame.time.Clock()                                     # 프레임 때문에 

pygame.mixer.init()
pygame.mixer.music.load(voard.sound[0])



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
    running_time = (pygame.time.get_ticks() - game_time) / 1000 +1
    # rball의 개수만큼 랜덤으로 공 출력 반복 ( rball -= 1 을 반복하다가 0이되면 rball 다시 받아오기 )
    screen.blit(checkline,(1020,0))
    earth_pos_x += vall.ball_speed                                               
    screen.blit(earth,(earth_pos_x,earth_pos_y))
    if int(running_time) >= 5: # 3초 넘기면 대미지 오브젝트 추가
        screen.blit(earth2,(earth2_pos_x,earth2_pos_y))
        earth2_pos_x += vall.ball_speed
    pygame.display.update()
    screen.fill((0,0,0))
    print(running_time)
    if int(running_time) % 5 == 0: # 30초 단위로 속도 증가
        vall.upSpeed()
    
    if  earth_pos_x > 1200 :
        voard.board_level = 2



while voard.board_level == 2:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_END:
                voard.board_level = 4
 
pygame.display.flip()

pygame.quit()