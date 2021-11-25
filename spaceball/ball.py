import random

class Ball():
    def __init__(self, ball_speed = 0, earth_img = 'image\earth.jpg',meteor_img = 'image\meteor.jpg'):
        self.earth_img = earth_img
        self.meteor_img = meteor_img
        self.ball_speed = ball_speed

    def ranBall(self):
        cntball = random.randint(15,24)
            # 공의 갯수를 지정함
            # x 위치 변경
    


    def upSpeed(self):
        ball_speed += 0