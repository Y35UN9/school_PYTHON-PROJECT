import random
import pygame

class Ball():
    def __init__(self, ball_speed = 0.5, earth_img = 'image\earth.jpg',meteor_img = 'image\meteor.jpg'):
        self.earth_img = earth_img
        self.meteor_img = meteor_img
        self.ball_speed = ball_speed
       
    def ranBall(self):
        return random.uniform(1.3, 2)
        
    
    # def upSpeed(self):
    #     self.ball_speed += 0.0005