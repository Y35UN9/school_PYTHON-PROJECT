import pygame

class Score():
    def __init__(self, scoreboard_img='image\scoreboard.png',now_score = 0,best_score = 0):
        self.now_score = now_score
        self.best_score = best_score
        self.scoreboard_img = scoreboard_img

    def nowScan(self, morescore):
        self.now_score += morescore
        return self.now_score

    def bestScore(self):
        if self.now_score > self.best_score:
            self.best_score = self.now_score
        return self.best_score