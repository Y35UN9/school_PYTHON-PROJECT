import pygame
import ball
import random
import time

class Board:
    def __init__(self, sound = ['mp3\spaceBall_startBGM.mp3'], board_img = ['image\start_SPACE.jpg','image\start_BALL.jpg'], board_level = 0):
        self.board_level = board_level
        self.sound = sound
        self.board_img = board_img

    def gameOver(self):
        return self.board_level 

    def soundCheck(self):
        return self.sound

class Checkline():
    def __init__ (self,perfect, good,checkline_img='image\checkline.png'):
        self.checkline_img = checkline_img
        self.perfect = perfect
        self.good = good

    def lineScan(self):
        global earth_pos_x
        global earth2_pos_x
        global earth3_pos_x
        if nextclick_ball == 1:
            if earth_pos_x >= 970 and earth_pos_x <= 1050:
                earth_pos_x = -1
                return self.perfect
            elif earth_pos_x >= 950 and earth_pos_x <= 1070:
                earth_pos_x = -1
                return self.good
        elif nextclick_ball == 2:
            if earth2_pos_x >= 970 and earth2_pos_x <= 1050:
                earth2_pos_x = -1
                return self.perfect
            elif earth2_pos_x >= 950 and earth2_pos_x <= 1070:
                earth2_pos_x = -1
                return self.good
        elif nextclick_ball == 3:
            if earth2_pos_x >= 970 and earth2_pos_x <= 1050:
                earth2_pos_x = -1
                return self.perfect
            elif earth2_pos_x >= 950 and earth2_pos_x <= 1070:
                earth2_pos_x = -1
                return self.good

pygame.init()
pygame.display.set_caption("spaceball")

voard = Board()  # board 모듈에 Board 클래스를 v(virtual)oard에 저장
vall = ball.Ball()
vheckline = Checkline(10, 5)

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

nextclick_ball = 0

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nextclick_ball = 1
                vheckline.lineScan()

    running_time = (pygame.time.get_ticks() - game_time) / 1000 +1
    screen.blit(checkline,(1020,0))
    earth_pos_x += vall.ball_speed                                               
    screen.blit(earth,(earth_pos_x,earth_pos_y))
    pygame.display.update()
    screen.fill((0,0,0))
    if int(running_time) % 5 == 0: # 30초 단위로 속도 증가
        vall.upSpeed()
    
    if  earth_pos_x > 1200 :
        voard.board_level = 2
    
    if earth_pos_x > earth2_pos_x:
        nextclick_ball = 1
    elif earth2_pos_x > earth3_pos_x:
        nextclick_ball = 2
    elif earth3_pos_x > earth_pos_x:
        nextclick_ball = 3



while voard.board_level == 2:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_END:
                voard.board_level = 4
 
pygame.display.flip()

pygame.quit()