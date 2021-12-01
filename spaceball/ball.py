import random
import pygame
class Ball():
    def __init__(self, earth_pos_x = -1,earth_pos_y = 300,ball_speed = 1000, earth_img = 'image\earth.jpg',meteor_img = 'image\meteor.jpg'):
        self.earth_img = earth_img
        self.meteor_img = meteor_img
        self.ball_speed = ball_speed
       
    def ranBall(self):
        rball = random.randint(15,24)
        return rball
        
    
    def upSpeed(self):
        ball_speed -= 50