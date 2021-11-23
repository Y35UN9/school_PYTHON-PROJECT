import pygame

class Board:
    def __init__(self,sound,board_img,board_level=0):
        self.board_level = board_level
        self.sound = sound
        self.board_img = board_img

    def gameOver(self):
        self.board_level = 2
        return self.board_level

    def soundCheck(self):
        return self.sound
        