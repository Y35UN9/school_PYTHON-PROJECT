import pygame

class Board:
    def __init__(self, sound = ['spaceBall_startBGM.mp3'], board_img = ['start_BALL.jpg','start_SPACE.jpg'], board_level = 0):
        self.board_level = board_level
        self.sound = sound
        self.board_img = board_img

    def gameOver(self):
        return self.board_level 

    def soundCheck(self):
        return self.sound