import pygame
import random
import time
import score
import board

class Checkline():
    def __init__ (self,perfect, good,checkline_img='image\checkline.png'):
        self.checkline_img = checkline_img
        self.perfect = perfect
        self.good = good

    def lineScan(self):
        try:
            if earth_x[rm_ball] >= 785 and earth_x[rm_ball] <= 845:
                earth_x[rm_ball] = -1
                del earth_x[rm_ball]
                return self.perfect
            elif earth_x[rm_ball] >= 750 and earth_x[rm_ball] <= 870:
                earth_x[rm_ball] = -1
                del earth_x[rm_ball]
                return self.good
            if meteor_x >= 750 and meteor_x <= 870:
                vcore.now_score = 0
        except IndexError:
            voard.board_level = 2

class Ball():
    def __init__(self, ball_speed = 0.35, earth_img = 'image\earth.jpg',meteor_img = 'image\meteor.jpg'):
        self.earth_img = earth_img
        self.meteor_img = meteor_img
        self.ball_speed = ball_speed
       
    def ranBall(self):
        for j in range(len(earth_x)):
            screen.blit(earth,(earth_x[j], earth_y))

    def up_Speed(self):
        return self.ball_speed

pygame.init()
pygame.display.set_caption("spaceball")

voard = board.Board()  # board 모듈에 Board 클래스를 v(virtual)oard에 저장
vall = Ball()
vheckline = Checkline(10, 5)
vcore = score.Score()

screen = pygame.display.set_mode([1080,720])                    # 게임화면 가로 세로

background_img = pygame.image.load('image/back_ground.jpg')     # 그냥 검정화면(화면을 초기화 하기 위한 검은색 화면, 덮는 용도임)
background = pygame.transform.scale(background_img, (1280, 720))
space = pygame.image.load(voard.board_img[0])                   # 시작화면 SPACE
ball = pygame.image.load(voard.board_img[1])                    # 시작화면 BALL
scoreboard = pygame.image.load(vcore.scoreboard_img)
scoreboard = pygame.transform.scale(scoreboard, (250, 200))
game_font = pygame.font.Font(None,70)
press = game_font.render("Please press SPACE BAR!", True, (255,255,255))
p_or_g =game_font.render("", True, (255,255,255))
nscore =game_font.render("", True, (255,255,255))
restart_font = pygame.font.Font(None,35)
re_continue = restart_font.render("continue?", True, (255,255,255))
restart_space = restart_font.render("PRESS SPACE BAR!", True, (255,255,255))
exit_click = restart_font.render("EXIT - ESC", True, (255,255,255))
earth = pygame.image.load(vall.earth_img)                       # class BAll에 있는 지구 이미지
earth = pygame.transform.scale(earth, (100, 100))               # 사이즈 조절 (지구)
earth_x = [0]
earth_y = 300  
i = 0
rm_ball = 0

morescore = 0

meteor = pygame.image.load(vall.meteor_img)                     # class BALL에 있는 메테오 이미지
meteor = pygame.transform.scale(meteor, (140, 140))
meteor_x = -1
random_meteor = random.randint(1, 100)

checkline = pygame.image.load(vheckline.checkline_img)
checkline = pygame.transform.scale(checkline,(50,1000))

ran = 0

game_time = pygame.time.get_ticks()

clock = pygame.time.Clock()                                     # 프레임 때문에 

pygame.mixer.init()
voard.soundCheck()

pygame.mixer.music.play()
clock.tick(100)
while voard.board_level <= 2:
    while voard.board_level == 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:                          # 스페이스바를 누르면 게임시작(1)
                    voard.board_level = 1
                    start = time.time()
                    pygame.mixer.music.stop()
                elif event.key == pygame.K_ESCAPE:
                    voard.board_level = 4

        screen.blit(press,(230,290))
        screen.blit(space,(455,160))     
        screen.blit(ball,(455,380))
        screen.blit(earth,(20,20))
        screen.blit(earth,(960,600))
        screen.blit(meteor,(940,15))
        screen.blit(meteor,(5,600))
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
                    click_score = vheckline.lineScan()
                    if click_score == 10:
                        p_or_g = game_font.render("Perfect!!!", True, (255,255,255))
                        morescore = 10
                    elif click_score == 5:
                        p_or_g = game_font.render("Good!", True, (255,255,255))
                        morescore = 5
                    nscore = game_font.render("" + str(int(vcore.nowScan(morescore))), True, (255,255,255))

        score_font = pygame.font.Font(None,15)
        bscore = game_font.render("" + str(int(vcore.bestScore())), True, (255,255,255))
        running_time = (pygame.time.get_ticks() - game_time) / 1000 +1
        screen.blit(checkline,(820,0))
        ran = random.uniform(1.3, 2.0)
        if time.time() - start > ran:
            vall.ranBall()
            start = time.time()
            earth_x.append(0)
            i += 1
        if random_meteor == 1:
            screen.blit(meteor,(meteor_x, 280))
            meteor_x += 1
        if meteor_x > 1080 or random_meteor != 1:
            random_meteor = random.randint(0, 29)
            meteor_x = -1

        for j in range(len(earth_x)):
            earth_x[j] += vall.up_Speed()

        vall.ranBall()
        screen.blit(p_or_g,(50,600))
        screen.blit(scoreboard,(30,10))
        screen.blit(nscore,(180, 120))
        screen.blit(bscore,(65, 120))
        pygame.display.update()
        screen.fill((0,0,0))

        if int(running_time) % 10 == 0:
            vall.ball_speed += 0.001
        
        for j in range(len(earth_x)):
            if  earth_x[j] > 1000:
                voard.board_level = 2

    while voard.board_level == 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    voard.board_level = 4
                elif event.key == pygame.K_SPACE:
                    earth_x = []
                    screen.blit(background, (0,0))
                    pygame.display.flip()
                    p_or_g =game_font.render("", True, (255,255,255))
                    nscore =game_font.render("", True, (255,255,255))
                    i = 0
                    meteor_x = -1
                    rm_ball = 0
                    vcore.now_score = 0
                    morescore = 0
                    vall.ball_speed = 0.35
                    voard.board_level = 1
        
        screen.blit(background, (0,0))
        screen.blit(scoreboard,(410,190))
        screen.blit(nscore,(540, 300))
        screen.blit(bscore,(425, 300))
        screen.blit(re_continue,(480, 450))
        screen.blit(restart_space,(430, 500))
        screen.blit(exit_click,(470, 600))
        pygame.display.flip()
                
 
pygame.display.flip()
pygame.quit()