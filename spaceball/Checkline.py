import pygame

class Checkline():
    def __init__ (self,perfect,good,checkline_img='image\checkline.png'):
        self.checkline_img = checkline_img
        self.perfect = perfect
        self.good = good

    def lineScan(self):
        pass