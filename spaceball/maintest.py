import pygame
import random
import time
import score

class Board:
    def __init__(self, sound = ['mp3\spaceBall_startBGM.mp3'], board_img = ['image\start_SPACE.jpg','image\start_BALL.jpg'], board_level = 0):
        self.board_level = board_level
        self.sound = sound
        self.board_img = board_img

    def soundCheck(self):
        pygame.mixer.music.load(self.sound[0])  # 0을 board_level로 변경해야함

class Checkline():
    def __init__ (self,perfect, good,checkline_img='image\checkline.png'):
        self.checkline_img = checkline_img
        self.perfect = perfect
        self.good = good

    def lineScan(self):
        global earth_pos_x
        global click_ball
        global earth_time
        rm_ball = 0
        for j in range(len(earth_x)):   
            if earth_x[rm_ball] < earth_x[j]:
                rm_ball = j
        if earth_x[rm_ball] >= 870 and earth_x[rm_ball] <= 850:
            earth_x[rm_ball] = -1
            del earth_x[rm_ball]
            return self.perfect
        elif earth_x[rm_ball] >= 750 and earth_x[rm_ball] <= 870:
            earth_x[rm_ball] = -1
            del earth_x[rm_ball]
            return self.good

class Ball():
    def __init__(self, ball_speed = 0.25, earth_img = 'image\earth.jpg',meteor_img = 'image\meteor.jpg'):
        self.earth_img = earth_img
        self.meteor_img = meteor_img
        self.ball_speed = ball_speed
       
    def ranBall(self):
        global earth_x
        for j in range(len(earth_x)):
            screen.blit(earth,(earth_x[j], earth_y))

    def up_Speed(self):
        return self.ball_speed

pygame.init()
pygame.display.set_caption("spaceball")

voard = Board()  # board 모듈에 Board 클래스를 v(virtual)oard에 저장
vall = Ball()
vheckline = Checkline(10, 5)

screen = pygame.display.set_mode([1080,720])                    # 게임화면 가로 세로

background_img = pygame.image.load('image/back_ground.jpg')     # 그냥 검정화면(화면을 초기화 하기 위한 검은색 화면, 덮는 용도임)
background = pygame.transform.scale(background_img, (1280, 720))#

space = pygame.image.load(voard.board_img[0])                   # 시작화면 SPACE
ball = pygame.image.load(voard.board_img[1])                    # 시작화면 BALL

earth = pygame.image.load(vall.earth_img)                       # class BAll에 있는 지구 이미지
earth = pygame.transform.scale(earth, (100, 100))               # 사이즈 조절 (지구)
earth_x = []
earth_y = 300  
i = 0
plus_limit = 0

meteor = pygame.image.load(vall.meteor_img)                     # class BALL에 있는 메테오 이미지
meteor = pygame.transform.scale(meteor, (140, 140))

checkline = pygame.image.load(vheckline.checkline_img)
checkline = pygame.transform.scale(checkline,(50,1000))

click_ball = 0
ran = 0

game_time = pygame.time.get_ticks()

clock = pygame.time.Clock()                                     # 프레임 때문에 

pygame.mixer.init()
voard.soundCheck()

pygame.mixer.music.play()
clock.tick(100)
while voard.board_level == 0:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:                          # 스페이스바를 누르면 게임시작(1)
                voard.board_level = 1
                start = time.time()
                pygame.mixer.music.stop()

    screen.blit(space,(455,180))     
    screen.blit(ball,(455,360))
    pygame.display.update()
        
    if voard.board_level == 1:
        screen.blit(background, (0,0))
        pygame.display.flip()

while voard.board_level == 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                voard.board_level = 4
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vheckline.lineScan()
    
    running_time = (pygame.time.get_ticks() - game_time) / 1000 +1
    screen.blit(checkline,(820,0))
    ran = random.uniform(1, 1.9)
    if time.time() - start > ran:
        vall.ranBall()
        start = time.time()
        earth_x.append(0)
        i += 1

    for j in range(len(earth_x)):
        earth_x[j] += vall.up_Speed()

    vall.ranBall()
    pygame.display.update()
    screen.fill((0,0,0))

    if int(running_time) % 5 == 0: # 30초 단위로 속도 증가
        vall.ball_speed += 0.001
    
    for j in range(len(earth_x)):
        if  earth_x[j] > 1000:
            voard.board_level = 2

    print(running_time)


while voard.board_level == 2:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                voard.board_level = 4
 
pygame.display.flip()
pygame.quit()