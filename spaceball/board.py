class Board:
    def __init__(self, sound = ['mp3\spaceBall_startBGM.mp3'], board_img = ['image\start_SPACE.jpg','image\start_BALL.jpg'], board_level = 0):
        self.board_level = board_level
        self.sound = sound
        self.board_img = board_img

    def gameOver(self):
        return self.board_level 

    def soundCheck(self):
        return self.sound