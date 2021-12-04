import pygame

class Board:
    def __init__(self, sound = ['mp3\spaceBall_startBGM.mp3'], board_img = ['image\start_SPACE.jpg','image\start_BALL.jpg'], board_level = 0):
        self.board_level = board_level
        self.sound = sound
        self.board_img = board_img

    def soundCheck(self):
        pygame.mixer.music.load(self.sound[0])  # 0을 board_level로 변경해야함